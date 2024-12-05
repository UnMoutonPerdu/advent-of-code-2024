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

def part_1(entries: list[str]):
    
    return 0

def part_2(entries: list[str]):
    
    return 0

if __name__ == '__main__':
    main()
