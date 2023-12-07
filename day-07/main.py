
def part_one(input_file):
    from collections import Counter 
    with open(input_file, 'r') as data:
        hands = []
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            cards = line.split(' ')[0].replace('T', 'I').replace('K', 'L').replace('Q', 'K').replace('A', 'M')
            for i in range(2, 10):
                cards = cards.replace(str(i), chr(i + 63))
            rank = '1'
            c = Counter(cards)
            if c.most_common()[0][1] == 5:
                rank = '7'
            if c.most_common()[0][1] == 4:
                rank = '6'
            if c.most_common()[0][1] == 3:
                if c.most_common()[1][1] == 2:
                    rank = '5'
                else:
                    rank = '4'
            if c.most_common()[0][1] == 2:
                if c.most_common()[1][1] == 2:
                    rank = '3'
                else:
                    rank = '2'
            bid = int(line.split(' ')[1])
            hands.append({'type': rank, 'org': line.split(' ')[0], 'cards': cards, 'bid': bid})

        hands = sorted(hands, key=lambda x: x['cards'])
        hands = sorted(hands, key=lambda x: x['type'])
        total_winnings = 0
        for i, hand in enumerate(hands):
            total_winnings += (i + 1) * hand['bid']

    return total_winnings


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
