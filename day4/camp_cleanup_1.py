from parse import search

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        contains_total = 0
        for line in f:
            line = line.rstrip()
            result = search('{:d}-{:d},{:d}-{:d}', line)
            assert result

            if (result[0] <= result[2] and result[1] >= result[3]) or \
                (result[2] <= result[0] and result[3] >= result[1]):
                contains_total += 1
        
        print(contains_total)
