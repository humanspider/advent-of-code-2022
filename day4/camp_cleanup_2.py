from parse import search

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        contains_total = 0
        for line in f:
            line = line.rstrip()
            result = search('{:d}-{:d},{:d}-{:d}', line)
            assert result
            # 2-4,7-9
            if not (result[1] < result[2]  or result[0] > result[3]):
                contains_total += 1
        
        print(contains_total)
