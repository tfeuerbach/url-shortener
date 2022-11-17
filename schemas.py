# app/schemas.py

from datetime import datetime
from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    clicks: int
    timestamp: datetime

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str
