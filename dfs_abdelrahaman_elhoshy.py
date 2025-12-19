import collections
import sys

# Set recursion limit higher for deep searches like DFS and IDS
sys.setrecursionlimit(2000)

# --- Project Setup ---
# Grid: 0 = free cell, 1 = obstacle
GRID = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
ROWS = len(GRID)
COLS = len(GRID[0])
START = (0, 0)
GOAL = (6, 9)
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Right, Left, Down, Up

# --- Helper Functions ---
def is_valid(r, c):
    """Checks if a cell is within bounds and not an obstacle."""
    return 0 <= r < ROWS and 0 <= c < COLS and GRID[r][c] == 0

def reconstruct_path(came_from, current):
    """Reconstructs the path from the came_from dictionary."""
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(START)
    path.reverse()
    return path

# --- Algorithm Implementation ---

# Implemented by: Abdelrahaman elhoshy
# Description: Depth-First Search (DFS) explores as far as possible along each branch
# before backtracking. It uses a stack (LIFO) to manage the order of nodes to visit.
# DFS is not guaranteed to find the shortest path (not optimal) and can get stuck
# in infinite loops in graphs without cycle detection. In this finite grid, it is
# complete but not optimal.
def dfs(start, goal):
    """Depth-First Search implementation."""
    print(f"--- Running DFS (Implemented by: Abdelrahaman elhoshy) ---")
    stack = [start]
    visited = {start}
    came_from = {}
    visited_nodes = []

    while stack:
        current = stack.pop()
        visited_nodes.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            print(f"Visited Nodes: {visited_nodes}")
            print(f"Path Found: {path}")
            return len(path) - 1, path

        r, c = current
        # Reverse the order of neighbors to explore in a consistent manner (e.g., Right, Down, Left, Up)
        # The order of neighbor exploration affects the path found by DFS.
        for dr, dc in reversed(DIRECTIONS):
            neighbor = (r + dr, c + dc)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                stack.append(neighbor)

    print(f"Visited Nodes: {visited_nodes}")
    return -1, None # Path not found

# --- Main Execution ---
if __name__ == "__main__":
    print("Grid-Based Pathfinding Problem Setup:")
    print(f"Start: {START}, Goal: {GOAL}")
    
    length, path = dfs(START, GOAL)
    
    if path:
        print(f"\nDFS Result:")
        print(f"Path Length: {length}")
        print(f"Path: {path}")
    else:
        print("\nDFS Result: Path not found.")
