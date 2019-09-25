from simpleMazeKata.Maze import Maze

maze = ['### ####',
        '# # ##  ',
        '# #k#  ####',
        '# # # ##',
        '#  # # ##',
        '      #',
        '#######']

print Maze()\
        .define(maze)\
        .has_exit()
