
def part_one(input_file):
    with open(input_file, 'r') as data:
        def distance(time, speed):
            return time * speed

        times = [int(x) for x in data.readline().split(':')[1].split()]
        distances = [int(x) for x in data.readline().split(':')[1].split()]

        total_wins_mul = 1
        for race in range(len(times)):
            num_wins = 0
            for i in range(times[race]):
                if distance(times[race] - i, i) > distances[race]:
                    num_wins += 1
            total_wins_mul *= num_wins
    return total_wins_mul


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
