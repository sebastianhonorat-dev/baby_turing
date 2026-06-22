import os
import base64
import time
from flask import Flask, jsonify, request, render_template, send_from_directory

from ttt import (
    set_board,
    select_cell,
    get_available_cells,
    game_over,
    choose_best_move,
    choose_best_move_ab,
    max_player,
    min_player,
)
from puzzle_8 import BFS_Shortest_Path, Dijkstra, randommizer, Start, Goal, A_Star_Search, Heuristic

app = Flask(__name__)

# ─────────────────────────────────────────────────────────────────────────────
# In-memory game state
# ─────────────────────────────────────────────────────────────────────────────
ttt_state = {
    "board":      set_board(),
    "turn":       "X",
    "status":     "playing",
    "winner":     None,
    "last_nodes": None,
    "last_time":  None,
    "move_count": 0,
}

puzzle_state = {
    "board":  list(Start),
    "result": None,
}

# ─────────────────────────────────────────────────────────────────────────────
# Image set loader
# ─────────────────────────────────────────────────────────────────────────────
IMAGES_ROOT = "ttt_images"

def find_image(folder, symbol):
    for ext in ("jpg", "jpeg", "png"):
        path = os.path.join(folder, f"{symbol}.{ext}")
        if os.path.exists(path):
            return path
    return None

def load_image_sets():
    sets = {}
    if not os.path.isdir(IMAGES_ROOT):
        return sets
    for folder in sorted(os.listdir(IMAGES_ROOT)):
        full = os.path.join(IMAGES_ROOT, folder)
        if not os.path.isdir(full):
            continue
        x = find_image(full, "x")
        o = find_image(full, "o")
        if x and o:
            sets[folder] = {"x": x, "o": o}
    return sets

IMAGE_SETS = load_image_sets()

# ─────────────────────────────────────────────────────────────────────────────
# TTT helpers
# ─────────────────────────────────────────────────────────────────────────────
def ttt_snapshot():
    s = ttt_state
    return {
        "board":      s["board"],
        "turn":       s["turn"],
        "status":     s["status"],
        "winner":     s["winner"],
        "last_nodes": s["last_nodes"],
        "last_time":  round(s["last_time"], 4) if s["last_time"] else None,
        "move_count": s["move_count"],
    }

def ttt_check():
    board     = ttt_state["board"]
    available = get_available_cells(board)
    done, result = game_over(board, available)
    if done:
        ttt_state["status"] = "win" if result != 0 else "draw"
        ttt_state["winner"] = ("X" if result == -1 else "O") if result != 0 else None
    else:
        ttt_state["turn"] = "O" if ttt_state["turn"] == "X" else "X"

# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", image_sets=list(IMAGE_SETS.keys()))

@app.route("/puzzle")
def puzzle_page():
    return render_template("puzzle.html")

@app.route("/images/<set_name>/<symbol>")
def get_image(set_name, symbol):
    if set_name not in IMAGE_SETS or symbol not in ("x", "o"):
        return "", 404
    path   = IMAGE_SETS[set_name][symbol]
    folder = os.path.dirname(os.path.abspath(path))
    return send_from_directory(folder, os.path.basename(path))

# TTT
@app.route("/ttt/state")
def ttt_get_state():
    return jsonify(ttt_snapshot())

@app.route("/ttt/move/<int:cell>", methods=["POST"])
def ttt_human_move(cell):
    if ttt_state["status"] != "playing" or ttt_state["turn"] != "X":
        return jsonify(ttt_snapshot())
    board = ttt_state["board"]
    if cell not in get_available_cells(board):
        return jsonify(ttt_snapshot())
    select_cell(board, "X", cell)
    ttt_state["move_count"] += 1
    ttt_check()
    return jsonify(ttt_snapshot())

@app.route("/ttt/ai_move", methods=["POST"])
def ttt_ai_move():
    if ttt_state["status"] != "playing" or ttt_state["turn"] != max_player:
        return jsonify(ttt_snapshot())
    algorithm = request.json.get("algorithm", "Minimax")
    board = ttt_state["board"]
    t0    = time.perf_counter()
    move, nodes = choose_best_move(board) if algorithm == "Minimax" else choose_best_move_ab(board)
    elapsed = time.perf_counter() - t0
    if move is not None:
        select_cell(board, max_player, move)
        ttt_state["move_count"] += 1
        ttt_state["last_nodes"]  = nodes
        ttt_state["last_time"]   = elapsed
        ttt_check()
    return jsonify(ttt_snapshot())

@app.route("/ttt/reset", methods=["POST"])
def ttt_reset():
    ttt_state.update({"board": set_board(), "turn": "X", "status": "playing",
                      "winner": None, "last_nodes": None, "last_time": None, "move_count": 0})
    return jsonify(ttt_snapshot())

# Puzzle
@app.route("/puzzle/state")
def puzzle_get_state():
    return jsonify(puzzle_state)

@app.route("/puzzle/solve", methods=["POST"])
def puzzle_solve():
    algorithm = request.json.get("algorithm", "BFS")
    board     = tuple(puzzle_state["board"])
        # Inside app.py under @app.route("/puzzle/solve", methods=["POST"])
    if algorithm == "BFS":
        path, nodes, elapsed = BFS_Shortest_Path(board, Goal)
        puzzle_state["result"] = {
            "algorithm": "BFS", 
            "steps": len(path) - 1 if path else "—", 
            "nodes": nodes, 
            "elapsed": round(elapsed, 4),
            "path": path  # Add this line so JavaScript can read the path list!
        }
    elif algorithm == "Dijkstra":
        path, nodes, elapsed = Dijkstra(board, Goal)
        puzzle_state["result"] = {
                    "algorithm": "Dijkstra", 
                    "steps": len(path) - 1 if path else "—", 
                    "nodes": nodes, 
                    "elapsed": round(elapsed, 4),
                    "path": path  # Add this line so JavaScript can read the path list!
                }
    elif algorithm == "A*":
        path, nodes, elapsed = A_Star_Search(board, Goal)
        puzzle_state["result"] = {
                    "algorithm": "A*", 
                    "steps": len(path) - 1 if path else "—", 
                    "nodes": nodes, 
                    "elapsed": round(elapsed, 4),
                    "path": path  # Add this line so JavaScript can read the path list!
                }
    else:
        puzzle_state["result"] = {"algorithm": algorithm, "steps": "—", "nodes": "—", "elapsed": "—"}
    return jsonify(puzzle_state)

@app.route("/puzzle/reset", methods=["POST"])
def puzzle_reset():
    puzzle_state.update({"board": list(Start), "result": None})
    return jsonify(puzzle_state)

@app.route("/puzzle/randomize", methods=["POST"])
def puzzle_randomize():
    puzzle_state["board"]  = list(randommizer(tuple(puzzle_state["board"])))
    puzzle_state["result"] = None
    return jsonify(puzzle_state)

if __name__ == "__main__":
    app.run(debug=True)