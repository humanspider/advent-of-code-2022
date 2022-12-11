from parse import findall, search


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        stack_lines = []
        line = f.readline().rstrip('\n')
        while line != '':
            stack_lines.append(line)
            line = f.readline().rstrip('\n')
        
        n_stacks = sum(1 for _ in (i for i in findall('{:d}', stack_lines[-1])))
        stack_list = []
        for stack_n in range(n_stacks):
            stack_list.append([])
        for layer in stack_lines[-2::-1]:
            for stack_n in range(n_stacks):
                if layer[stack_n*4 + 1] != ' ':
                    stack_list[stack_n].append(layer[stack_n*4 + 1])
        
        line = f.readline().rstrip()
        while line != '':
            result = search('move {:d} from {:d} to {:d}', line)
            n_move = result[0]
            from_stack = result[1]-1
            to_stack = result[2]-1
            for i in range(n_move):
                stack_list[to_stack].append(stack_list[from_stack].pop())
            line = f.readline().rstrip()
        
        for i, stack in enumerate(stack_list):
            print(f"stack {i}: {stack}")
        
