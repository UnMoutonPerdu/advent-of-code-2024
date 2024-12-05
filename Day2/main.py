from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('-s', '--sol', action='store_true', help='Get solution for both part')
    args = parser.parse_args()
    entries = []
    with open(args.input_file, 'r') as file:
        for line in file:
            entries.append(line)

    print(f'Solution 1: {part_1(entries)}')
    print(f'Solution 2: {part_2(entries)}')

    return sum

def is_safe(levels: list[int]):
    increasing = True if levels[0] < levels[1] else False
    for i in range(len(levels)-1):
        if levels[i] == levels[i+1]:
            return False
        if not (increasing ^ (levels[i] < levels[i+1])):
            if abs(levels[i] - levels[i+1]) > 3:
                return False 
        else:
            return False 

    return True

def part_1(entries: list[str]):
    num_safe = 0
    for entry in entries:
        levels = list(map(int, entry.split()))
        num_safe += is_safe(levels)

    return num_safe

def is_safe2(levels: list[int]):
    if is_safe(levels[1:]):
        return True
    increasing = True if levels[0] < levels[1] else False
    for i in range(len(levels)-1):
        if levels[i] == levels[i+1]:
            return is_safe(levels[:i] + levels[i+1:])
        if not (increasing ^ (levels[i] < levels[i+1])):
            if abs(levels[i] - levels[i+1]) > 3:
                return True if is_safe(levels[:i] + levels[i+1:]) + is_safe(levels[:i+1] + levels[i+2:]) > 0 else False      
        else:
            return True if is_safe(levels[:i] + levels[i+1:]) + is_safe(levels[:i+1] + levels[i+2:]) > 0 else False      
    return True

def part_2(entries: list[str]):
    num_safe = 0
    for entry in entries:
        levels = list(map(int, entry.split()))
        num_safe += is_safe2(levels)

    return num_safe



if __name__ == '__main__':
    main()
