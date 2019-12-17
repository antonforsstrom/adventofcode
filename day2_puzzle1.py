import csv
import numpy as np


def read_input(file):
    """Reads input for intcodes from file"""
    with open(file, 'r') as f:
        input_data = csv.reader(f, delimiter=',')
        input_data = [data for data in input_data][0]
        input_data = np.asarray(input_data, dtype=int)
    return input_data


def int_computer(file):
    """Executes optcode commands and updates intcode list read from file"""
    commands = read_input(file)
    # print(commands)

    # Restore input data to "1202 program alarm"
    # If statement for manual testing
    if file == 'day2_input.txt':
        commands[1] = 12
        commands[2] = 2

    index = 0
    print("Tot len: ", len(commands))
    while index < len(commands):
        command = commands[index]

        if command == 99:
            return commands

        value1 = commands[commands[index + 1]]
        value2 = commands[commands[index + 2]]
        pos = commands[index + 3]

        if command == 1:
            commands[pos] = value1 + value2
        elif command == 2:
            commands[pos] = value1 * value2
        else:
            print("Something went wrong. Unknown optcode.")

        index += 4

    return commands


if __name__ == '__main__':
    file = 'inputs/day2_input.txt'
    print("Answer: ", int_computer(file)[0])