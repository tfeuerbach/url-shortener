# app/main.py

import validators
import secrets

from configparser import ConfigParser
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import schemas, models
from .database import SessionLocal, engine

# Reading api_config.ini file
config_object = ConfigParser()
config_object.read("/home/ubuntu/urlshortener/app/api_config.ini")

# Extract API Details
api_config = config_object["APICONFIG"]

# API Tags
tags_metadata = [
        {
            "name": "shortener",
            "description": "Endpoint for interacting with and shortening URLs",
            },
        ]

# Initialize the API
app = FastAPI(title="URL Shortener",
              description=api_config["description"],
              version=api_config["version"],
              contact={
                  "name": api_config["name"],
                  "url": api_config["url"],
              },
              license_info={
                  "name": api_config["license_name"],
                  "url": api_config["license_url"],
              },
              openapi_tags=tags_metadata,
             )
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)

@app.get("/")
def read_root():
    return "Welcome to the URL shortener API :)"

@app.post("/url", response_model=schemas.URLInfo, tags=["shortener"])
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
   
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url

@app.get("/{url_key}", tags=["shortener"])
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)

app.mount("/home", StaticFiles(directory="/home/ubuntu/urlshortener/app/ui", html=True), name="ui")
