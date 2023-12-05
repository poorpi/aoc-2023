
def part_one(input_file):
    with open(input_file, 'r') as data:
        def check_line(lines):
            line_parts_total = 0
            current_part = ''
            current_part_good = False
            for i, c in enumerate(lines[1]):
                if not c.isdigit():
                    if current_part_good:
                        line_parts_total += int(current_part)
                    current_part_good = False
                    current_part = ''
                    continue
                if c.isdigit():
                    current_part += c
                    if current_part_good:
                        continue

                if i > 0:
                    if not lines[0][i-1].isdigit() and lines[0][i-1] != '.' or \
                       not lines[1][i-1].isdigit() and lines[1][i-1] != '.' or \
                       not lines[2][i-1].isdigit() and lines[2][i-1] != '.':
                        current_part_good = True
                        continue

                if not lines[0][i].isdigit() and lines[0][i] != '.' or \
                   not lines[2][i].isdigit() and lines[2][i] != '.':
                    current_part_good = True
                    continue

                if i < len(lines[1]) - 1:
                    if not lines[0][i+1].isdigit() and lines[0][i+1] != '.' or \
                       not lines[1][i+1].isdigit() and lines[1][i+1] != '.' or \
                       not lines[2][i+1].isdigit() and lines[2][i+1] != '.':
                        current_part_good = True
                        continue

            if current_part_good:
                line_parts_total += int(current_part)
            return line_parts_total

        lines = []
        line = data.readline().rstrip('\n')
        lines.append('.' * len(line))
        lines.append('.' * len(line))
        lines.append(line)

        parts_total = 0
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            lines.pop(0)
            lines.append(line)

            parts_total += check_line(lines)

        lines.pop(0)
        lines.append('.' * len(lines[0]))
        parts_total += check_line(lines)
    return parts_total


def part_two(input_file):
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')

    return


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
