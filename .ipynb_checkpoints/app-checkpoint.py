import streamlit as st

# from ttt import Minimax, AlphaBeta
from puzzle_8 import (
    BFS_Shortest_Path,
    Dijkstra,
    randommizer,
    Start,
    Goal,
)


st.set_page_config(
    page_title="AI Search Lab",
    layout="wide"
)


# -----------------------------
# Helper display functions
# -----------------------------
def show_puzzle(board):
    """Display a flat 9-value puzzle tuple/list as a 3x3 grid."""
    for row in range(3):
        st.write(board[row * 3 : row * 3 + 3])


def show_dashboard(
    decision_time=None,
    nodes=None,
    solution_length=None,
    pruning=None,
):
    """Shared dashboard for both modules."""
    st.subheader("Performance Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Decision Time",
        "--" if decision_time is None else f"{decision_time:.4f} sec",
    )

    col2.metric(
        "Nodes Explored",
        "--" if nodes is None else nodes,
    )

    col3.metric(
        "Solution Length",
        "--" if solution_length is None else solution_length,
    )

    col4.metric(
        "Pruning Efficiency",
        "N/A" if pruning is None else f"{pruning:.2f}%",
    )


# -----------------------------
# Session state setup
# -----------------------------
if "puzzle_board" not in st.session_state:
    st.session_state.puzzle_board = Start

if "puzzle_result" not in st.session_state:
    st.session_state.puzzle_result = None


# -----------------------------
# Main app title and navigation
# -----------------------------
st.title("AI Search Lab")

module = st.sidebar.radio(
    "Choose Module",
    ["8-Puzzle Solver", "Tic-Tac-Toe AI"],
)


# ============================================================
# Module A: 8-Puzzle Solver
# ============================================================
if module == "8-Puzzle Solver":
    st.header("Module A: 8-Puzzle Solver")

    st.write("Solve the 8-puzzle using BFS, Dijkstra, or A*.")

    algorithm = st.selectbox(
        "Choose Algorithm",
        ["BFS", "Dijkstra", "A*"],
    )

    st.subheader("Current Puzzle")
    show_puzzle(st.session_state.puzzle_board)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Use Required Test Puzzle"):
            st.session_state.puzzle_board = Start
            st.session_state.puzzle_result = None
            st.rerun()

    with col2:
        if st.button("Randomize Puzzle"):
            st.session_state.puzzle_board = randommizer(Goal)
            st.session_state.puzzle_result = None
            st.rerun()

    with col3:
        solve_clicked = st.button("Solve Puzzle")

    if solve_clicked:
        if algorithm == "BFS":
            steps, nodes, elapsed = BFS_Shortest_Path(
                st.session_state.puzzle_board,
                Goal,
            )

            st.session_state.puzzle_result = {
                "algorithm": "BFS",
                "steps": steps,
                "nodes": nodes,
                "elapsed": elapsed,
            }

        elif algorithm == "Dijkstra":
            steps, nodes, elapsed = Dijkstra(
                st.session_state.puzzle_board,
                Goal,
            )

            st.session_state.puzzle_result = {
                "algorithm": "Dijkstra",
                "steps": steps,
                "nodes": nodes,
                "elapsed": elapsed,
            }

        else:
            st.warning("A* is not connected yet.")
            st.session_state.puzzle_result = None

    if st.session_state.puzzle_result:
        result = st.session_state.puzzle_result

        st.success(f"{result['algorithm']} completed.")

        show_dashboard(
            decision_time=result["elapsed"],
            nodes=result["nodes"],
            solution_length=result["steps"],
            pruning=None,
        )
    else:
        show_dashboard()


# ============================================================
# Module B: Tic-Tac-Toe AI
# ============================================================
if module == "Tic-Tac-Toe AI":
    st.header("Module B: Tic-Tac-Toe with AI")

    st.info("Tic-Tac-Toe UI placeholder. Connect ttt.py functions here once Minimax and Alpha-Beta are ready.")

    mode = st.selectbox(
        "Choose Game Mode",
        ["Human vs AI", "AI vs AI"],
    )

    algorithm_x = st.selectbox(
        "Algorithm for X",
        ["Minimax", "Alpha-Beta"],
    )

    algorithm_o = st.selectbox(
        "Algorithm for O",
        ["Minimax", "Alpha-Beta"],
    )

    st.subheader("Game Status")
    st.write("Current Turn: X")
    st.write("Game State: Playing")
    st.write("Winner: None")

    st.subheader("Board")

    board = list(range(9))

    row1 = st.columns(3)
    for i in range(3):
        with row1[i]:
            st.button(str(board[i]), key=f"ttt_cell_{i}")

    row2 = st.columns(3)
    for i in range(3, 6):
        with row2[i - 3]:
            st.button(str(board[i]), key=f"ttt_cell_{i}")

    row3 = st.columns(3)
    for i in range(6, 9):
        with row3[i - 6]:
            st.button(str(board[i]), key=f"ttt_cell_{i}")

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Start Game")

    with col2:
        st.button("Run AI Move")

    with col3:
        st.button("Reset Board")

    show_dashboard()