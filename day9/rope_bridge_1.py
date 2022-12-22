import copy

class Point:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = x_coord
        self.y = y_coord
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def move_tail(h_coord: Point, t_coord: Point):
    x_dif = h_coord.x - t_coord.x
    y_dif = h_coord.y - t_coord.y
    if abs(x_dif) == 2:
        t_coord.x += 1 * int(x_dif/abs(x_dif))
        if y_dif != 0:
            t_coord.y = h_coord.y

    elif abs(y_dif) == 2:
        t_coord.y += 1 * int(y_dif/abs(y_dif))
        if x_dif != 0:
            t_coord.x = h_coord.x

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        h_coord = Point(0,0)
        t_coord = Point(0,0)
        t_coord_history = set([copy.copy(t_coord)])
        for line in f:
            tokens = line.rstrip().split(' ')
            # move head
            match tokens[0]:
                case 'U':
                    for i in range(int(tokens[1])):
                        h_coord.y += 1
                        move_tail(h_coord, t_coord)
                        t_coord_history.add(copy.copy(t_coord))
                case 'D':
                    for i in range(int(tokens[1])):
                        h_coord.y -= 1
                        move_tail(h_coord, t_coord)
                        t_coord_history.add(copy.copy(t_coord))
                case 'L':
                    for i in range(int(tokens[1])):
                        h_coord.x -= 1
                        move_tail(h_coord, t_coord)
                        t_coord_history.add(copy.copy(t_coord))
                case 'R':
                    for i in range(int(tokens[1])):
                        h_coord.x += 1
                        move_tail(h_coord, t_coord)
                        t_coord_history.add(copy.copy(t_coord))
        
        print(len(t_coord_history))