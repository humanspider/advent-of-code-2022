# Left column: A=rock, B=paper, C=scissors
# Right column: X=rock, Y=paper, Z=scissors
# Points: loss=0, draw=3, win=6; rock=1, paper=2, scissors=3
def get_score(your_play, opp_play):
    match your_play:
        case 'X':
            your_play = 'R'
        case 'Y':
            your_play = 'P'
        case 'Z':
            your_play = 'S'

    match opp_play:
        case 'A':
            opp_play = 'R'
        case 'B':
            opp_play = 'P'
        case 'C':
            opp_play = 'S'

    score = 0

    match your_play:
        case 'R':
            match opp_play:
                case 'R':
                    score += 3
                case 'P':
                    score += 0
                case 'S':
                    score += 6
            score += 1
        case 'P':
            match opp_play:
                case 'R':
                    score += 6
                case 'P':
                    score += 3
                case 'S':
                    score += 0
            score += 2
        case 'S':
            match opp_play:
                case 'R':
                    score += 0
                case 'P':
                    score += 6
                case 'S':
                    score += 3
            score += 3
    
    return score


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        total_score = 0
        for line in f:
            line = line.rstrip()
            letters = line.split()
            total_score += get_score(letters[1], letters[0])
        print(total_score)
