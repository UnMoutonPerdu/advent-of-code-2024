from argparse import ArgumentParser
import re

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
    string_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    regex_pattern = re.compile(string_pattern)
    sum = 0
    
    for entry in entries:
        result = regex_pattern.findall(entry)
        for tup in result:
            a, b = tup
            sum += int(a) * int(b)
    
    return sum

def part_2(entries: list[str]):
    # Define the pattern for regex
    string_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    regex_pattern = re.compile(string_pattern)
    sum = 0

    # Define this boolean, will be useful between two entries to know if the first mul(X,Y) pattern has to be compute or not 
    # False if the previous entry ended with a "don't()" instruction
    enable = True

    for entry in entries:
        # We split each entry with "do()" instruction to get substring where mul(X,Y) will be potentially computed
        do_instr = entry.split("do()")
        for i in range(len(do_instr)):
            # Check if the previous entry ended with a "don't()" instruction
            if i == 0 and not enable:
                enable = True
                continue
            # We split each substring where "do()" is applied with "don't()" instruction and we only take the first substring resulting of the splitting
            # This is the only possible instruction where mul(X,Y) is interesting
            dont_instr = do_instr[i].split("don't()")
            possible_inst = dont_instr[0]
            if possible_inst == '':
                continue 
            # As before, check for the mul(X,Y) pattern
            result = regex_pattern.findall(possible_inst)
            for tup in result:
                a, b = tup
                sum += int(a) * int(b)
            # Modify the boolean enable if the last instruction was a "don't()" one
            if i == len(do_instr)-1 and len(dont_instr) > 1:
                enable = False 

    return sum

if __name__ == '__main__':
    main()
