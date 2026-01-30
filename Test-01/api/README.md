# RBC App Monitoring API

## Architecture Overview

```
Client → FastAPI (api/) → Service Layer → Elasticsearch
```

- **Routes**: HTTP endpoints (api/routes/)
- **Services**: Business logic (api/services/)
- **Core**: Config, logging, error handling (api/core/)
- **Schemas**: Pydantic models (api/schemas/)
- **Dependencies**: DI for Elasticsearch (api/dependencies/)

---

## Features
- Ingest service health status via REST
- Query latest status for app or individual service
- Production-ready error handling and logging
- Auto-creates ES index with correct mapping
- Docker and docker-compose support

---

## Folder Structure

```
api/
  core/
  dependencies/
  routes/
  schemas/
  services/
  tests/
  main.py
  requirements.txt
```

---

## Endpoints

### POST `/add`
- Ingest a new service status document.
- **Body:**
  ```json
  {
    "application_name": "rbcapp1",
    "service_name": "httpd",
    "service_status": "UP",
    "host_name": "host1",
    "timestamp": "2026-01-30T10:30:00Z"
  }
  ```
- **Response:** `{ "message": "Document indexed successfully" }`

### GET `/healthcheck`
- Returns overall application health (UP/DOWN).
- **Response:**
  ```json
  {
    "success": true,
    "message": "Application is UP",
    "data": { "application_status": "UP" }
  }
  ```

### GET `/healthcheck/{service_name}`
- Returns latest status for a specific service.
- **Response:**
  ```json
  {
    "success": true,
    "message": "Service status retrieved",
    "data": { "service_name": "httpd", "status": "UP" }
  }
  ```
- **404 Example:**
  ```json
  {
    "success": false,
    "message": "Service 'httpd' not found",
    "data": null
  }
  ```

---

## Running Locally

### 1. Prerequisites
- Python 3.10+
- Docker (for ES/Kibana)

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Start Elasticsearch (Docker recommended)
```
docker-compose up -d elasticsearch kibana
```

### 4. Run the API
```
uvicorn main:app --reload
```

Or with Docker Compose (recommended):
```
docker-compose up --build
```

---

## Elasticsearch Index Mapping
- Auto-created on startup with correct types (keyword/date).
- See `ElasticService.create_index_if_not_exists()` for mapping logic.

---

## Error Handling
- All errors return structured JSON.
- See `core/error_handler.py` for details.

---

## Example curl Commands

Add status:
```
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"application_name":"rbcapp1","service_name":"httpd","service_status":"UP","host_name":"host1","timestamp":"2026-01-30T10:30:00Z"}'
```

Get app health:
```
curl http://localhost:8000/healthcheck
```

Get service health:
```
curl http://localhost:8000/healthcheck/httpd
```

---

## Testing

```
pytest tests/
```