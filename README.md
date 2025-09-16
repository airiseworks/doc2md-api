# 📄 Doc2MD API

API built with **Python (FastAPI + MarkItDown)** to convert documents (DOCX, PDF, PPTX, images, etc.) into **Markdown**.
Includes **API Key authentication** and is configured to run in **Docker/Coolify**, with a built-in **healthcheck**.

---

## ✨ Features

* Convert common document formats to Markdown (`.docx`, `.pdf`, `.pptx`, `.xlsx`, `.html`, images, etc.).
* Secure file upload via `multipart/form-data`.
* **API Key** protection (via `X-API-Key` header).
* `/health` endpoint for monitoring.
* Ready for Docker and DevContainer environments.

---

## 🚀 Running Locally

### Requirements

* [Python 3.12+](https://www.python.org/)
* [Docker](https://www.docker.com/)

### Local setup

```bash
pip install -r requirements.txt
uvicorn app:api --reload
```

Access the API at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Running with Docker

### Build

```bash
docker build -t doc2md-api .
```

### Run

```bash
docker run -e API_KEY=supersecret -p 8000:8000 doc2md-api
```

---

## 🔑 Authentication

All requests must include the header:

```http
X-API-Key: supersecret
```

Set your API key via the `API_KEY` environment variable.

---

## 📡 Endpoints

### Healthcheck

```http
GET /health
```

Response:

```json
{ "status": "ok" }
```

### Convert document

```http
POST /convert
```

**Headers:**

```
X-API-Key: supersecret
```

**Body (form-data):**

* `file`: document file (`.docx`, `.pdf`, etc.)

**Example using `curl`:**

```bash
curl -H "X-API-Key: supersecret" \
     -F "file=@mydocument.docx" \
     http://localhost:8000/convert
```

Response:

```json
{
  "filename": "mydocument.md",
  "markdown": "# Title\n\nConverted content in Markdown..."
}
```

---

## 🛠 DevContainer

The project includes **VS Code DevContainer** support.
Open it in VS Code and select **“Reopen in Container”** to start with a fully prepared development environment.

---

## 📜 License

MIT – you are free to use, modify, and contribute.

---
💰 Donations

This initiative is open-source and free to use.
If you find it valuable and would like to contribute, you can make a donation as a way to support the continuation of this work.

[PayPal](https://www.paypal.com/donate/?business=KYF6D3FF3MTHA&no_recurring=0&item_name=This+project+is+developed+an+open-source+initiative+to+provide+a+simple+and+secure+API+for+converting+documents+into+Markdown.&currency_code=USD)

---

Project powered by [FastAPI](https://fastapi.tiangolo.com/) and [MarkItDown](https://github.com/microsoft/markitdown).
