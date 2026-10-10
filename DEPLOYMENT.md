# Pashu Sentinel — Production Deployment Guide

This guide provides end-to-end instructions for deploying Pashu Sentinel to production across both free-tier cloud platforms and dedicated container infrastructure.

---

## Architecture Topology

```
                         +-----------------------------+
                         |      Client Browsers        |
                         |    (Offline PWA / Mobile)   |
                         +--------------+--------------+
                                        | HTTPS
                                        v
                         +-----------------------------+
                         |       Frontend CDN          |
                         |   (Vercel / Nginx Alpine)   |
                         +--------------+--------------+
                                        | REST / JSON
                                        v
                         +-----------------------------+
                         |        FastAPI Core         |
                         |   (Render / Docker / Uvicorn)|
                         +------+---------------+------+
                                |               |
          SQL / GeoAlchemy      |               | Local ONNX / Groq API
                                v               v
            +----------------------+  +----------------------+
            |   PostGIS Spatial    |  |   ChromaDB Vector    |
            | (Supabase / Postgres)|  |   (Knowledge Store)  |
            +----------------------+  +----------------------+
```

---

## Strategy A: Zero-Cost Cloud Deployment (Recommended)

This setup runs entirely on production-grade free tiers with 99.9% uptime.

### Step 1: Database (Supabase PostgreSQL + PostGIS)
1. Create a free project at [supabase.com](https://supabase.com).
2. In the Supabase SQL Editor, enable PostGIS:
   ```sql
   CREATE EXTENSION IF NOT EXISTS postgis;
   ```
3. Navigate to **Project Settings** > **Database** > **Connection string** > **URI**.
4. Copy the connection URI:
   ```
   postgresql://postgres.[PROJECT_REF]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres
   ```

### Step 2: Backend API (Render / Railway)
1. Create a **Web Service** on [render.com](https://render.com) or [railway.app](https://railway.app) connected to your GitHub repository.
2. Configure service settings:
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Configure Environment Variables:
   | Variable | Value / Example | Notes |
   |---|---|---|
   | `DATABASE_URL` | `postgresql+psycopg://postgres...` | Replace `postgresql://` with `postgresql+psycopg://` if needed |
   | `SECRET_KEY` | *(Generate a 64-char random hex string)* | `python -c "import secrets; print(secrets.token_hex(32))"` |
   | `GROQ_API_KEY` | `gsk_...` | Free API key from [console.groq.com](https://console.groq.com) |
   | `CORS_ORIGINS` | `https://pashu-sentinel.vercel.app` | Comma-separated list of allowed frontend origins |
4. Deploy service. On startup, Alembic migrations run automatically, tables are provisioned, demo villages are seeded, and the RAG vector store initializes.

### Step 3: Frontend PWA (Vercel)
1. Import the repository at [vercel.com](https://vercel.com).
2. Configure project settings:
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
3. Add Environment Variable:
   - `VITE_API_URL`: URL of your deployed backend (e.g., `https://pashu-backend.onrender.com`).
4. Click **Deploy**. Vercel will build the React 19 PWA, register the Workbox service worker, and publish the application with automatic edge SSL.

---

## Strategy B: Single-Server Docker Compose Deployment

Deploy the complete stack (PostGIS + FastAPI + Nginx PWA) on an Ubuntu/Debian VPS (AWS EC2, DigitalOcean Droplet, Hetzner, or GCP Compute Engine).

### Prerequisites
- Docker Engine 24.0+ and Docker Compose v2.20+
- Inbound firewall access on ports 80, 443, and 8000 (optional for internal API)

### Step 1: Clone & Configure
```bash
git clone https://github.com/akt1410/PashuSentinel.git
cd PashuSentinel
```

Create `.env.prod`:
```bash
POSTGRES_DB=pashu_sentinel
POSTGRES_USER=pashu
POSTGRES_PASSWORD=pashu_strong_production_password_2026
SECRET_KEY=9b7f92e0cbfae4210b37dc18d6a858e7c10b40a32e1858a8a47bfb3cb4ee08e6
GROQ_API_KEY=gsk_your_groq_api_key_here
CORS_ORIGINS=http://localhost,http://your-server-ip,https://pashusentinel.gov.in
VITE_API_URL=http://localhost:8000
```

### Step 2: Build & Launch
```bash
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d --build
```

### Step 3: Verify Container Health
```bash
docker compose -f docker-compose.prod.yml ps
```
All 3 containers (`pashu_prod_postgis`, `pashu_prod_backend`, `pashu_prod_frontend`) should report `healthy` or `running`.

Check backend health check endpoint:
```bash
curl http://localhost:8000/health
```
Expected response:
```json
{
  "status": "ok",
  "service": "pashu-sentinel-api",
  "version": "2.0.0",
  "database": "postgresql",
  "ml_engine": {
    "isolation_forest": true,
    "ewma_farrington": true
  }
}
```

---

## Production Security & Best Practices

1. **Non-Root Execution**: The backend container runs under `appuser` (UID 1000) with restricted system privileges.
2. **Reverse Proxy SSL Termination**: When hosting publicly, place Cloudflare or Caddy in front of Nginx:
   ```caddy
   pashusentinel.gov.in {
       reverse_proxy localhost:80
   }
   api.pashusentinel.gov.in {
       reverse_proxy localhost:8000
   }
   ```
3. **Database Backups**:
   Schedule daily compressed PostGIS dumps via cron:
   ```bash
   0 3 * * * docker exec pashu_prod_postgis pg_dump -U pashu pashu_sentinel | gzip > /backups/pashu_$(date +%F).sql.gz
   ```
4. **PWA Offline Resilience**: The frontend automatically caches static assets, Leaflet map tiles, and offline report mutations using IndexedDB + Dexie.js. No extra configuration required.
