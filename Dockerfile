FROM node:20 as frontend
WORKDIR /app
COPY frontend/ ./frontend/
RUN cd frontend && npm install && npm run build

FROM python:3.11-slim as backend
WORKDIR /app

# Empêcher TensorFlow de tenter d'utiliser le GPU
ENV CUDA_VISIBLE_DEVICES="-1"

COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ ./backend/
COPY --from=frontend /app/frontend/dist/ ./backend/static/

EXPOSE 8080
CMD ["gunicorn", "-b", ":8080", "backend.main:app"]
