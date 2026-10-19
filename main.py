from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello AI Product!"}

@app.get("/words")
def get_words():
    return {"words": ["abandon", "benefit", "crucial"]}