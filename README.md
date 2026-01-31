# tyle

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)

## About

A Python CLI with a small interactive toy roguelike-like experience.

> [!NOTE] 
> This is a no-dependency concept to help me learn Python.

## Install

Install with [uv](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uv tool install git+https://github.com/matt-dray/tyle
```

## Play

From a terminal:

```bash
tyle
```

The terminal will clear and a tile grid will appear.

```
.......#..
..........
.##..#....
....#....#
......#...
.....@....
..#.......
........#.
..........
....#.....
Move (WASD+Enter): 
```

You control `@`.
Floor tiles (`.`) are traversable but walls (`#`) aren't.

Type at the prompt:

* e.g. <kbd>W</kbd> and <kbd>Enter</kbd> to move up
* <kbd>Q</kbd> and <kbd>Enter</kbd> to quit

## Dev

To develop the tool, clone and install in editable mode:

```bash
git clone https://github.com/matt-dray/tyle.git
cd tyle
uv venv  # then activate the venv
uv sync
uv pip install -e .
tyle
```

## Related

I wrote [the r.oguelike package](https://github.com/matt-dray/r.oguelike) for a toy roguelike in the R console .
You can [read some blog posts](https://www.rostrum.blog/index.html#category=r.oguelike) about it.