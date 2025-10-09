from fastapi import FastAPI

app = FastAPI()


@app.get("/_health")
def health():
    return "OK"
