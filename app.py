import os
import tempfile
from pathlib import Path
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from markitdown import MarkItDown

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)
EXPECTED = os.getenv("API_KEY", "")

async def check_key(x_api_key: str | None = Depends(API_KEY_HEADER)):
    if not EXPECTED or x_api_key != EXPECTED:
        raise HTTPException(
            status_code=401, detail="Invalid or missing API key")

api = FastAPI(title="Doc2MD API")

@api.post("/convert", dependencies=[Depends(check_key)])
async def convert(file: UploadFile = File(...)):
    data = await file.read()
    ext = Path(file.filename or "document").suffix or ""
    with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
        tmp.write(data)
        tmp_path = tmp.name

    try:
        md = MarkItDown()
        out = md.convert(tmp_path)
        return {
            "filename": f"{Path(file.filename or 'document').stem}.md",
            "markdown": out.text_content
        }
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass

@api.get("/health")
def health():
    return {"status": "ok"}
