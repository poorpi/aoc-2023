
def part_one(input_file):
    pipes = {
        '|': [(-1, 0), (1, 0)],
        '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)],
    }

    lines = []
    ix = 0;
    start_y = 0
    start_x = 0
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            lines.append(line)
            if 'S' in line:
                start_y = ix
                start_x = line.index('S')
            ix += 1

    x = None
    y = None

    last_x = None
    last_y = None

    length = 0
    while(not (x == start_x and y == start_y)):
        if not x:
            x = start_x
        if not y:
            y = start_y

        if lines[y][x] == 'S':
            last_x = x
            last_y = y
            if lines[y - 1][x] in '|7F':
                y = y - 1
            elif lines[y + 1][x] in '|LJ':
                y = y + 1
            elif lines[y][x - 1] in '-LF':
                x = x - 1
            else:
                x = x + 1
        else:
            pipe = pipes[lines[y][x]]
            if last_y == y + pipe[0][0] and last_x == x + pipe[0][1]:
                last_x = x
                last_y = y
                x = x + pipe[1][1]
                y = y + pipe[1][0]
            else:
                last_x = x
                last_y = y
                x = x + pipe[0][1]
                y = y + pipe[0][0]
        length += 1
    return int((length + 1) / 2)


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
