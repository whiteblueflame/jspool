from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter()


@router.get("")
def health():
    return {"status": "ok", "service": "jspool-api"}


@router.get("/db")
def health_db(db: Session = Depends(get_db)):
    db.scalar(text("SELECT 1"))
    return {"status": "ok", "database": True}
