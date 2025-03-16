import unittest
import sqlite3
from Api.Model.Game import Game
from Api.Model.Format import Format
from Api.Model.PlatformChoice import PlatformChoice
from Api.Model.Status import Status
from Core.CreateGame.CreateGameCommandHandler import CreateGameCommandHandler, CreateGameCommand
from Core.GameRepository import SQLiteGameRepository

class CreateGameCommandShould(unittest.TestCase):

    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repository = SQLiteGameRepository(self.connection)
        self.handler = CreateGameCommandHandler(self.repository)

    def tearDown(self):
        self.repository.close()
        self.connection.close()

    def test_call_repository_to_store_value(self):
        a_game = Game(
            name="aGame",
            developer="aDeveloper",
            release_date="2015-05-19",
            completed=False,
            format=Format.DIGITAL,
            my_time=0,
            platform=PlatformChoice.PC,
            status=Status.NOT_STARTED
        )
        request = CreateGameCommand(game=a_game)

        game_id = self.handler.execute(request)

        self.assertIsNotNone(game_id)
        game = self._getGameBy(game_id)
        self.assertIsNotNone(game)
        self.assertEqual(game.name, a_game.name)
        self.assertEqual(game.developer, a_game.developer)
        self.assertEqual(game.release_date, a_game.release_date)
        self.assertEqual(game.completed, a_game.completed)
        self.assertEqual(game.format, a_game.format)
        self.assertEqual(game.my_time, a_game.my_time)
        self.assertEqual(game.platform, a_game.platform)
        self.assertEqual(game.status, a_game.status)

    def _getGameBy(self, game_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM games WHERE id = ?", (game_id,))
        row = cursor.fetchone()
        return self.repository.row_to_game(row) if row else None


if __name__ == "__main__":
    unittest.main()
