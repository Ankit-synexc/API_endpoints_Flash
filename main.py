from fastapi import FastAPI
from config.settings import settings
from routers.api_routes import router

app = FastAPI(
    title=settings.app_name,
    description="4 endpoints: Health Check · Echo · Simple Math · User CRUD",
    debug=settings.debug
)

app.include_router(router)


@app.exception_handler(404)
async def not_found_handler(request, exc):    # ← make sure both params are here
    from fastapi.responses import JSONResponse
    return JSONResponse(status_code=404, content={"error": "Endpoint not found"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)