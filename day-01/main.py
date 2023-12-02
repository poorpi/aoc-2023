
def part_one(input_file):
    def digit(s):
        return s if s.isdigit() else ''

    first_digit = ''
    last_digit = ''
    total = 0
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            for i in range(len(line)):
                if not first_digit:
                    first_digit = digit(line[i])
                if not last_digit:
                    last_digit = digit(line[-1-i])
                if first_digit and last_digit:
                    break

            total += int(first_digit + last_digit)
            first_digit = ''
            last_digit = ''

    return total


def part_two(input_file):
    def digit(s):
        return s if s.isdigit() else ''

    def build_str_digit_dict():
        str_digits = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                      'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        str_digit_dict = {}
        for str_digit, value in str_digits.items():
            current = str_digit_dict
            for c in str_digit:
                if ord(c) not in current:
                    current[ord(c)] = {}
                current = current[ord(c)]
            current['value'] = value
        return str_digit_dict

    def str_digit_value(str_digit_dict, s):
        current = str_digit_dict
        for c in s:
            if current.get('value', ''):
                return current['value']
            if ord(c) in current:
                current = current[ord(c)]
                continue
            return ''
        return current.get('value', '')

    str_digit_dict = build_str_digit_dict()
    first_digit = ''
    last_digit = ''
    total = 0

    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            for i in range(len(line)):
                if not first_digit:
                    first_digit = digit(line[i])
                    if not first_digit:
                        first_digit = str_digit_value(str_digit_dict, line[i:])
                if not last_digit:
                    last_digit = digit(line[-1-i])
                    if not last_digit:
                        for x in range(2, 5):
                            sub = line[-1-i-x:]
                            for ii in range(len(sub)):
                                if line[-1-ii].isdigit():
                                    last_digit = line[-1-ii]
                            if str_digit_value(str_digit_dict, sub):
                                last_digit = str_digit_value(str_digit_dict, sub)
                                break
                if first_digit and last_digit:
                    break
            total += int(first_digit + last_digit)
            first_digit = ''
            last_digit = ''
    return total


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
