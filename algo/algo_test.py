from bfs import BreadthFirstSearch
from dfs import DepthFirstSearch
from a_star import AStar


# Test cases
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

tree = {
    0: [1, 2, 3],
    1: [],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

tree_string = {
    "0": ["1", "2", "3"],
    "1": [],
    "2": [],
    "3": [],
}

grid = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 5],
    3: [0, 6],
    5: [2, 8],
    6: [3, 7],
    7: [6, 8],
    8: [5, 7]
}

grid_blocked = {
    0: [1],
    1: [0, 2],
    2: [1],
    6: [7],
    7: [6, 8],
    8: [7]
}

grid_complicated = {
    0: [1, 3],
    1: [0, 2],
    2: [1],
    3: [0, 6],
    6: [3, 7],
    7: [6, 8],
    8: [7]
}


def evaluate(correct_solution, solution):
    if(correct_solution == solution):
        return "Test Case Passed"
    return "Test Case Failed"


# Testing for Breadth First Search Algorithm
print("--- Testing BFS ---")
BFS = BreadthFirstSearch(graph, 2)
solution, closed_set = BFS.fit()
print(solution, closed_set)
print(str(evaluate([2, 0, 3, 1], solution)))

BFS = BreadthFirstSearch(tree, 0)
solution, closed_set = BFS.fit()
print(solution, closed_set)
print(str(evaluate([0, 1, 2, 3, 4, 5], solution)))

BFS = BreadthFirstSearch(tree, 0, 2)
solution, closed_set = BFS.fit()
print(solution, closed_set)
print(str(evaluate([0, 1, 2], solution)))

BFS = BreadthFirstSearch(tree_string, "0")
solution, closed_set = BFS.fit()
print(solution, closed_set)
print(str(evaluate(["0", "1", "2", "3"], solution)))


# Testing for Depth First Search Algorithm
print("--- Testing DFS ---")
DFS = DepthFirstSearch(graph, 2)
solution, closed_set = DFS.fit()
print(solution, closed_set)
print(str(evaluate([2, 0, 1, 3], solution)))

DFS = DepthFirstSearch(tree, 0, 4)
solution, closed_set = DFS.fit()
print(solution, closed_set)
print(str(evaluate([0, 1, 2, 4], solution)))

DFS = DepthFirstSearch(tree, 0, 2)
solution, closed_set = DFS.fit()
print(solution, closed_set)
print(str(evaluate([0, 1, 2], solution)))

DFS = DepthFirstSearch(tree_string, "0")
solution, closed_set = DFS.fit()
print(solution, closed_set)
print(str(evaluate(["0", "1", "2", "3"], solution)))

DFS = DepthFirstSearch(grid_blocked, 0, 7)
solution = DFS.fit()
print(solution, closed_set)


# Tesing for A* Algorithm
print("--- Testing A* ---")
AS = AStar(grid, (3, 3), 0, 5)
solution, open_set_cache = AS.fit()
print(open_set_cache, solution)
# print(str(evaluate([0, 3, 6, 7], solution)))

AS = AStar(grid_blocked, (3, 3), 0, 7)
solution, open_set_cache = AS.fit()
# print(open_set_cache, solution)
# print(str(evaluate(None, solution)))

AS = AStar(grid_complicated, (3, 3), 0, 7)
solution, open_set_cache = AS.fit()
# print(open_set_cache, solution)
