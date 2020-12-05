  
from fastapi import APIRouter
from app.controller import search

router = APIRouter()

router.include_router(search.router, tags=["search"])