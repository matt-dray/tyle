# tyle

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)
[![Blog
posts](https://img.shields.io/badge/rostrum.blog-posts-008900?labelColor=000000&logo=data%3Aimage%2Fgif%3Bbase64%2CR0lGODlhEAAQAPEAAAAAABWCBAAAAAAAACH5BAlkAAIAIf8LTkVUU0NBUEUyLjADAQAAACwAAAAAEAAQAAAC55QkISIiEoQQQgghRBBCiCAIgiAIgiAIQiAIgSAIgiAIQiAIgRAEQiAQBAQCgUAQEAQEgYAgIAgIBAKBQBAQCAKBQEAgCAgEAoFAIAgEBAKBIBAQCAQCgUAgEAgCgUBAICAgICAgIBAgEBAgEBAgEBAgECAgICAgECAQIBAQIBAgECAgICAgICAgECAQECAQICAgICAgICAgEBAgEBAgEBAgICAgICAgECAQIBAQIBAgECAgICAgIBAgECAQECAQIBAgICAgIBAgIBAgEBAgECAgECAgICAgICAgECAgECAgQIAAAQIKAAAh%2BQQJZAACACwAAAAAEAAQAAAC55QkIiESIoQQQgghhAhCBCEIgiAIgiAIQiAIgSAIgiAIQiAIgRAEQiAQBAQCgUAQEAQEgYAgIAgIBAKBQBAQCAKBQEAgCAgEAoFAIAgEBAKBIBAQCAQCgUAgEAgCgUBAICAgICAgIBAgEBAgEBAgEBAgECAgICAgECAQIBAQIBAgECAgICAgICAgECAQECAQICAgICAgICAgEBAgEBAgEBAgICAgICAgECAQIBAQIBAgECAgICAgIBAgECAQECAQIBAgICAgIBAgIBAgEBAgECAgECAgICAgICAgECAgECAgQIAAAQIKAAA7)](https://www.rostrum.blog/index.html#category=tyle)

## About

A Python CLI with a small interactive toy roguelike-like experience.

> [!NOTE]
> This is a simple concept to help me learn Python.

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
..............#.....
.#................#.
....................
............#.......
...#..............#.
..........@.........
........#...........
.............#......
....................
..#..........#......
Move (WASD+Enter):
```

You control `@` (starting centrally-ish).
Floor tiles (`.`) are traversable but the randomly-placed walls (`#`) aren't.

Type at the prompt:

* <kbd>W</kbd>, <kbd>A</kbd>, <kbd>S</kbd> or <kbd>D</kbd> then <kbd>Enter</kbd> to move up, left, down or right
* <kbd>Q</kbd> then <kbd>Enter</kbd> to quit

You can use optional arguments to set tile-grid parameters:

```bash
tyle -r 5 -c 30 -w 15
```

Use `tyle -h` for help.

## Related

I wrote [the r.oguelike package](https://github.com/matt-dray/r.oguelike) for a toy roguelike in the R console.
You can [read some blog posts](https://www.rostrum.blog/index.html#category=r.oguelike) about it.
