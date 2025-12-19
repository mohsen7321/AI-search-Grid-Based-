import collections
import heapq
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

# Implemented by: Yousef Hamed
# Description: Uniform-Cost Search (UCS) is a complete and optimal search algorithm
# that explores the node with the lowest cumulative cost (g(n)) from the start.
# It uses a priority queue to ensure that the lowest-cost path is always expanded next.
# Since all edge costs are 1 in this grid, it behaves identically to BFS, guaranteeing
# the shortest path.
def ucs(start, goal):
    """Uniform-Cost Search implementation."""
    print(f"--- Running UCS (Implemented by: Yousef Hamed) ---")
    # Priority queue stores tuples: (cost, node)
    priority_queue = [(0, start)]
    cost_so_far = {start: 0}
    came_from = {}
    visited_nodes = []

    while priority_queue:
        cost, current = heapq.heappop(priority_queue)
        visited_nodes.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            print(f"Visited Nodes: {visited_nodes}")
            print(f"Path Found: {path}")
            return len(path) - 1, path

        r, c = current
        for dr, dc in DIRECTIONS:
            neighbor = (r + dr, c + dc)
            new_cost = cost + 1 # All edge costs are 1
            
            if is_valid(neighbor[0], neighbor[1]):
                # Only update if the neighbor hasn't been visited or a shorter path is found
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    heapq.heappush(priority_queue, (priority, neighbor))
                    came_from[neighbor] = current

    print(f"Visited Nodes: {visited_nodes}")
    return -1, None # Path not found

# --- Main Execution ---
if __name__ == "__main__":
    print("Grid-Based Pathfinding Problem Setup:")
    print(f"Start: {START}, Goal: {GOAL}")
    
    length, path = ucs(START, GOAL)
    
    if path:
        print(f"\nUCS Result:")
        print(f"Path Length: {length}")
        print(f"Path: {path}")
    else:
        print("\nUCS Result: Path not found.")
