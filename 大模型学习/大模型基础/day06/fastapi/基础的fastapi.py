from fastapi import FastAPI

app = FastAPI()


@app.get("/index")
async def root():
    return {"message": "Hello World"}