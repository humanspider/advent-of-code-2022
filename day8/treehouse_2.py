def scenic_score(tree_grid: list[list[int]], x: int, y: int)-> int:
    length = len(tree_grid)
    width = len(tree_grid[0])
    this_tree = tree_grid[y][x]

    if y == 0 or y == length-1 or x == 0 or x == width-1:
        return 0

    up_score = 0
    for up in range(y-1, -1, -1):
        up_score += 1
        if tree_grid[up][x] < this_tree:
            continue
        else:
            break
    
    left_score = 0
    for left in range(x-1, -1, -1):
        left_score += 1
        if tree_grid[y][left] < this_tree:
            continue
        else:
            break

    down_score = 0
    for down in range(y+1, length):
        down_score += 1
        if tree_grid[down][x] < this_tree:
            continue
        else:
            break
    
    right_score = 0
    for right in range(x+1, width):
        right_score += 1
        if tree_grid[y][right] < this_tree:
            continue
        else:
            break
    
    return up_score*left_score*down_score*right_score

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

    high_score = 0    
    for i in range(length):
        for j in range(width):
            score = scenic_score(tree_grid, j, i)
            if score > high_score:
                high_score = score
    
    print(high_score)
    