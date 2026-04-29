# Dead Defenders

Dead Defenders is a real-time pathfinding system where an agent must navigate a grid to reach a safe zone while avoiding dynamic, moving threats ("Zombies"). Unlike static mazes, this system requires constant re-calculation to ensure survival in a changing environment.

## 🎮 Game Overview

**Dead Defenders** is a real-time, grid-based pathfinding game developed in Python using the Pygame library. The core concept involves an **AI-controlled agent** that must navigate a tile-based grid to reach a designated **safe zone (goal)**, while dynamically avoiding **zombie enemies** that move autonomously throughout the map.

Unlike traditional static maze solvers, Dead Defenders operates in a **dynamic environment**: obstacles (zombies) are in constant motion, which forces the agent's pathfinding algorithm to **recalculate its route every game tick** to respond to ever-changing threats. This makes it a practical demonstration of real-time AI pathfinding under uncertainty.

## 🌱 Inspiration

Dead Defenders is partially inspired by the classic strategy game *Plants vs. Zombies*. While the gameplay mechanics differ, the inspiration comes from the idea of **defending against unpredictable, continuously moving enemies in a grid-based environment**.

Instead of placing defensive units like plants, this project flips the perspective:

* You guide the **setup of the environment**
* While an **AI agent autonomously reacts** to threats in real time

The presence of roaming zombies, spatial constraints, and tactical positioning all echo the strategic tension found in Plants vs. Zombies—but here, the focus is on **AI decision-making and adaptive pathfinding** rather than tower defense mechanics.

## 🚀 Features

* **Real-Time Dynamic Pathfinding**: Uses a custom implementation of the A* (A-Star) search algorithm that recalculates the shortest, safest path every game frame
* **Procedurally Generated Levels**: A smart grid generator ensures every playthrough is unique while validating solvability (ensuring the goal is always reachable)
* **Dynamic AI Enemies**: Zombies move randomly and independently, constantly altering the optimal path for the agent
* **Polished UI/UX**: Includes an interactive main menu, hover effects, fade transitions, and visual indicators for the agent's planned path and visited trail

## 🛠️ Built With

* **Python 3.8+** - Core programming language
* **Pygame** - Rendering, event handling, and sprite management

## 📦 How to Run

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/bakwasbandd/DeadDefenders.git
   cd DeadDefenders
   ```

2. **(Optional) Create and activate a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\\Scripts\\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

To start the game, run the `main.py` script:

```bash
python main.py
```

## 🕹️ Controls

Once you start the game from the main menu, you will enter **Placing Mode**. Follow these controls to set up and play:

| Input            | Action                                                    |
| ---------------- | --------------------------------------------------------- |
| `S` + Left Click | Place the agent's start position on an empty tile         |
| `G` + Left Click | Place the goal (safe zone) position on an empty tile      |
| `Enter`          | Lock in positions and start the simulation                |
| `Z` + Left Click | Spawn an extra zombie during gameplay (5-second cooldown) |

## ⚙️ Game Mechanics

* **Agent**: Moves autonomously towards the goal, recalculating its path to avoid zombies
* **Zombies**: Move randomly and block the agent's path

**End Conditions:**

* If the agent reaches the goal, **YOU WIN**
* If a zombie collides with the agent, **GAME OVER**

## 🧠 Project Architecture

The project is highly modularized for clean architecture and maintainability:

* `main.py`: Entry point and main menu UI logic
* `game.py`: Core game loop, input handling, and simulation state
* `path_finding.py`: Custom A* pathfinding algorithm implementation
* `grid_generator.py`: Procedural, solvable level generation using internal path validation
* `ui_renderer.py`: Handles all Pygame drawing and rendering operations
* `about_screen.py` & `end_screen.py`: Handles the tutorial slideshow and win/loss states

## 🎯 Conclusion

Dead Defenders is more than just a game—it's a hands-on exploration of **real-time AI, adaptive decision-making, and dynamic pathfinding in unpredictable environments**.

By combining inspiration from classic games with modern algorithmic techniques, this project demonstrates how intelligent agents can operate effectively under constant change.

Whether you're studying AI, experimenting with game development, or exploring pathfinding algorithms in action, Dead Defenders provides a strong and interactive foundation to build upon.
