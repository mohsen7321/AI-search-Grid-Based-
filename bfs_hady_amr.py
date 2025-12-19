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

# Implemented by: Hady Amr
# Description: Breadth-First Search (BFS) is a complete and optimal search algorithm
# for unweighted graphs (like this grid where all steps cost 1). It explores all nodes
# at the present depth level before moving on to the nodes at the next depth level.
# It guarantees finding the shortest path first. It uses a queue (FIFO) to manage
# the order of nodes to visit.
def bfs(start, goal):
    """Breadth-First Search implementation."""
    print(f"--- Running BFS (Implemented by: Hady Amr) ---")
    queue = collections.deque([start])
    visited = {start}
    came_from = {}
    visited_nodes = []

    while queue:
        current = queue.popleft()
        visited_nodes.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            print(f"Visited Nodes: {visited_nodes}")
            print(f"Path Found: {path}")
            return len(path) - 1, path

        r, c = current
        for dr, dc in DIRECTIONS:
            neighbor = (r + dr, c + dc)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)

    print(f"Visited Nodes: {visited_nodes}")
    return -1, None # Path not found

# --- Main Execution ---
if __name__ == "__main__":
    print("Grid-Based Pathfinding Problem Setup:")
    print(f"Start: {START}, Goal: {GOAL}")
    
    length, path = bfs(START, GOAL)
    
    if path:
        print(f"\nBFS Result:")
        print(f"Path Length: {length}")
        print(f"Path: {path}")
    else:
        print("\nBFS Result: Path not found.")
