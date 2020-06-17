import copy


class BreadthFirstSearch:
    def __init__(self, graph, start, end=None):
        self.graph = graph
        self.start = start
        self.end = end

        self.queue = []
        self.visited = {key: 0 for key in graph}
        self.solution = []

        self.parent = {}

    def fit(self):
        # Edge case - Start node without neighbours
        if not self.graph[self.start]:
            return []

        # Edge case - End node does not exist
        if self.end and self.end not in self.graph.keys():
            return None

        open_set_cache = []

        # Adding the start node to the solution list
        # Adding all the neighbours of the start node
        # to the BFS queue and marking them as visited
        self.visited[self.start] = 1
        self.solution.append(self.start)
        node_list = self.graph[self.start]
        for node in node_list:
            self.queue.append(node)
            self.parent[node] = self.start

        open_set_cache.append(copy.deepcopy(self.queue))

        # While loop to repeat the above process till
        # the queue becomes empty
        while (self.queue):
            curr_node = self.queue.pop(0)
            self.visited[curr_node] = 1
            self.solution.append(curr_node)

            # Breaking out of the loop when destination
            # is reached
            if self.end != None and curr_node == self.end:
                break

            # Adding only the unmarked neighbours of
            # the current node the queue
            for adjacent in self.graph[curr_node]:
                if self.visited[adjacent] != 1:
                    self.queue.append(adjacent)
                    self.parent[adjacent] = curr_node

            open_set_cache.append(copy.deepcopy(self.queue))

        if not self.end or self.end in self.solution:
            return self.solution, open_set_cache
        return None

    def back_track(self):
        print(self.parent)
        if self.end and self.parent:
            path = [self.end]
            while path[-1] != self.start:
                path.append(self.parent[path[-1]])
            path.reverse()

            return path
