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

# Implemented by: Anas Elzanaty
# Description: Iterative Deepening Search (IDS) combines the space efficiency of DFS
# with the completeness and optimality of BFS (for unit costs). It performs a series
# of Depth-Limited Search (DLS) searches, gradually increasing the depth limit.
# This approach is optimal and complete, while using memory proportional to the depth.
def ids(start, goal):
    """Iterative Deepening Search implementation."""
    print(f"--- Running IDS (Implemented by: Anas Elzanaty) ---")
    
    # Helper function for Depth-Limited Search (DLS)
    def dls(current, goal, came_from, limit, visited_in_dls):
        visited_in_dls.append(current)
        
        if current == goal:
            return True, came_from
        
        if limit == 0:
            return False, came_from

        r, c = current
        for dr, dc in DIRECTIONS:
            neighbor = (r + dr, c + dc)
            # Check if valid and not already in the current path (to avoid immediate cycles)
            if is_valid(neighbor[0], neighbor[1]) and neighbor not in came_from:
                came_from[neighbor] = current
                found, final_came_from = dls(neighbor, goal, came_from, limit - 1, visited_in_dls)
                if found:
                    return True, final_came_from
                # Backtrack: remove the neighbor from came_from if not found in this branch
                del came_from[neighbor]
        return False, came_from

    max_depth = ROWS * COLS # A safe upper bound for the depth limit
    total_visited_nodes = []

    for depth_limit in range(max_depth):
        # Reset state for each iteration
        came_from = {start: None}
        visited_in_dls = []
        
        found, final_came_from = dls(start, goal, came_from, depth_limit, visited_in_dls)
        total_visited_nodes.extend(visited_in_dls)
        
        if found:
            path = reconstruct_path(final_came_from, goal)
            # Note: IDS prints all nodes visited across all iterations.
            print(f"Visited Nodes (across all iterations): {total_visited_nodes}")
            print(f"Path Found: {path}")
            return len(path) - 1, path
        
        # If the last DLS didn't find the goal but didn't explore any new nodes, we can stop
        if not visited_in_dls and depth_limit > 0:
             break

    print(f"Visited Nodes (across all iterations): {total_visited_nodes}")
    return -1, None # Path not found

# --- Main Execution ---
if __name__ == "__main__":
    print("Grid-Based Pathfinding Problem Setup:")
    print(f"Start: {START}, Goal: {GOAL}")
    
    length, path = ids(START, GOAL)
    
    if path:
        print(f"\nIDS Result:")
        print(f"Path Length: {length}")
        print(f"Path: {path}")
    else:
        print("\nIDS Result: Path not found.")
