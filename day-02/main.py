
def part_one(input_file):
    limits = {'red': 12, 'green': 13, 'blue': 14}
    ids_sum = 0

    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            s = line.split(': ')
            id = s[0].split(' ')[1]
            limit_exceeded = False
            for game in s[1].split('; '):
                for count in game.split(', '):
                    amount = count.split(' ')[0]
                    color = count.split(' ')[1]
                    if limits[color] < int(amount):
                        limit_exceeded = True
                        break
                if limit_exceeded:
                    break
            if not limit_exceeded:
                ids_sum += int(id)
    return ids_sum


def part_two(input_file):
    with open(input_file, 'r') as data:
        pass

    return


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
