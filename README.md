# React + Flask + GCP

## Déploiement
```bash
gcloud builds submit --tag gcr.io/PROJECT_ID/skin-analyzer
gcloud run deploy skin-analyzer --image gcr.io/PROJECT_ID/skin-analyzer --platform managed --region europe-west1
```

## Structure
- `frontend/` : App React + Vite
- `backend/` : App Flask + TensorFlow
