
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
    def read_seeds(line):
        line = line.split(': ')[1]
        raw_seeds = [int(x) for x in line.split(' ')]
        seeds = []
        for i in range(0, len(raw_seeds), 2):
            seeds.append({'start': raw_seeds[i], 'end': raw_seeds[i] + raw_seeds[i + 1] - 1})
        return seeds

    def read_map(destination, lines):
        m = {'destination': destination, 'spans': []}
        for line in lines:
            line = [int(x) for x in line.split(' ')]
            m['spans'].append({'source_start': line[1], 'source_end': line[1] + line[2] - 1, 'offset': line[1] - line[0]})
        m['spans'] = sorted(m['spans'], key=lambda d: d['source_start'])
        return m

    def traverse_maps(maps, seed_range, map):
        locations = []

        if map == 'location':
            return [seed_range['start']]

        remaining_seed_range = seed_range
        for span in maps[map]['spans']:
            # seed whole before span - cont
            if remaining_seed_range['end'] < span['source_start']:
                continue
            # seed whole after span - cont
            if remaining_seed_range['start'] > span['source_end']:
                continue
            # seed whole in span - break
            if remaining_seed_range['start'] >= span['source_start'] and remaining_seed_range['end'] <= span['source_end']:
                locations += traverse_maps(maps, {'start': remaining_seed_range['start'] - span['offset'], 'end': remaining_seed_range['end'] - span['offset']}, maps[map]['destination'])
                remaining_seed_range = None
                break
            # seed ends in span - split
            if remaining_seed_range['end'] < span['source_end']:
                locations += traverse_maps(maps, {'start': span['source_start'] - span['offset'], 'end': remaining_seed_range['end'] - span['offset']}, maps[map]['destination'])
                remaining_seed_range['end'] = span['source_start'] - 1
                continue
            # seed starts in span - split
            if remaining_seed_range['start'] >= span['source_start']:
                locations += traverse_maps(maps, {'start': remaining_seed_range['start'] - span['offset'], 'end': span['source_end'] - span['offset']}, maps[map]['destination'])
                remaining_seed_range['start'] = span['source_end'] + 1
                continue
            # span inside seed - 2x split
            if span['source_start'] >= remaining_seed_range['start'] and span['source_end'] <= remaining_seed_range['end']:
                fitted_range = {'start': span['source_start'], 'end': span['source_end']}
                locations += traverse_maps(maps, {'start': fitted_range['start'] - span['offset'], 'end': fitted_range['end'] - span['offset']}, maps[map]['destination'])
                locations += traverse_maps(maps, {'start': remaining_seed_range['start'] - span['offset'], 'end': fitted_range['start'] - 1 - span['offset']}, map)
                locations += traverse_maps(maps, {'start': fitted_range['end'] + 1 - span['offset'], 'end': remaining_seed_range['end'] - span['offset']}, map)
                remaining_seed_range = None
                break
        if remaining_seed_range:
            locations += traverse_maps(maps, remaining_seed_range, maps[map]['destination'])
        return locations

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
        for seed_range in seeds:
            l = traverse_maps(maps, seed_range, 'seed')
            locations += l
    return min(locations)


if __name__ == '__main__':
    input_file = 'input.txt'
    results_file = 'results.txt'
    with open(results_file, 'w') as results:
        results.write('part 1 - {}\n'.format(part_one(input_file)))
        results.write('part 2 - {}\n'.format(part_two(input_file)))
