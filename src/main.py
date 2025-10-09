from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator(excluded_handlers=["/_health", "/metrics"])

instrumentator.instrument(app).expose(app)


@app.get("/")
def root():
    return "Welcome to FastAPI Playground"


@app.get("/_health")
def health():
    return "OK"
