# app/main.py

import validators
import secrets

from starlette.datastructures import URL
from configparser import ConfigParser
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import schemas, models, db_functions
from .database import SessionLocal, engine
from .config import get_settings

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
        {
            "name": "admin info",
            "description": "Endpoint for retrieving shortened URL information.",
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
              swagger_ui_parameters={"defaultModelsExpandDepth": -1} # Hides Schema in UI
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

# Returns information about the shortened URL
def get_admin_info(db_url: models.URL) -> schemas.URLInfo:
    base_url = URL(get_settings().base_url)
    admin_endpoint = app.url_path_for("admin info", secret_key=db_url.secret_key)
    db_url.url = str(base_url. replace(path=db_url.key))
    db_url.admin_url = str(base_url.replace(path=admin_endpoint))
    return db_url

@app.post("/url", response_model=schemas.URLInfo, tags=["shortener"])
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    
    db_url = db_functions.create_db_url(db=db, url=url)
    return get_admin_info(db_url)

@app.get("/{url_key}", tags=["shortener"])
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    if db_url := db_functions.get_db_url_by_key(db=db, url_key=url_key):
        db_functions.update_clicks(db=db, db_url=db_url)
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)

@app.get("/admin/{secret_key}", response_model=schemas.URLInfo, name="admin info", tags=["admin info"])
def get_url_info(secret_key: str, request: Request, db: Session = Depends(get_db)):
    if db_url := db_functions.get_db_url_by_secret_key(db, secret_key=secret_key):
        return get_admin_info(db_url)
    else:
        raise_not_found(request)

@app.delete("/admin/{secret_key}", tags=["admin info"])
def delete_url(secret_key: str, request: Request, db: Session = Depends(get_db)):
        if db_url := db_functions.deactivate_url(db, secret_key=secret_key):
            message = f"Success! Shortened URL for '{db_url.target_url}' deleted."
            return {"detail": message}
        else:
            raise_not_found(request)


app.mount("/", StaticFiles(directory="/home/ubuntu/urlshortener/app/ui", html=True))
