"""
Classes and functions to set up a tile grid and entities.
"""

import random
from typing import Dict, List


class Tile:
    """
    A class representing a tile.

    Attributes:
        symbol (str): Single-character symbol representing the tile.
        traversable (bool): Can entities travel on this tile?
    """

    def __init__(self, symbol: str, traversable: bool) -> None:
        """
        Initialise a Tile object.

        Parameters:
            symbol (str): Single-character symbol representing the tile.
            traversable (bool): Can entities travel on this tile?
        """
        self.symbol = symbol
        self.traversable = traversable


def is_traversable(symbol: str, blocking_symbols: List[str] = ["#"]) -> bool:
    """
    Decide if a tile can be travelled on by an entity.

    Parameters:
        symbol (str): Single-character symbol representing the tile.
        blocking_symbols (List[str]): Single-character representations of tiles that can't be traversed by an entity.

    Returns:
        bool: Can entities travel on this tile?
    """
    if symbol in blocking_symbols:
        return False
    else:
        return True


class Entity:
    """
    A class representing an entity.

    Attributes:
        symbol (str): Single-character symbol representing the tile.
        row (int): The row of the tile grid that the entity is on.
        col (int): The column of the tile grid that the entity is on.
        hp (int): Hit points of the entity.
    """

    def __init__(self, symbol: str, row: int, col: int, hp: int = 1) -> None:
        """
        Initialise an Entity object.

        Parameters:
            symbol (str): Single-character symbol representing the tile.
            row (int): The row of the tile grid that the entity is on.
            col (int): The column of the tile grid that the entity is on.
            hp (int): Hit points of the entity.
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.hp = hp


def create_grid(
    n_rows: int, n_cols: int, n_walls: int, tileset: Dict[str, str], player: Entity
) -> List[List[Tile]]:
    """
    Create a grid of tiles.

    Parameters:
        n_rows (int): The number of rows for the tile grid.
        n_cols (int): The number of columns for the tile grid.
        n_walls (int): The number of impassable wall tiles to spawn.
        tileset (Dict[str, str]): Single-character symbols representing named tiles types.
        player (Entity): Instance of an Entity class representing the player.

    Returns:
        List[List[Tile]: A list with n_rows lists, each containing n_rows tiles.
    """
    grid = [
        [Tile(tileset["floor"], True) for _ in range(n_cols)] for _ in range(n_rows)
    ]

    possible_wall_positions = [
        (row, col) for row in range(n_rows) for col in range(n_cols)
    ]
    player_position = (player.row, player.col)
    possible_wall_positions.remove(player_position)  # don't spawn on player tile

    for row, col in random.sample(possible_wall_positions, n_walls):
        grid[row][col] = Tile(tileset["wall"], False)

    return grid


class TileGrid:
    """
    A class representing a grid of tiles.

    Attributes:
        n_rows (int): The number of rows for the tile grid.
        n_cols (int): The number of columns for the tile grid.
        n_walls (int): The number of impassable wall tiles to spawn.
        tileset (Dict[str, str]): Single-character symbols representing named tiles types.
        player (Entity): Instance of an Entity class representing the player.
        fog (int): Tile-distance to draw fog of war. Defaults to 2.
    """

    def __init__(
        self,
        n_rows: int,
        n_cols: int,
        n_walls: int,
        tileset: Dict[str, str],
        player: Entity,
        fog: int,
    ) -> None:
        """
        Initialise a TileGrid object.

        Parameters:
            n_rows (int): The number of rows for the tile grid.
            n_cols (int): The number of columns for the tile grid.
            n_walls (int): The number of impassable wall tiles to spawn.
            tileset (Dict[str, str]): Single-character symbols representing named tiles types.
            player (Entity): Instance of an Entity class representing the player.
            tiles (List[List[Tile]]): A list with n_rows lists, each containing n_rows tiles.
            fog (int): Tile-distance to draw fog of war. Defaults to 2.
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_walls = n_walls
        self.player = player
        self.tileset = tileset
        self.tiles = create_grid(n_rows, n_cols, n_walls, tileset, player)
        self.fog = fog
        self.direction = "right"

    def draw(self) -> None:
        """
        Print the tile grid.

        Returns:
            None: Prints the tile grid.
        """

        # ANSI colour codes for symbols
        YELLOW = "\033[93m"
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREY = "\033[90m"
        RESET = "\033[0m"  # reset codes after use (colour-symbol-reset)

        symbol_colours = {"@": YELLOW, ".": BLACK, "#": RED, "?": GREY}

        for row in range(self.n_rows):
            row_symbols = []
            for col in range(self.n_cols):
                if self.player.row == row and self.player.col == col:
                    symbol = self.player.symbol
                elif max(
                    abs(self.player.row - row), abs(self.player.col - col)
                ) in range(1, self.fog + 1):
                    symbol = self.tiles[row][col].symbol
                else:
                    symbol = "?"

                colour = symbol_colours[symbol]
                row_symbols.append(f"{colour}{symbol}{RESET} ")  # breathing space

            print("".join(row_symbols))

    def move_player(self, player: Entity, row_change: int, col_change: int) -> bool:
        """
        Move the player entity around the grid, given user input.

        Parameters:
            player (Entity): Instance of an Entity class representing the player.
            row_change (int): Count of tiles to move the player right (positive value) or left (negative value).
            col_change (int): Count of tiles to move the player down (positive value) or up (negative value).

        Returns:
            bool: True if the player can be moved, False if not.
        """
        new_row = player.row + row_change
        new_col = player.col + col_change

        # Check boundary, don't travel beyond the grid
        if not (0 <= new_row < self.n_rows and 0 <= new_col < self.n_cols):
            return False

        # Check terrain, don't travel on non-traversable tiles
        if not self.tiles[new_row][new_col].traversable:
            return False

        # Change player's row and column properties
        player.row = new_row
        player.col = new_col

        return True

    def process_input(self) -> bool | None:
        """
        Accept user input and process it.
        """

        moves = {
            "w": "up",
            "s": "down",
            "a": "left",
            "d": "right",
        }

        direction_changes = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }

        while True:
            move = input("Move [wasd], [b]reak, [p]lace, [q]uit: ").lower()

            if move == "q":
                break

            if move in ["b", "p"]:
                row_change, col_change = direction_changes[self.direction]
                target_row = self.player.row + row_change
                target_col = self.player.col + col_change

                if not (
                    0 <= target_row < self.n_rows and 0 <= target_col < self.n_cols
                ):
                    return True

                target_tile = self.tiles[target_row][target_col]

                if move == "b":
                    if target_tile.symbol == self.tileset["wall"]:
                        self.tiles[target_row][target_col] = Tile(
                            self.tileset["floor"], True
                        )

                if move == "p":
                    if target_tile.symbol == self.tileset["floor"]:
                        self.tiles[target_row][target_col] = Tile(
                            self.tileset["wall"], False
                        )

                return True

            if move in moves:
                self.direction = moves[move]

                row_change, col_change = direction_changes[self.direction]
                self.move_player(self.player, row_change, col_change)

                return True

            print("Input not recognised. Try again.")
