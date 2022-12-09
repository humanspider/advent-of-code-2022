def get_score(opp_play, outcome):
    match opp_play:
        case 'A':
            opp_play = 'R'
        case 'B':
            opp_play = 'P'
        case 'C':
            opp_play = 'S'
    
    score = 0
    # Points: loss=0, draw=3, win=6; rock=1, paper=2, scissors=3
    match outcome:
        case 'X':
            match opp_play:
                case 'R':
                    score += 3
                case 'P':
                    score += 1
                case 'S':
                    score += 2
            score += 0
        case 'Y':
            match opp_play:
                case 'R':
                    score += 1
                case 'P':
                    score += 2
                case 'S':
                    score += 3
            score += 3
        case 'Z':
            match opp_play:
                case 'R':
                    score += 2
                case 'P':
                    score += 3
                case 'S':
                    score += 1
            score += 6
    
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        total_score = 0
        for line in f:
            line = line.rstrip()
            letters = line.split()
            total_score += get_score(letters[0], letters[1])
        print(total_score)
