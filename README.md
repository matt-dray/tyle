# tyle

[![Project Status: Concept – Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.](https://www.repostatus.org/badges/latest/concept.svg)](https://www.repostatus.org/#concept)
[![Code quality](https://github.com/matt-dray/tyle/actions/workflows/code-quality.yml/badge.svg)](https://github.com/matt-dray/tyle/actions/workflows/code-quality.yml)
[![Blog
posts](https://img.shields.io/badge/rostrum.blog-posts-008900?labelColor=000000&logo=data%3Aimage%2Fgif%3Bbase64%2CR0lGODlhEAAQAPEAAAAAABWCBAAAAAAAACH5BAlkAAIAIf8LTkVUU0NBUEUyLjADAQAAACwAAAAAEAAQAAAC55QkISIiEoQQQgghRBBCiCAIgiAIgiAIQiAIgSAIgiAIQiAIgRAEQiAQBAQCgUAQEAQEgYAgIAgIBAKBQBAQCAKBQEAgCAgEAoFAIAgEBAKBIBAQCAQCgUAgEAgCgUBAICAgICAgIBAgEBAgEBAgEBAgECAgICAgECAQIBAQIBAgECAgICAgICAgECAQECAQICAgICAgICAgEBAgEBAgEBAgICAgICAgECAQIBAQIBAgECAgICAgIBAgECAQECAQIBAgICAgIBAgIBAgEBAgECAgECAgICAgICAgECAgECAgQIAAAQIKAAAh%2BQQJZAACACwAAAAAEAAQAAAC55QkIiESIoQQQgghhAhCBCEIgiAIgiAIQiAIgSAIgiAIQiAIgRAEQiAQBAQCgUAQEAQEgYAgIAgIBAKBQBAQCAKBQEAgCAgEAoFAIAgEBAKBIBAQCAQCgUAgEAgCgUBAICAgICAgIBAgEBAgEBAgEBAgECAgICAgECAQIBAQIBAgECAgICAgICAgECAQECAQICAgICAgICAgEBAgEBAgEBAgICAgICAgECAQIBAQIBAgECAgICAgIBAgECAQECAQIBAgICAgIBAgIBAgEBAgECAgECAgICAgICAgECAgECAgQIAAAQIKAAA7)](https://www.rostrum.blog/index.html#category=tyle)

## About

A Python CLI with a small interactive toy [roguelike](https://en.wikipedia.org/wiki/Roguelike)-like experience.

> [!NOTE]
> This is a simple concept to help me learn Python. No guarantees whatsoever.

## Install

Install with [uv](https://docs.astral.sh/uv/getting-started/installation/), for example:

```bash
uv tool install git+https://github.com/matt-dray/tyle
```

## Play

From a terminal:

```bash
tyle
```

The terminal will clear and a tile grid will appear.
It'll be in colour if your terminal supports [ANSI colour codes](https://en.wikipedia.org/wiki/ANSI_escape_code).

```
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? . . . . # ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? . . . . . ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? . . @ . . ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? . . . . . ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? . . . # . ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? 
Facing: right
Move [wasd], [b]reak, [p]lace, [q]uit: 
```

You control the player character: `@` (starting centrally-ish).
Floor tiles (`.`) are traversable but the randomly-placed walls (`#`) aren't.
You can break and place wall tiles.
You can't see beyond two tiles in any direction because of the [fog of war](https://en.wikipedia.org/wiki/Fog_of_war#In_video_games).

Type at the prompt (followed by <kbd>Enter</kbd>):

* <kbd>w</kbd>, <kbd>a</kbd>, <kbd>s</kbd> or <kbd>d</kbd>  to move up, left, down or right
* <kbd>b</kbd> to break a wall
* <kbd>p</kbd> to place a wall
* <kbd>q</kbd> to quit

You can use optional arguments to set tile-grid parameters when you start a new game:

```bash
tyle -r 5 -c 30 -w 15 -f 3
```

Use `tyle -h` for help with the available options.

## Related

You can [read blogposts](https://www.rostrum.blog/index.html#category=tyle) about the development of this tool, or [read about](https://www.rostrum.blog/index.html#category=r.oguelike) my toy [r.oguelike package](https://github.com/matt-dray/r.oguelike) for R.
