from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db

router = APIRouter(
    prefix="/question",
    tags=['For YT']
)


# @router.get("/", response_model=List[schemas.Response)
@router.get("/")
def return_question(question: schemas.Response):

    response = "No one is best"

    if question.response == "Simon":
        response = "Simon is the best"
    elif question.response == "YT":
        response = "YT is the best"

    return response