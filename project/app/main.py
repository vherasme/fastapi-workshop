from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.api import router as api_router
from app.core.config import get_settings
from app.core.database import engine
from app.models import Base

app = FastAPI(title=get_settings().APP_NAME)
app.include_router(api_router)


@app.on_event("startup")
def startup_event():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
