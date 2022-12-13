if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        processed = 0
        marker = []
        chars = f.read(14)
        marker = [c for c in chars]
        if len(set(marker)) == len(marker):
            print(14)
            exit(0)
        processed += 14
        
        char = f.read(1)
        processed += 1
        while char != '':
            del(marker[0])
            marker.append(char)
            if len(set(marker)) == len(marker):
                print(processed)
                exit(0)
            char = f.read(1)
            processed += 1
        print("EOF reached: no marker found")
