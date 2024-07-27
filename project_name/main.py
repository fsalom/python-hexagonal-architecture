from fastapi import FastAPI

from project_name.driving.api.user.user_api_adapter import router

app = FastAPI()
app.include_router(router)
