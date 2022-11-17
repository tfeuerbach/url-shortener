# app/hashser.py

import secrets
import string
import hashlib
from . import db_functions, models, schemas
from sqlalchemy.orm import Session

def create_hash(length: int = 5) -> str:
    key = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(key) for _ in range(length))

def create_hash_2():
    key = hashlib.md5(models.target_url.encode("utf-8")).hexdigest()
    return "".join(secrets.choice(key) for _ in range(length))

def create_unique_hash(db: Session) -> str:
    key = create_hash()
    while db_functions.get_db_url_by_key(db, key):
        key = create_hash()
    return key

def create_unique_hash_2(db: Session) -> str:
    key = create_hash_2()
    while db_functions.get_db_url_by_key(db, key):
        key = create_hash_2()
    return key

