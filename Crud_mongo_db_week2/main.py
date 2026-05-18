from contextlib import asynccontextmanager

from fastapi import FastAPI

from config.db import init_db
from routers.api_routes import api_router


@asynccontextmanager
async def lifespan():
    await init_db()
    yield

app = FastAPI(
    title="User Crud API",
    lifespan=lifespan
)


app.include_router(api_router)

@app.get('/health')
async def health():
    return {'status': 'ok'}