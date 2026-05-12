from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "index.html"


@app.get("/")
async def read_index():
    return FileResponse(INDEX_PATH)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8080)