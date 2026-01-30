# tyle

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

A Python CLI with a small interactive toy roguelike-like experience.

Just a concept for now.
May be developed in future.

Install with [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uv tool install git+https://github.com/matt-dray/tyle
```

Or, to develop the tool, clone and install in editable mode:

```bash
uv pip install -e .
```

Then, from a terminal:

```bash
tyle
```

To get a randomised tile grid like this:

```txt
.......#..
..........
.##..#....
....#....#
.....#....
.....@....
..#.......
........#.
..........
....#.....
Move (WASD+Enter): 
```

You control `@`. Floor tiles (`.`) are traversable but walls (`#`) aren't.

Type:

* e.g. <kbd>W</kbd> and <kbd>Enter</kbd> to move up.
* <kbd>Q</kbd> and <kbd>Enter</kbd> to quit.
