from Api.Model.Game import Game
from Core.GameRepository import SQLiteGameRepository

class CreateGameCommand:
    def __init__(self, game: Game):
        self.game = game


class CreateGameCommandHandler:
    def __init__(self, repository: SQLiteGameRepository):
        self.repository = repository

    def execute(self, command: CreateGameCommand) -> str:
        game = command.game
        return self.repository.create(game)
