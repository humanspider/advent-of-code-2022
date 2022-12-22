import copy

class Point:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = x_coord
        self.y = y_coord
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def move_knot(h_coord: Point, t_coord: Point):
    x_dif = h_coord.x - t_coord.x
    y_dif = h_coord.y - t_coord.y
    if abs(x_dif) == 2:
        t_coord.x += 1 * int(x_dif/abs(x_dif))
        if y_dif != 0:
            t_coord.y += int(y_dif/abs(y_dif))

    elif abs(y_dif) == 2:
        t_coord.y += 1 * int(y_dif/abs(y_dif))
        if x_dif != 0:
            t_coord.x += int(x_dif/abs(x_dif))

def print_rope(knot_list: list[Point]):
    grid: list[bytearray] = []
    for y in range(21):
        grid.append(bytearray('.'*21, encoding='ascii'))
    
    for i in range(len(knot_list)-1, -1, -1):
        if i == 0:
            grid[knot_list[i].y+10][knot_list[i].x+10] = ord('H')
        else:
            grid[knot_list[i].y+10][knot_list[i].x+10] = ord(str(i))

    for i, line in enumerate(reversed(grid)):
        print(str(10-i).rjust(3) + line.decode())
    print()

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        n_knot = 10
        knot_list = []
        for i in range(n_knot):
            knot_list.append(Point(0, 0))
        h_coord = knot_list[0]
        t_coord = knot_list[n_knot-1]
        t_coord_history = set([copy.copy(t_coord)])
        for line in f:
            tokens = line.rstrip().split(' ')
            # move head
            match tokens[0]:
                case 'U':
                    for i in range(int(tokens[1])):
                        h_coord.y += 1
                        for i in range(n_knot-1):
                            move_knot(knot_list[i], knot_list[i+1])
                        t_coord_history.add(copy.copy(t_coord))
                case 'D':
                    for i in range(int(tokens[1])):
                        h_coord.y -= 1
                        for i in range(n_knot-1):
                            move_knot(knot_list[i], knot_list[i+1])
                        t_coord_history.add(copy.copy(t_coord))
                case 'L':
                    for i in range(int(tokens[1])):
                        h_coord.x -= 1
                        for i in range(n_knot-1):
                            move_knot(knot_list[i], knot_list[i+1])
                        t_coord_history.add(copy.copy(t_coord))
                case 'R':
                    for i in range(int(tokens[1])):
                        h_coord.x += 1
                        for i in range(n_knot-1):
                            move_knot(knot_list[i], knot_list[i+1])
                        t_coord_history.add(copy.copy(t_coord))
            
            # print_rope(knot_list)
        
        print(len(t_coord_history))