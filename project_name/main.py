from fastapi import FastAPI

from project_name.infrastructure.adapters.api import router

app = FastAPI()
app.include_router(router)