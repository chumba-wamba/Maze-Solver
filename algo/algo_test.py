from bfs import BreadthFirstSearch
from dfs import DepthFirstSearch

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

# Testing for Breadth First Search
BFS = BreadthFirstSearch(graph, 2)
solution = BFS.fit()
print(solution)

BFS = BreadthFirstSearch(tree, 0)
solution = BFS.fit()
print(solution)

BFS = BreadthFirstSearch(tree_string, "0")
solution = BFS.fit()
print(solution)

# Testing for Depth First Search
DFS = DepthFirstSearch(graph, 2)
solution = DFS.fit()
print(solution)

DFS = DepthFirstSearch(tree, 0)
solution = DFS.fit()
print(solution)

DFS = DepthFirstSearch(tree_string, "0")
solution = DFS.fit()
print(solution)
