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
    sum_dist = 0
    right_list = []
    left_list = []
    for entry in entries:
        a, b = entry.split()
        right_list.append(int(a))
        left_list.append(int(b))

    right_list.sort()
    left_list.sort()

    for a, b in zip(right_list, left_list):
        sum_dist += abs(a-b)

    return sum_dist 

def part_2(entries: list[str]):
    right_list = []
    left_list = []
    for entry in entries:
        a, b = entry.split()
        right_list.append(int(a))
        left_list.append(int(b))
    
    freq = {} 
    for num in right_list:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    similarity = 0
    for num in left_list:
        if num not in freq:
            freq[num] = 0
        similarity += num*freq[num]

    return similarity

if __name__ == '__main__':
    main()
