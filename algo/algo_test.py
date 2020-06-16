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

# Test case evaluator


def evaluate(correct_solution, solution):
    if(correct_solution == solution):
        return "Test Case Passed"
    return "Test Case Failed"


# Testing for Breadth First Search
BFS = BreadthFirstSearch(graph, 2)
solution = BFS.fit()
print(str(evaluate([2, 0, 3, 1], solution)))

BFS = BreadthFirstSearch(tree, 0)
solution = BFS.fit()
print(str(evaluate([0, 1, 2, 3, 4, 5], solution)))

BFS = BreadthFirstSearch(tree, 0, 2)
solution = BFS.fit()
print(str(evaluate([0, 1, 2], solution)))

BFS = BreadthFirstSearch(tree_string, "0")
solution = BFS.fit()
print(str(evaluate(["0", "1", "2", "3"], solution)))

# Testing for Depth First Search
DFS = DepthFirstSearch(graph, 2)
solution = DFS.fit()
print(str(evaluate([2, 0, 1, 3], solution)))

DFS = DepthFirstSearch(tree, 0)
solution = DFS.fit()
print(str(evaluate([0, 1, 2, 4, 5, 3], solution)))

DFS = DepthFirstSearch(tree, 0, 2)
solution = DFS.fit()
print(str(evaluate([0, 1, 2], solution)))

DFS = DepthFirstSearch(tree_string, "0")
solution = DFS.fit()
print(str(evaluate(["0", "1", "2", "3"], solution)))
