import random
import time
import os


class BreadthFirstSearch:
    def __init__(self, graph, start, end=None):
        self.graph = graph
        self.start = start
        self.end = end

        self.queue = []
        self.visited = {key: 0 for key in graph}
        self.solution = []

    def fit(self):
        # Edge case - Start node without neighbours
        if not self.graph[self.start]:
            return []

        # Adding the start node to the solution list
        # Adding all the neighbours of the start node
        # to the BFS queue and marking them as visited
        self.visited[self.start] = 1
        self.solution.append(self.start)
        node_list = self.graph[self.start]
        for node in node_list:
            self.queue.append(node)

        # While loop to repeat the above process till
        # the queue becomes empty
        while (self.queue):
            curr_node = self.queue.pop(0)
            self.visited[curr_node] = 1
            self.solution.append(curr_node)

            # Adding only the unmarked neighbours of
            # the current node the queue
            for temp_node in self.graph[curr_node]:
                if self.visited[temp_node] != 1:
                    self.queue.append(temp_node)

        return self.solution