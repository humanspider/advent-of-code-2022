if __name__ == '__main__':
    max_cal_total = 0
    cal_total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                if cal_total > max_cal_total:
                    max_cal_total = cal_total
                cal_total = 0
            else:
                cal_total += int(line)
        print('Reached end of input')
        print(f'Max calories: {max_cal_total}')
        