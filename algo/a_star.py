import random
import time
import os


class AStar:
    '''
    This implementation of the A Start algorithm 
    will only work for a grid like graph becasue
    the heuristic to be used is SLD.
    '''

    def __init__(self, grid, grid_dims, start, end):
        self.grid = grid
        self.grid_dims = grid_dims
        self.start = start
        self.end = end

        self.solution = []
        self.visited = {key: 0 for key in grid}

    def id_to_loc(self, id):
        grid_l, grid_b = self.grid_dims
        return (id//(grid_l), id % (grid_l))

    def heuristic(self, curr_index):
        curr_pos = self.id_to_loc(curr_index)
        end_pos = self.id_to_loc(self.end)

        return ((curr_pos[0]-end_pos[0])**2 + (curr_pos[1]-end_pos[1])**2)**0.5

    def fit(self):
        curr_node = self.start
        self.solution.append(curr_node)
        self.visited[curr_node] = 1
        while(curr_node != self.end):
            heuristic_cost = {}
            for adjacent in self.grid[curr_node]:
                if not self.visited[adjacent]:
                    heuristic_cost[adjacent] = self.heuristic(adjacent)
                    self.visited[adjacent] = 1

            if heuristic_cost:
                temp = min(heuristic_cost.values())
                curr_node = [
                    key for key in heuristic_cost if heuristic_cost[key] == temp][0]
            self.solution.append(curr_node)

        return self.solution
