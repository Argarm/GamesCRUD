import sqlite3
from typing import Dict, Any, Optional
from Api.Model.Format import Format
from Api.Model.Game import Game
from Api.Model.PlatformChoice import PlatformChoice
from Api.Model.Status import Status


class SQLiteGameRepository:
    def __init__(self, connection:  sqlite3.connect):
        self.connection = connection
        self.connection.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            developer TEXT NOT NULL,
            release_date TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            format TEXT NOT NULL,
            my_time INTEGER NOT NULL,
            platform TEXT NOT NULL,
            status TEXT NOT NULL
        )
        ''')
        self.connection.commit()

    def _game_to_dict(self, game: Game) -> Dict[str, Any]:
        return {
            "name": game.name,
            "developer": game.developer,
            "release_date": game.release_date,
            "completed": 1 if game.completed else 0,
            "format": game.format.value,
            "my_time": game.my_time,
            "platform": game.platform.value,
            "status": game.status.value
        }

    def row_to_game(self, row) -> Game:
        return Game(
            name=row["name"],
            developer=row["developer"],
            release_date=row["release_date"],
            completed=bool(row["completed"]),
            format=Format(row["format"]),
            my_time=row["my_time"],
            platform=PlatformChoice(row["platform"]),
            status=Status(row["status"])
        )

    def get_by_id(self, game_id: int) -> Optional[Game]:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM games WHERE id = ?", (game_id,))
        row = cursor.fetchone()
        if row:
            return self.row_to_game(row)
        return None

    def create(self, game: Game) -> str:
        cursor = self.connection.cursor()
        game_dict = self._game_to_dict(game)
        columns = ", ".join(game_dict.keys())
        placeholders = ", ".join(["?"] * len(game_dict))
        cursor.execute(
            f"INSERT INTO games ({columns}) VALUES ({placeholders})",
            tuple(game_dict.values())
        )
        self.connection.commit()
        return cursor.lastrowid

    def close(self):
        if self.connection:
            self.connection.close()