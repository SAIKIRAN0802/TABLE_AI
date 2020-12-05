import logging
import os
import shutil
import uuid
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import UploadFile, File, Form

router = APIRouter()

@router.post("/file-upload")
def UPLOAD_FILE(
    file: UploadFile = File(...)
):
    pass
@router.post("/ask-question")
def ASK_QUESTION(
    file: UploadFile = File(...)
):
    pass