# Pashu Sentinel — Production Deployment Guide

This guide details the two official deployment methods for Pashu Sentinel: the live zero-setup web application hosted on GitHub Pages, and the full-stack containerized deployment via Docker Compose.

---

## 🌐 1. Live Web Application (GitHub Pages)

The frontend PWA is live in production at:
👉 **[https://akt1410.github.io/PashuSentinel/](https://akt1410.github.io/PashuSentinel/)**

### Overview
- **Zero-Setup Access**: Runs immediately in any desktop or mobile browser.
- **Offline-First Resilience**: Powered by Workbox service workers and Dexie.js (IndexedDB). If a network connection is unavailable, field reports, triage simulations, and GIS maps function client-side.
- **Automated CI/CD**: Every push to the `main` branch triggers `.github/workflows/deploy-pages.yml`, which runs unit checks, builds the production Vite bundle, and publishes updates to GitHub Pages automatically.
- **Client Routing**: Configured with SPA redirect fallbacks (`404.html`) to ensure deep routes like `/farmer`, `/vet`, and `/dashboard` resolve cleanly without 404 errors.

---

## 🐳 2. Full-Stack Containerized Deployment (Docker Compose)

For production deployments requiring the complete backend API, spatial database, and ML inference engine, Pashu Sentinel provides a production Docker Compose orchestration.

### Architecture
```
                         +-----------------------------+
                         |      Client Browsers        |
                         |   (Mobile PWA / Offline)    |
                         +--------------+--------------+
                                        | HTTPS (Port 80)
                                        v
                         +-----------------------------+
                         |   pashu_prod_frontend       |
                         |  (Nginx Alpine + React PWA) |
                         +--------------+--------------+
                                        | REST (Port 8000)
                                        v
                         +-----------------------------+
                         |   pashu_prod_backend        |
                         |  (FastAPI + ML Intelligence)|
                         +------+---------------+------+
                                |               |
           Port 5432            |               | Local ONNX Embeddings
                                v               v
            +----------------------+  +----------------------+
            |   pashu_prod_postgis |  |   ChromaDB Vector    |
            | (PostGIS 16-3.4)     |  |   (18 Protocol Docs) |
            +----------------------+  +----------------------+
```

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akt1410/PashuSentinel.git
   cd PashuSentinel
   ```

2. **Configure Environment Variables** (optional — sensible defaults are provided):
   ```bash
   cat << 'ENV' > .env.prod
   POSTGRES_DB=pashu_sentinel
   POSTGRES_USER=pashu
   POSTGRES_PASSWORD=pashu_secure_password
   SECRET_KEY=9b7f92e0cbfae4210b37dc18d6a858e7c10b40a32e1858a8a47bfb3cb4ee08e6
   GROQ_API_KEY=
   CORS_ORIGINS=http://localhost,http://localhost:80
   VITE_API_URL=http://localhost:8000
   ENV
   ```

3. **Build & Start Services**:
   ```bash
   docker compose -f docker-compose.prod.yml up -d --build
   ```

4. **Verify Container Health**:
   ```bash
   docker compose -f docker-compose.prod.yml ps
   ```

   All 3 services will report healthy:
   - **Frontend**: `http://localhost:80`
   - **Backend API**: `http://localhost:8000`
   - **API Docs (Swagger)**: `http://localhost:8000/docs`
   - **Health Endpoint**: `http://localhost:8000/health`

### Service Management
- **View logs**: `docker compose -f docker-compose.prod.yml logs -f`
- **Stop services**: `docker compose -f docker-compose.prod.yml down`
- **Stop & wipe volumes**: `docker compose -f docker-compose.prod.yml down -v`

---

## 🔒 Security Best Practices
- **Non-Root Execution**: Backend containers run under unprivileged user `appuser` (UID 1000).
- **Graceful DB Fallback**: Backend automatically connects to PostgreSQL/PostGIS in production, and falls back to SQLite for single-file local execution.
