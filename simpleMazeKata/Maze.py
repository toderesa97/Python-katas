from simpleMazeKata.InvalidMazeDefinition import InvalidMazeDefinition


class Maze:

    def __init__(self):
        self.grid = []
        self.visited_positions = {}

    def define(self, grid):
        self.grid = grid
        return self

    def has_exit(self):
        kates_position = self.__find_kate_position()
        if len(self.grid) == 0 or kates_position == -1:
            raise InvalidMazeDefinition(None)
        else:
            return self.__find_light(kates_position)

    def __find_light(self, kate_position):
        current_cell = kate_position['list_position']
        cell_position = kate_position['str_index']
        if self.visited_positions.has_key(str(current_cell)+str(cell_position)):
            return False
        else:
            self.visited_positions.update({str(current_cell)+str(cell_position): ''})
        if current_cell == 0 or current_cell == len(self.grid) - 1:
            return True
        if cell_position == 0 or cell_position == len(self.grid[current_cell]) - 1:
            return True
        r = []
        if self.grid[current_cell][cell_position-1] == ' ': # left
            r.append(self.__find_light({'list_position': current_cell, 'str_index': cell_position-1}))
        if self.grid[current_cell][cell_position+1] == ' ': # right
            r.append(self.__find_light({'list_position': current_cell, 'str_index': cell_position+1}))
        if len(self.grid[current_cell+1]) > cell_position:
            if self.grid[current_cell+1][cell_position] == ' ': #down
                r.append(self.__find_light({'list_position': current_cell+1, 'str_index': cell_position}))
        if len(self.grid[current_cell-1]) > 0:
            if self.grid[current_cell-1][cell_position] == ' ': #up
                r.append(self.__find_light({'list_position': current_cell-1, 'str_index': cell_position}))
        return any(r)

    def __find_kate_position(self):
        ks = 0
        index = -1
        list_position = 0
        for i, slice_ in enumerate(self.grid):
            if "k" in slice_:
                if ks > 0:
                    return -1
                index = slice_.find('k')
                list_position = i
                ks = ks + 1
        return {'str_index': index, 'list_position': list_position}
