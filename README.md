# Pong Game

A two-player version of the classic Pong arcade game, written in Python. Each player controls a paddle and tries to bounce the ball past the opponent. The ball speeds up as the rally goes on, and the score is tracked at the top of the screen.

![Pong gameplay demo](demo.gif)

## Features

- Two-player gameplay on one keyboard
- Ball bounces off the walls and paddles
- Scoreboard that updates when a player misses the ball
- Object-oriented design with separate classes for the ball, paddles and scoreboard

## Controls

| Player | Up | Down |
|--------|----|------|
| Left paddle | `W` | `S` |
| Right paddle | `↑` | `↓` |

## Requirements

- Python 3.8 or newer
- No extra libraries are needed. The game uses `turtle`, which ships with Python (it needs Tkinter, included in the standard Windows and macOS installers).

## Run locally

```bash
git clone https://github.com/jivasnider/Pong-game.git
cd Pong-game
python main.py
```

On macOS/Linux you may need to use `python3 main.py` instead.

## Project structure

```
Pong-game/
├── main.py         # Game setup and main loop
├── ball.py         # Ball movement, bouncing and speed
├── paddle.py       # Paddle class and movement
├── scoreboard.py   # Score display and updates
└── demo.gif        # Gameplay preview
```

## What I learned

- Object-oriented programming in Python (classes, inheritance, methods)
- Building a game loop and handling keyboard input
- Detecting collisions and handling ball physics
- Splitting a project into multiple modules
