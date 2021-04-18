from fastapi import FastAPI, Request, Response, status, HTTPException
from typing import Optional
import hashlib

app = FastAPI()
app.counter = 0


@app.get("/counter")
def counter():
    app.counter = app.counter + 1
    return app.counter


# 1.1
@app.get("/")
def root():
    return {"message": "Hello world!"}


# 1.2
@app.get("/method")
def method_get():
    return {"method": "GET"}


@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}


@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}


@app.put("/method")
def method_put():
    return {"method": "PUT"}


@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}


# 1.3
@app.get("/auth", status_code=204)
def check_password(password: Optional[str] = None, password_hash: Optional[str] = None):
    if password_hash != hashlib.sha512(str(password).encode("utf-8")).hexdigest() or not password or not password_hash:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
