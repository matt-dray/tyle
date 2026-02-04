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


def create_grid(
    n_rows: int, n_cols: int, n_walls: int, tileset: Dict[str, str]
) -> List[List[Tile]]:
    """
    Create a grid of tiles.

    Parameters:
        n_rows (int): The number of rows for the tile grid.
        n_cols (int): The number of columns for the tile grid.
        n_walls (int): The number of impassable wall tiles to spawn.
        tileset (Dict[str, str]): Single-character symbols representing named tiles types.

    Returns:
        List[List[Tile]: A list with n_rows lists, each containing n_rows tiles.
    """
    grid = [
        [Tile(tileset["floor"], True) for _ in range(n_cols)] for _ in range(n_rows)
    ]

    wall_positions = [(row, col) for row in range(n_rows) for col in range(n_cols)]

    for row, col in random.sample(wall_positions, min(n_walls, len(wall_positions))):
        grid[row][col] = Tile(tileset["wall"], False)

    return grid


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


class TileGrid:
    """
    A class representing a grid of tiles.

    Attributes:
        n_rows (int): The number of rows for the tile grid.
        n_cols (int): The number of columns for the tile grid.
        n_walls (int): The number of impassable wall tiles to spawn.
        tileset (Dict[str, str]): Single-character symbols representing named tiles types.
        player (Entity): Instance of an Entity class representing the player.
    """

    def __init__(
        self,
        n_rows: int,
        n_cols: int,
        n_walls: int,
        tileset: Dict[str, str],
        player: Entity,
    ) -> None:
        """
        Initialise a TileGrid object.

        Parameters:
            n_rows (int): The number of rows for the tile grid.
            n_cols (int): The number of columns for the tile grid.
            n_walls (int): The number of impassable wall tiles to spawn.
            player (Entity): Instance of an Entity class representing the player.
            tiles (List[List[Tile]]): A list with n_rows lists, each containing n_rows tiles.
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.n_walls = n_walls
        self.player = player
        self.tiles = create_grid(n_rows, n_cols, n_walls, tileset)

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
        RESET = "\033[0m" # reset codes after use (colour-symbol-reset)

        symbol_colours = {
            "@": YELLOW,
            ".": BLACK,
            "#": RED,
        }

        for row in range(self.n_rows):
            row_symbols = []
            for col in range(self.n_cols):
                if self.player.row == row and self.player.col == col:
                    symbol = self.player.symbol
                else:
                    symbol = self.tiles[row][col].symbol

                colour = symbol_colours[symbol]
                row_symbols.append(f"{colour}{symbol}{RESET} ")  # breathing space

            print("".join(row_symbols))

    def move_player(self, player: Entity, row_change: int, col_change: int) -> bool:
        """
        Move the player entity around the grid, given user input.

        Parameters:
            player (Entity): Instance of an Entity class representing the player.
            row_change (int): Count of tiles to move the player right (positive value) or left (negative value).
            col_change (int):Count of tiles to move the player down (positive value) or up (negative value).

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

        Returns:
            bool: True if the inputs is accepted and the player has been moved, False if the user quits.
        """
        while True:
            move = input("Move (WASD+Enter): ").lower()

            if move == "q":
                break

            directions = {
                "w": (-1, 0),  # (row change, column change)
                "s": (1, 0),
                "a": (0, -1),
                "d": (0, 1),
            }

            if move in directions:
                row_change, col_change = directions[move]
                self.move_player(self.player, row_change, col_change)
                return True

            print("Input not recognised. Try again.")
