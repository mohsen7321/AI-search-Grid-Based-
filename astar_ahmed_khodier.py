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

def manhattan_distance(p1, p2):
    """Manhattan distance heuristic: h(n) = |x1 - x2| + |y1 - y2|."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# --- Algorithm Implementation ---

# Implemented by: Ahmed khodier
# Description: A* Search is an informed, complete, and optimal search algorithm.
# It uses a heuristic function h(n) to estimate the cost to the goal, and prioritizes
# nodes based on f(n) = g(n) + h(n), where g(n) is the cost from the start.
# The heuristic used here is the Manhattan Distance, which is admissible (never
# overestimates the cost) and consistent, ensuring A* finds the shortest path.
def a_star(start, goal):
    """A* Search implementation."""
    print(f"--- Running A* (Implemented by: Ahmed khodier) ---")
    # Priority queue stores tuples: (f_score, g_score, node)
    # f_score = g_score + h_score
    priority_queue = [(manhattan_distance(start, goal), 0, start)]
    g_score = {start: 0}
    came_from = {}
    visited_nodes = []

    while priority_queue:
        f_score, cost, current = heapq.heappop(priority_queue)
        
        # Check if the node has already been processed with a better path
        if current in visited_nodes:
            continue
            
        visited_nodes.append(current)

        if current == goal:
            path = reconstruct_path(came_from, current)
            print(f"Visited Nodes: {visited_nodes}")
            print(f"Path Found: {path}")
            return len(path) - 1, path

        r, c = current
        for dr, dc in DIRECTIONS:
            neighbor = (r + dr, c + dc)
            
            if is_valid(neighbor[0], neighbor[1]):
                new_g_score = g_score[current] + 1 # All edge costs are 1
                
                if neighbor not in g_score or new_g_score < g_score[neighbor]:
                    g_score[neighbor] = new_g_score
                    h_score = manhattan_distance(neighbor, goal)
                    f_score = new_g_score + h_score
                    heapq.heappush(priority_queue, (f_score, new_g_score, neighbor))
                    came_from[neighbor] = current

    print(f"Visited Nodes: {visited_nodes}")
    return -1, None # Path not found

# --- Main Execution ---
if __name__ == "__main__":
    print("Grid-Based Pathfinding Problem Setup:")
    print(f"Start: {START}, Goal: {GOAL}")
    
    length, path = a_star(START, GOAL)
    
    if path:
        print(f"\nA* Result:")
        print(f"Path Length: {length}")
        print(f"Path: {path}")
    else:
        print("\nA* Result: Path not found.")
