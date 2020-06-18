import copy


class AStar:
    '''
    This implementation of the A Start algorithm
    will only work for a 2D grid.
    '''

    def __init__(self, grid, grid_dims, start, end, heuristic="euclidean"):
        self.grid = grid
        self.grid_dims = grid_dims
        self.start = start
        self.end = end
        self.heuristic = heuristic

        self.solution = []
        self.visited = {key: 0 for key in grid}
        self.path_cache = []

    @staticmethod
    def id_to_loc(id, dims):
        grid_l, grid_b = dims
        return (id//(grid_l), id % (grid_l))

    def reconstruct_path(self, came_from, curr):
        total_path = [curr]
        while curr in came_from.keys():
            curr = came_from[curr]
            total_path.insert(0, curr)
        return total_path

    def euclidean_heuristic(self, curr_index):
        curr_pos = self.id_to_loc(curr_index, self.grid_dims)
        end_pos = self.id_to_loc(self.end, self.grid_dims)

        return ((curr_pos[0]-end_pos[0])**2 + (curr_pos[1]-end_pos[1])**2)**0.5

    def manhattan_heuristic(self, curr_index):
        curr_pos = self.id_to_loc(curr_index, self.grid_dims)
        end_pos = self.id_to_loc(self.end, self.grid_dims)

        return (abs(curr_pos[0]-end_pos[0]) + abs(curr_pos[1]-end_pos[1]))

    def heuristic_picker(self):
        if self.heuristic == None or self.heuristic == "euclidean":
            return self.euclidean_heuristic
        elif self.heuristic == "manhattan":
            return self.manhattan_heuristic

    def fit(self):
        if self.end not in self.grid.keys():
            return None

        open_set_cache = []

        open_set = {self.start}
        came_from = {}

        g_score = {key: 'inf' for key in self.grid}
        g_score[self.start] = 0

        f_score = {key: 'inf' for key in self.grid}
        f_score[self.start] = self.heuristic_picker()(self.start)

        while open_set:
            open_set_cache.append(copy.deepcopy(open_set))
            val = min([f_score[item] for item in open_set])
            for key, value in f_score.items():
                if val == value:
                    curr = key

            open_set.remove(curr)

            if curr == self.end:
                open_set_cache.append(copy.deepcopy(open_set))
                return self.reconstruct_path(came_from, curr), open_set_cache[1:]

            for adjacent in self.grid[curr]:
                tentative_g_score = g_score[curr]

                if g_score[adjacent] == "inf" or tentative_g_score < g_score[adjacent]:
                    came_from[adjacent] = curr
                    g_score[adjacent] = tentative_g_score
                    f_score[adjacent] = g_score[adjacent] + \
                        self.heuristic_picker()(adjacent)

                    if adjacent not in open_set:
                        open_set.add(adjacent)

            if not open_set:
                open_set_cache.append({})
        return self.reconstruct_path(came_from, curr), open_set_cache[1:]
