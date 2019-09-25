class InvalidMazeDefinition(Exception):

    def __init__(self, errors):
        self.errors = errors
        super(InvalidMazeDefinition, self).__init__("Invalid Maze Definition (not found a grid or multiple Kates)")
