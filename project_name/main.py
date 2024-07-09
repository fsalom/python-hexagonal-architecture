from fastapi import FastAPI

from project_name.infrastructure.api.controllers import router

app = FastAPI()
app.include_router(router)