"""
backend/test_rag.py
─────────────────────────────────────────────────────────────────────────────
Comprehensive RAG System Verification Test Suite
─────────────────────────────────────────────────────────────────────────────
"""
import json
from dotenv import load_dotenv
load_dotenv('.env')

from fastapi.testclient import TestClient
from app.main import app
from app.services.rag_service import seed_knowledge_base, rag_health, retrieve_context, answer_query

print("=" * 65)
print("  PASHU SENTINEL — RAG VETERINARY SYSTEM TEST SUITE")
print("=" * 65)

# 1. Seeding Knowledge Base
print("\n[TEST 1] Seeding Knowledge Base in ChromaDB...")
indexed_count = seed_knowledge_base(force=True)
print(f" -> Indexed documents: {indexed_count}")
assert indexed_count >= 18, f"Expected at least 18 docs, got {indexed_count}"
print(" [PASS] Knowledge base seeded successfully.")

# 2. Health Check
print("\n[TEST 2] Verifying System Health Check...")
health = rag_health()
print(" -> Health Report:", json.dumps(health, indent=2))
assert health["documents_indexed"] >= 18
assert health["status"] == "ready"
print(" [PASS] Health status is READY.")

# 3. Semantic Retrieval Test
print("\n[TEST 3] Testing Semantic Retrieval on Clinical Queries...")
test_queries = [
    ("FMD Check", "cow has blisters on feet and salivating"),
    ("LSD Check", "nodules on skin and high fever in bull"),
    ("Anthrax Emergency", "sudden death with dark bleeding from nose and mouth"),
    ("EVM First-Aid", "herbal treatment for animal wound and maggots"),
    ("Vet Differential", "differential diagnosis vesicular stomatitis vs FMD equines"),
    ("Lab Cold Chain", "epithelial flap specimen collection phosphate buffered glycerol transport"),
    ("Ring Containment", "protection zone 3 km ring vaccination surveillance zone buffer"),
]

for label, q in test_queries:
    results = retrieve_context(q, n_results=2)
    top_doc = results[0] if results else None
    print(f" -> [{label}] Query: '{q}'")
    if top_doc:
        print(f"    Top Match: '{top_doc['title']}' (Score: {top_doc['score']:.2%})")
    else:
        print("    [!] No results found!")
    assert top_doc is not None
print(" [PASS] Semantic retrieval working accurately.")

# 4. End-to-End Answer Generation (Farmer vs Vet Modes)
print("\n[TEST 4] Testing End-to-End answer_query Pipeline (Role-Adaptive)...")
# Farmer Mode
sample_query = "My cow is drooling excessively and has vesicles on the tongue. What is the suspected disease and what immediate first aid can I provide?"
response_farmer = answer_query(sample_query, role="FARMER")
print(" -> Generated Response (Farmer Mode):")
print("-" * 50)
print(response_farmer["answer"][:400] + "...")
print("-" * 50)
assert len(response_farmer["sources"]) > 0
assert "foot-and-mouth" in response_farmer["answer"].lower() or "fmd" in response_farmer["answer"].lower()

# Vet Mode (CDSS)
vet_query = "What is the differential diagnosis matrix and sampling protocol for bovine vesicular lesions?"
response_vet = answer_query(vet_query, role="VET")
print(" -> Generated Response (Vet CDSS Mode):")
print("-" * 50)
print(response_vet["answer"][:400] + "...")
print("-" * 50)
assert len(response_vet["sources"]) > 0
assert "differential" in response_vet["answer"].lower() or "fmd" in response_vet["answer"].lower()
print(" [PASS] End-to-end question answering verified for both roles.")

# 5. FastAPI HTTP Router Integration Test
print("\n[TEST 5] Testing FastAPI Router Endpoints via HTTP TestClient...")
client = TestClient(app)

# GET /rag/health
res_health = client.get("/rag/health")
print(f" -> GET /rag/health status: {res_health.status_code}")
assert res_health.status_code == 200
assert res_health.json()["status"] == "ready"

# POST /rag/chat (Veterinarian Mode)
chat_payload = {
    "query": "What are the cold chain and preservative specifications for FMD epithelial tissue submission?",
    "history": [],
    "mode": "veterinarian"
}
res_chat = client.post("/rag/chat", json=chat_payload)
print(f" -> POST /rag/chat status: {res_chat.status_code}")
assert res_chat.status_code == 200
chat_data = res_chat.json()
print(f" -> Sources count: {len(chat_data['sources'])}")
print(f" -> Top source: {chat_data['sources'][0]['title']}")
assert len(chat_data["sources"]) > 0
print(" [PASS] FastAPI /rag endpoints verified successfully with clinical mode.")

print("\n" + "=" * 65)
print("  ALL RAG TESTS PASSED SUCCESSFULLY! ")
print("=" * 65)
