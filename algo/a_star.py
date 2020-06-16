import random
import time
import os


class AStar:
    def __init__(self, graph, start, end=None):
        self.graph = graph
        self.start = start
        self.end = end

        self.solution = {key: 0 for key in graph}
