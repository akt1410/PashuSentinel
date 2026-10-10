# syntax=docker/dockerfile:1
# Pashu Sentinel - Production Frontend Dockerfile
# Multi-stage build: Vite build -> Nginx Alpine static serving

# ── 1. Build Stage ─────────────────────────────────────────────────────────────
FROM node:22-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .

ARG VITE_API_URL=""
ENV VITE_API_URL=${VITE_API_URL}

RUN npm run build

# ── 2. Production Web Server ──────────────────────────────────────────────────
FROM nginx:alpine AS runner

COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD wget -q --spider http://localhost:80/health || exit 1

CMD ["nginx", "-g", "daemon off;"]
