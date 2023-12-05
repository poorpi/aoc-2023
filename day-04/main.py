
def part_one(input_file):
    total_points = 0
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            line = line.replace('  ', ' ')
            line = line.split(': ')[1]
            line = line.split(' | ')
            winning = [int(x) for x in line[0].split(' ')]
            current = [int(x) for x in line[1].split(' ')]
            matches = set(winning) & set(current)
            if len(matches) > 0:
                total_points += pow(2, len(matches) - 1)
    return total_points


def part_two(input_file):
    cards = {}
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            line = line.replace('  ', ' ')
            line = line.split('Card ')[1]
            card_num = int(line.split(':')[0])
            line = line.split(': ')[1]
            line = line.split(' | ')
            winning = [int(x) for x in line[0].split(' ')]
            current = [int(x) for x in line[1].split(' ')]
            cards[card_num] = {'count': 1, 'winning': winning, 'current': current}

    for k, v in cards.items():
        matches = set(v['winning']) & set(v['current'])
        for i in range(len(matches)):
            if k + i + 1 in cards:
                cards[k + i + 1]['count'] += v['count']

    return sum(card['count'] for card in cards.values())


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
