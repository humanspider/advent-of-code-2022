def is_visible(tree_grid: list[list[int]], x: int, y: int)-> bool:
    length = len(tree_grid)
    width = len(tree_grid[0])
    this_tree = tree_grid[y][x]

    if y == 0 or y == length-1 or x == 0 or x == width-1:
        return True
    else:
        # check up
        if all([that_tree < this_tree for that_tree in map(lambda up: tree_grid[up][x], list(range(y-1, -1, -1)))]):
            return True

        # check left
        if all([that_tree < this_tree for that_tree in map(lambda left: tree_grid[y][left], list(range(x-1, -1, -1)))]):
            return True

        # check down
        if all([that_tree < this_tree for that_tree in map(lambda down: tree_grid[down][x], list(range(y+1, length)))]):
            return True

        # check right
        if all([that_tree < this_tree for that_tree in map(lambda right: tree_grid[y][right], list(range(x+1, width)))]):
            return True
        
        return False

if __name__ == '__main__':
    tree_grid = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            tree_line = []
            for char in line:
                tree_line.append(int(char))
            tree_grid.append(tree_line)
    
    visible = 0
    length = len(tree_grid)
    width = len(tree_grid[0])

    for i in range(length):
        for j in range(width):
            if is_visible(tree_grid, j, i):
                visible += 1
    
    print(visible)
    