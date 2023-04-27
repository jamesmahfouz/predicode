from fastapi import UploadFile, File, Form
from pydantic import BaseModel
import zipfile
from io import BytesIO
from typing import List


class FileRequest(BaseModel):
    data: str
    content_type: str
    name: str
    appName: str
    price: float
    ageFrom: int
    ageTo: int
    appVersion: str

    # file: UploadFile = File(...)
    # name: str = Form(...)


