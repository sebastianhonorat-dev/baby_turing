# tiny-turing: Tic-Tac-Toe & 8-Puzzle Solver

This project is a web-based playground designed to showcase classic Artificial Intelligence (AI) search algorithms. It features an automated **Tic-Tac-Toe game** using adversarial search and an **8-Puzzle Solver** using state-space graph search.

The application is built using a **Flask** backend (Python) and a minimalist, custom-styled frontend (HTML/CSS/JavaScript).

---

## 🚀 Features

### 1. Tic-Tac-Toe AI
* **Adversarial Algorithms:** Switch dynamically between standard **Minimax** and **Alpha-Beta Pruning** to watch how significantly the explored nodes drop.
* **Contrasting Image Sets:** Rather than using basic "X" and "O" text, players compete using contrasting image segments.
* **Visual Takeover:** When a player wins, their image seamlessly floods the entire borderless grid.
* **Shuffled Themes:** The game randomly selects one of 3 image sets (`set_1`, `set_2`, `set_3`) every time you reset.
* **Automation:** The AI detects when it's its turn and automatically executes its moves without requiring you to click a button.

### 2. 8-Puzzle Solver
* **Graph Search Algorithms:** Solves randomized 8-puzzle boards using **Breadth-First Search (BFS)** or **Dijkstra's Algorithm**.
* **Dynamic Path Animation:** The backend calculates the full path of states, and the frontend steps through the tiles visually so you can watch it solve itself.
* **Custom Image Upload:** Upload any personal picture, and the web canvas will mathematically slice it into a flush 3x3 sliding tile grid.

---

## 📂 Project Architecture

Here is how your codebase is organized:

```text
├── app.py              # Main Flask server (handles routing, endpoints, and coordination)
├── ttt.py              # Tic-Tac-Toe rules, game logic, and Minimax AI engine
├── puzzle_8.py         # 8-Puzzle board definitions, BFS, and Dijkstra algorithms
├── ttt_images/         # Images accessed by the game
│   ├── set_1/          #   └── contains x.png and o.png
│   ├── set_2/          #   └── contains x.png and o.png
│   └── set_3/          #   └── contains x.png and o.png
└── templates/          # Frontend layout files
    ├── index.html      # Tic-Tac-Toe user interface
    └── puzzle.html     # 8-Puzzle user interface

```

---


### Prerequisites

You will also need to install **Flask** via your terminal or command prompt.

```bash
pip install Flask

```

### Running the Application

1. Open your terminal or command line app.
2. Navigate (`cd`) into the directory where this project folder is saved.
3. Execute the `app.py` script:

```bash
python app.py

```

4. You will see an output in your terminal saying something like:
`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`
5. Open your preferred web browser and type **`http://127.0.0.1:5000/`** into the URL bar.

---

## 👥 AI Devs

* *Nicholas Choi*
* *Sebastian Honorat*

```

```