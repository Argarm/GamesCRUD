from fastapi import FastAPI
from Model.Game import Game

app = FastAPI()

@app.get("/games/{game_id}")
async def say_hello(game_id: int)-> dict[str,str]:
    return {"message": f"Hello {game_id}!"}


@app.post("/games/{game_id}")
async def say_hello(game_id: int,  game : Game) -> dict[str,str]:
    return {"message": f"Hello World {game.name} {game.format} {game.status} {game.developer}"}

@app.put("/games/{game_id}")
async def say_hello(game_id: int,  game : Game)-> dict[str,str]:
    return {"message": "Hello World"}

@app.delete("/games/{game_id}")
async def say_hello(game_id: int)-> dict[str,str]:
    return {"message": "Hello World"}