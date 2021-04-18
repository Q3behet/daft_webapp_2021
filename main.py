from fastapi import FastAPI, Request, Response, status

app = FastAPI()
app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get("/counter")
def counter():
    app.counter = app.counter + 1
    return app.counter
