# Deployment

## Render
1. Push this repository to GitHub.
2. Render -> New -> Blueprint.
3. Select the repository.
4. Render uses `render.yaml` and the Dockerfile.
5. Verify `/api/health`, `/api/readiness`, `/docs`, and `/`.

## Docker
`docker compose up --build`

## Production healthcare warning
This is a deployable research platform, not clinically deployable medical-device software. Do not use identifiable patient data or make clinical claims until validation, security, governance, and applicable regulatory requirements are addressed.
