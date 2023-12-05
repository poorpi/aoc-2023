
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
        def check_line(lines):
            def count_checks(checks):
                hit_count = 0
                if (checks[0][0] and checks[0][1] and checks[0][2]) or \
                   (checks[0][0] and checks[0][1]) or \
                   (checks[0][1] and checks[0][2]):
                    hit_count += 1
                    checks[0][0] = 0
                    checks[0][2] = 0
                elif checks[0][0] and checks[0][2]:
                    hit_count += 2
                elif checks[0][0] or checks[0][1] or checks[0][2]:
                    hit_count += 1
                hit_count += checks[1][0]
                hit_count += checks[1][2]
                if (checks[2][0] and checks[2][1] and checks[2][2]) or \
                   (checks[2][0] and checks[2][1]) or \
                   (checks[2][1] and checks[2][2]):
                    hit_count += 1
                    checks[2][0] = 0
                    checks[2][2] = 0
                elif checks[2][0] and checks[2][2]:
                    hit_count += 2
                elif checks[2][0] or checks[2][1] or checks[2][2]:
                    hit_count += 1
                return hit_count, checks

            def get_number(line, index):
                num = ''
                while (index > 0 and line[index].isdigit()):
                    index -= 1
                if not line[index].isdigit():
                    index += 1
                while (index < len(line) and line[index].isdigit()):
                    num += line[index]
                    index += 1
                return num

            line_gear_ratios = 0
            checks = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ]
            for i, c in enumerate(lines[1]):
                if c != '*':
                    continue

                checks = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0],
                ]

                if i > 0:
                    if lines[0][i-1].isdigit():
                        checks[0][0] = 1
                    if lines[1][i-1].isdigit():
                        checks[1][0] = 1
                    if lines[2][i-1].isdigit():
                        checks[2][0] = 1

                if lines[0][i].isdigit():
                    checks[0][1] = 1
                if lines[2][i].isdigit():
                    checks[2][1] = 1

                if i < len(lines[1]) - 1:
                    if lines[0][i+1].isdigit():
                        checks[0][2] = 1
                    if lines[1][i+1].isdigit():
                        checks[1][2] = 1
                    if lines[2][i+1].isdigit():
                        checks[2][2] = 1

                hit_count, checks = count_checks(checks)
                nums = []
                if hit_count != 2:
                    continue

                for ii in range(3):
                    for jj in range(3):
                        if checks[ii][jj]:
                            nums.append(get_number(lines[ii], i + (jj - 2 + 1)))
                line_gear_ratios += int(nums[0]) * int(nums[1])

            return line_gear_ratios

        lines = []
        line = data.readline().rstrip('\n')
        lines.append('.' * len(line))
        lines.append('.' * len(line))
        lines.append(line)

        gear_rations_total = 0
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            lines.pop(0)
            lines.append(line)

            gear_rations_total += check_line(lines)

        lines.pop(0)
        lines.append('.' * len(lines[0]))
        gear_rations_total += check_line(lines)
    return gear_rations_total


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
