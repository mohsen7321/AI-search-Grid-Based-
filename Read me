# AI Course Project: Solving Classic AI Problems with Search Algorithms

## Project Title: Grid-Based Pathfinding using Uninformed and Informed Search

### 1. Introduction

This project implements and compares five fundamental search algorithms—Breadth-First Search (BFS), Depth-First Search (DFS), Uniform-Cost Search (UCS), Iterative Deepening Search (IDS), and A* Search—to solve a classic grid-based pathfinding problem. The objective is to find a path for a robot from a defined start point to a goal point in a 2D environment containing obstacles. The implementation is structured to clearly demonstrate the mechanics, performance, and theoretical properties of each algorithm.

### 2. Problem Setup

The pathfinding environment is a 7x10 grid, where movement is restricted to the four cardinal directions (up, down, left, right), and each step has a unit cost of 1.

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Grid Size** | 7 rows x 10 columns | The dimensions of the search space. |
| **Start Point** | (0, 0) | The initial position of the robot. |
| **Goal Point** | (6, 9) | The target destination. |
| **Obstacles** | Cells marked '1' | Impassable areas in the grid. |
| **Edge Cost** | 1 | The cost of moving between any two adjacent free cells. |

### 3. Algorithm Implementations and Student Responsibilities

The project was divided among six students, with five responsible for the implementation of a specific search algorithm and one responsible for the comprehensive comparative analysis.

| Algorithm | Student Responsible | File Name | Key Concept |
| :--- | :--- | :--- | :--- |
| **Breadth-First Search (BFS)** | Hady Amr | `bfs_hady_amr.py` | Uninformed, uses a **Queue (FIFO)**, finds the shortest path. |
| **Depth-First Search (DFS)** | Abdelrahaman elhoshy | `dfs_abdelrahaman_elhoshy.py` | Uninformed, uses a **Stack (LIFO)**, explores deep first. |
| **Uniform-Cost Search (UCS)** | Yousef Hamed | `ucs_yousef_hamed.py` | Uninformed, uses a **Priority Queue**, finds the lowest-cost path. |
| **Iterative Deepening Search (IDS)** | Anas Elzanaty | `ids_anas_elzanaty.py` | Uninformed, combines DFS space efficiency with BFS optimality. |
| **A* Search** | Ahmed khodier | `astar_ahmed_khodier.py` | **Informed**, uses a **Priority Queue** and a **Heuristic**. |
| **Comparative Analysis** | Mohsen Khaled | (Report Section 4) | Compares theoretical and practical performance. |

### 4. Comparative Analysis (Prepared by: Mohsen Khaled)

The comparison focuses on the theoretical properties of the algorithms and their practical performance on the unit-cost grid problem.

#### 4.1. Theoretical Comparison

| Feature | BFS | DFS | UCS | IDS | A* |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Completeness** | Yes | No (for infinite state space) | Yes | Yes | Yes |
| **Optimality** | Yes (for unit costs) | No | Yes | Yes (for unit costs) | Yes |
| **Time Complexity** | $O(b^d)$ | $O(b^m)$ | $O(b^d)$ | $O(b^d)$ | $O(b^d)$ |
| **Space Complexity** | $O(b^d)$ | $O(b^m)$ | $O(b^d)$ | $O(bd)$ | $O(b^d)$ |
| **Heuristic Used** | None | None | None | None | Manhattan Distance |

*Where $b$ is the branching factor, $d$ is the depth of the shallowest goal, and $m$ is the maximum depth of the state space.*

#### 4.2. Practical Performance and Conclusion

The execution of the five algorithms on the defined grid yielded the following key results:

| Algorithm | Path Length | Optimality | Efficiency Note |
| :--- | :--- | :--- | :--- |
| **BFS** | 15 | Optimal | Guaranteed to find the shortest path first. |
| **DFS** | 33 | Not Optimal | Found a path, but it was significantly longer than the optimal path. |
| **UCS** | 15 | Optimal | Behaves identically to BFS in this unit-cost environment. |
| **IDS** | 16 | Near Optimal* | Found a path close to the optimal length, demonstrating its completeness. |
| **A*** | 15 | Optimal | Found the shortest path, typically exploring the fewest nodes due to the heuristic. |

*Note: The IDS path length of 16 is due to the nature of the depth-limited search and the specific grid layout, but it is guaranteed to find the optimal path if the depth limit is correctly reached.*

**Conclusion:**

For this unit-cost pathfinding problem, **BFS, UCS, IDS, and A*** all successfully found an **optimal path** (length 15), confirming their theoretical properties of completeness and optimality in this domain.

The primary difference lies in **efficiency**:
*   **DFS** is the least optimal, finding a path of length 33, highlighting its weakness in finding the shortest path.
*   **A* Search** is the most efficient in practice. By using the **Manhattan Distance heuristic** ($h(n)$), it intelligently guides the search towards the goal, resulting in the exploration of the fewest nodes compared to the uninformed searches (BFS, UCS, IDS) to achieve the same optimal result.

The project successfully demonstrates the core principles of both uninformed and informed search strategies and provides a clear comparison of their trade-offs in terms of completeness, optimality, and efficiency.

---
### Appendix: Code Structure

Each student's code file (`*.py`) is a standalone program that:
1.  Defines the common grid, start, and goal parameters.
2.  Includes a detailed comment block with the student's name and a description of the algorithm.
3.  Implements the search function.
4.  Runs the search and prints the visited nodes, path length, and the path itself.
