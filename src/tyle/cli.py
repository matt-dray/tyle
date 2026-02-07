"""
Entry point to the CLI with argument parser.
"""

import argparse
from .tiles import Entity, TileGrid
from importlib.metadata import version
import os


def bounded_int(value: str) -> int:
    """
    Check values are within a specific range.

    Arguments:
        value (str): The value to check from CLI input.

    Returns:
        int: The value entered, otherwise an error.
    """
    int_value = int(value)
    if int_value <= 2 or int_value > 50:
        raise argparse.ArgumentTypeError("Value must be >2 and <=50")
    return int_value


def positive_int(value: str) -> int:
    """
    Check values are positive.

    Arguments:
        value (int): The value to check from CLI input.

    Returns:
        int: The value entered, otherwise an error.
    """
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError("Value must be >0")
    return int_value


def main() -> None:
    """
    CLI entry point for tyle.

    Returns:
        None: Performs action depending on user input.
    """

    parser = argparse.ArgumentParser(
        prog="tyle",
        description="A small interactive toy roguelike-like experience",
        epilog=(
            "usage:\n"
            "  * example with optional arguments: tyle -r 5 -c 30 -w 15\n"
            "  * move with W, A, S or D then Enter\n"
            "  * quit with Q then Enter\n"
            f"\nSource: https://github.com/matt-dray/tyle (v{version('tyle')})"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,  # preserve formatting
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"v{version('tyle')}"
    )
    parser.add_argument(
        "-r",
        "--rows",
        type=bounded_int,
        default=10,
        help="number of tile-grid rows (default 10)",
    )
    parser.add_argument(
        "-c",
        "--cols",
        type=bounded_int,
        default=20,
        help="number of tile-grid columns (default 20)",
    )
    parser.add_argument(
        "-w",
        "--walls",
        type=positive_int,
        default=25,
        help="number of non-traversable walls (default 25, clipped to max 25%% of tiles)",
    )
    args = parser.parse_args()

    tileset = {"floor": ".", "wall": "#", "player": "@"}

    n_rows = args.rows
    n_cols = args.cols
    n_walls = min(args.walls, max(0, n_rows * n_cols) // 4)  # ensure floorspace

    player = Entity(tileset["player"], n_rows // 2, n_cols // 2)  # middle-ish

    tile_grid = TileGrid(n_rows, n_cols, n_walls, tileset, player)

    while True:
        os.system("cls" if os.name == "nt" else "clear")  # clear screen
        tile_grid.draw()
        in_play = tile_grid.process_input()
        if not in_play:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
