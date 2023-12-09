
def part_one(input_file):
    extrapolated_sum = 0
    with open(input_file, 'r') as data:
        while True:
            line = data.readline()
            if not line:
                break
            line = line.rstrip('\n')
            numbers = [int(x) for x in line.split()]
            stage_lasts = []
            stage_lasts.append(numbers[-1])
            current_numbers = numbers
            while True:
                all_zeros = True
                new_numbers = []
                for ix in range(len(current_numbers) - 1):
                    new_numbers.append(current_numbers[ix + 1] - current_numbers[ix])
                    if new_numbers[-1]:
                        all_zeros = False
                if all_zeros:
                    break
                stage_lasts.append(new_numbers[-1])
                current_numbers = new_numbers
            stage_lasts.reverse()
            extrapolated = 0
            for stage_last in stage_lasts:
                extrapolated = extrapolated + stage_last
            extrapolated_sum += extrapolated

    return extrapolated_sum


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
