"""
Entry point to the CLI.
"""

from .tiles import Entity, TileGrid
import os


def main() -> None:
    tileset = {"floor": ".", "wall": "#", "player": "@"}
    n_rows = n_cols = n_walls = 10
    player = Entity(tileset["player"], n_rows // 2, n_cols // 2)  # middle-ish
    tile_grid = TileGrid(n_rows, n_cols, n_walls, tileset, player)

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # clear screen
        tile_grid.draw()
        in_play = tile_grid.process_input()
        if not in_play:
            break


if __name__ == "__main__":
    main()
