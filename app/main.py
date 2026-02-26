from fastapi import FastAPI

from app.routers import chat


def create_app() -> FastAPI:
    app = FastAPI(
        title="Paper AI Backend",
        description="Minimal backend for a paper-writing AI agent using Gemini and local papers folder.",
        version="0.1.0",
    )

    app.include_router(chat.router, prefix="/api")

    return app


app = create_app()


