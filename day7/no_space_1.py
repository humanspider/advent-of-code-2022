from parse import search

class Node:
    def __init__(self, name, directory: bool, size=0):
        self.name = name
        if directory:
            self.children: list[Node] = []
        else:
            self.children = None

        self.size: int = size
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def calculate_size(node: Node) -> int:
    if not node.children or len(node.children) == 0:
        return node.size

    size: int = 0
    for child in node.children:
        size += calculate_size(child)
    
    node.size = size
    
    return size

cleanup_total = 0

def calc_cleanup_total(node: Node):
    global cleanup_total
    if node.size <= 100000 and node.children:
        cleanup_total += node.size

    if node.children:
        for child in node.children:
            calc_cleanup_total(child)


if __name__ == '__main__':
    root: Node = None
    with open('input.txt', 'r') as f:
        cur_node: Node = None

        line = f.readline().rstrip()
        tokens = line.split(' ')
        while len(tokens) != 0:
            if tokens[0] == '$':
                if tokens[1] == 'cd':
                    if tokens[2] == '/':
                        if not root:
                            root = Node('/', True)
                            root.parent = root
                        cur_node = root
                    elif tokens[2] == '..':
                        cur_node = cur_node.parent
                    else:
                        cur_node = next((child for child in cur_node.children if child.name == tokens[2]))
                elif tokens[1] == 'ls':
                    line = f.readline().rstrip()
                    tokens = line.split(' ')
                
                    while len(tokens) > 0 and tokens[0] != '' and tokens[0] != '$':
                        if tokens[0] == 'dir': 
                            child = Node(tokens[1], True)
                            cur_node.add_child(child)
                        elif tokens[0].isnumeric():
                            child = Node(tokens[1], False, int(tokens[0]))
                            cur_node.add_child(child)
                        line = f.readline().rstrip()
                        tokens = line.split(' ')
                    continue
            elif tokens[0] == '':
                break    
            else:
                raise Exception(f'Command could not be parsed: {tokens}')

            line = f.readline().rstrip()
            tokens = line.split(' ')
        
    # calculate dir sizes
    calculate_size(root)
    calc_cleanup_total(root)
    print(cleanup_total)
