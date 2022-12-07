if __name__ == '__main__':
    top_cal = [0,0,0]
    cal_total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                top_cal.append(cal_total)
                top_cal.sort(reverse=True)
                top_cal.pop() # remove lowest value
                cal_total = 0
            else:
                cal_total += int(line)
        print('Reached end of input')
        print(f'Top 3 calorie counts: {top_cal}, totalling {sum(top_cal)}')
        