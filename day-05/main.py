
def part_one(input_file):
    def read_seeds(line):
        seeds = []
        line = line.split(': ')[1]
        seeds = [int(x) for x in line.split(' ')]
        return seeds

    def read_map(destination, lines):
        m = {'destination': destination, 'spans': []}
        for line in lines:
            line = [int(x) for x in line.split(' ')]
            m['spans'].append({'destination_start': line[0], 'source_start': line[1], 'range': line[2]})
        return m

    with open(input_file, 'r') as data:
        line = data.readline().rstrip('\n')
        seeds = read_seeds(line)
        data.readline()

        maps = {}
        source = ''
        destination = ''
        lines = []
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            if not line:
                if source and destination and lines:
                    maps[source] = read_map(destination, lines)
                    source = ''
                    destination = ''
                    lines = []
                continue
            if not source and not destination:
                source = line.split('-to-')[0]
                destination = line.split('-to-')[1].split(' ')[0]
                continue
            lines.append(line)

        if source and destination and lines:
            maps[source] = read_map(destination, lines)
            source = ''
            destination = ''
            lines = []

        locations = []
        for seed_value in seeds:
            current_value = seed_value
            current_map = 'seed'
            while current_map != 'location':
                for span in maps[current_map]['spans']:
                    if current_value >= span['source_start'] and current_value < span['source_start'] + span['range']:
                        current_value = span['destination_start'] + current_value - span['source_start']
                        break
                current_map = maps[current_map]['destination']
            locations.append(current_value)

    return min(locations)


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
