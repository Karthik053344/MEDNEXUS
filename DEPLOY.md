
# Deploy MEDNEXUS AI

## Fastest route: Render

The repository is already Docker-ready and includes `render.yaml`.

1. Create a GitHub repository.
2. Extract this project and push the contents to the repository root.
3. In Render, choose **New -> Blueprint** and select the repository.
4. Render will read `render.yaml`.
5. Deploy.
6. Open the generated `onrender.com` URL.

Render supports Docker-based web services and can build directly from the repository Dockerfile. The included health check uses `/api/health`.

## Alternative: Docker locally

```bash
docker compose up --build
```

Then visit:

http://localhost:8000

## Important production limitation

The included deployment is suitable for a **software demonstration/research prototype**.

Do not use it with identifiable patient/PHI data or market it as a validated diagnostic or prescribing product. Before clinical use, replace SQLite with managed PostgreSQL, implement real authentication/RBAC, secure storage, audit logging, privacy controls, validated clinical models, external validation, monitoring, and the applicable regulatory/quality processes.

## Deployment verification

After deployment, test:

- `/`
- `/api/health`
- `/api/readiness`
- `/docs`

Then submit a non-identifying demo assessment through the UI.

## Git commands

```bash
git init
git add .
git commit -m "Initial MEDNEXUS AI deployment"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY
git push -u origin main
```
