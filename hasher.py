# app/hashser.py

import secrets
import string
from . import db_functions 
from sqlalchemy.orm import Session

def create_hash(length: int = 5) -> str:
    key = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(key) for _ in range(length))

def create_unique_hash(db: Session) -> str:
    key = create_hash()
    while db_functions.get_db_url_by_key(db, key):
        key = create_hash()
    return key
