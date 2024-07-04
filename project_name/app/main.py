from fastapi import FastAPI

from project_name.infrastructure.api.controllers.user.user_controller import router

app = FastAPI()
app.include_router(router)