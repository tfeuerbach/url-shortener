# app/db_functions.py

from sqlalchemy.orm import Session
from datetime import datetime

from . import hasher, models, schemas

# Update Database w/ URL
def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    key = hasher.create_unique_hash(db)
    secret_key = f"{key}_{hasher.create_hash(length=8)}"
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key, timestamp=datetime.now()
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def create_db_url_2(db: Session, url: schemas.URLBase) -> models.URL:
    key = hasher.create_unique_hash_2(db)
    secret_key = f"{key}_{hasher.create_hash(length=8)}"
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key, timestamp=datetime.now()
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

# Check if HASH already exists in DB
def get_db_url_by_key(db: Session, url_key: str) -> models.URL:
    return (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )

# Check if entry in DB is found w/ secret_key
def get_db_url_by_secret_key(db: Session, secret_key: str) -> models.URL:
    return(
            db.query(models.URL)
            .filter(models.URL.secret_key == secret_key, models.URL.is_active)
            .first()
    )

# Track URL Stats
def update_clicks(db: Session, db_url: schemas.URL) -> models.URL:
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)
    return db_url

# Deactivate URL in DB
def deactivate_url(db: Session, secret_key: str) -> models.URL:
    db_url = get_db_url_by_secret_key(db, secret_key)
    if db_url:
        db_url.is_active = False
        db.commit()
        db.refresh(db_url)
    return db_url
