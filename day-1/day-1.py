
def part_one():
    input_file = 'input.txt'
    first_digit = ''
    last_digit = ''
    total = 0
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            for i in range(len(line)):
                if line[i].isdigit() and not first_digit:
                    first_digit = line[i]
                if line[-1-i].isdigit() and not last_digit:
                    last_digit = line[-1-i]
                if first_digit and last_digit:
                    break

            total += int(first_digit + last_digit)
            first_digit = ''
            last_digit = ''
    return total


if __name__ == '__main__':
    print('part one calibration total : {}'.format(part_one()))
