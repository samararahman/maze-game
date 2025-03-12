# Samara's Maze Game

## Overview

**Samara's Maze Game** is a multi-level 2D adventure game built with Python and Pygame, where players navigate a cat through a maze filled with treasures, potions, diamonds, and doors to advance through levels. Players must avoid walls, collect items, and maintain health while racing against time.

## How to Play

- Navigate the Maze: Use arrow keys to move the cat (`P`) around the maze.
- Collect Items:
  - `*` — Coins (increase score).
  - `p` — Potion (boost health).
  - `d` — Diamond (increase score more than coins).
- Avoid Walls: `x` — Walls block movement and reduce health when hit.
- Doors: Numbered doors (`1`, `2`, `3`, `4`, `5`) help you travel between levels.
- Health & Score: Monitor health and score on the screen.
- Timer: Complete levels before time runs out.

## Controls

| Key              | Action                 |
|------------------|------------------------|
| Left Arrow       | Move left              |
| Right Arrow      | Move right             |
| Up Arrow         | Move up                |
| Down Arrow       | Move down              |

## Features

- 4 unique levels with increasing difficulty.
- Sound effects for interactions (coins, potions, doors, walls, diamonds).
- Background music throughout gameplay.
- Health system to challenge players.
- Scoring system with win condition (score 340 or above).
- Time limit for added difficulty.
- Visual health, score, timer, and level display on screen.

## Files & Assets Needed

Ensure the following image and sound files are present in the same directory as the game file:

- Images:
  - `mouse.png`
  - `cat.png`
  - `door3.jpeg`
  - `potion1.jpeg`
  - `diamond.jpeg`
- Audio:
  - `background.mp3`
  - `cash_register.wav`
  - `clapping.wav`
  - `explosion.wav`
  - `doorcreak1.wav`
  - `ding.wav`
  - `bounce.wav`

## Requirements

- Python 3.x
- Pygame

### Install Pygame:

```bash
pip install pygame