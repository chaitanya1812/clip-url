FROM python:3.11-slim

WORKDIR /clip-url
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV DATABASE_URL=postgresql://chaitanya:chaitanya123@host.docker.internal:5432/clipurl
ENV BASE_URL=localhost:8300

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8500"]
