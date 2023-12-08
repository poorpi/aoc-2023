
def part_one(input_file):
    with open(input_file, 'r') as data:
        instructions = data.readline().rstrip('\n')
        data.readline()
        nodes = {}
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            node_name = line.split(' = ')[0]
            directions = line.split(' = ')[1].strip('()')
            nodes[node_name] = {'name': node_name, 'L': directions.split(', ')[0], 'R': directions.split(', ')[1]}
    
    end_node_name = 'ZZZ'
    end_reached = False
    steps = 0
    current_node = nodes['AAA']
    while not end_reached:
        for instruction in instructions:
            current_node = nodes[current_node[instruction]]
            steps += 1
            if current_node['name'] == end_node_name:
                end_reached = True
                break
    return steps


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
