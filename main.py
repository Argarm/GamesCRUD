from fastapi import FastAPI

app = FastAPI()
@app.get("/games")
async def root():
    return {"message": "Hello World"}


@app.get("/games/{game_id}")
async def say_hello(game_id: int ):
    return {"message": f"Hello {game_id}!"}
