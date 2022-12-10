from itertools import islice


if __name__ == '__main__':
    priority_sum = 0
    with open('input.txt', 'r') as f:
        while True:
            line_group = list(islice(f, 3))
            if not line_group:
                break
            rucksack_group = []
            for line in line_group:
                line = line.rstrip()
                rucksack_group.append(set([*line]))
            
            item_types = set.intersection(*rucksack_group)
            assert len(item_types) == 1
            item_type = list(item_types)[0]
            
            if ord('A') <= ord(item_type) <= ord('Z'):
                priority_sum += ord(item_type) - 38
            elif ord(item_type) <= ord('z'):
                priority_sum += ord(item_type) - 96
            else:
                raise Exception(f"Character:{item_type} is not alphabetical")

    print(priority_sum)