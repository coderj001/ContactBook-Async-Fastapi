import uvicorn

from app.contactbook import router as contactbook
from core.application import create_api
from core.config import config
from core.database import init_models

app = create_api()

app.include_router(contactbook, prefix="/contactbook")


# @app.on_event("startup")
# async def startup():
#     """
#     Create db tables
#     """
#     await init_models()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=config.debug,
        log_level="info"
    )
