if __name__ == '__main__':
    priority_sum = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            left = []
            right = []
            i = 0
            while i < len(line)/2 :
                left.append(line[i])
                i +=1
            left = set(left)
            while i < len(line):
                right.append(line[i])
                i+=1
            right = set(right)

            intersect = left.intersection(right)
            assert len(intersect) == 1
            item_type = list(intersect)[0]
            
            if ord('A') <= ord(item_type) <= ord('Z'):
                priority_sum += ord(item_type) - 38
            elif ord(item_type) <= ord('z'):
                priority_sum += ord(item_type) - 96
            else:
                raise Exception(f"Character:{item_type} is not alphabetical")

    print(priority_sum)