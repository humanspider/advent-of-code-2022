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

def dir_to_delete(node: Node, min_size: int) -> tuple[str, int]:
    if not node.children or len(node.children) == 0:
        if node.size >= min_size:
            return (node.name, node.size)
        else:
            return None

    dir_list = []
    for child in node.children:
        dir = dir_to_delete(child, min_size)
        if dir:
            dir_list.append(dir)
    if node.size >= min_size:
        dir_list.append((node.name, node.size))
    
    try:
        return min(dir_list, key=lambda x:x[1])
    except (ValueError):
        return None

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
    
    print(dir_to_delete(root, 30000000-(70000000-root.size)))