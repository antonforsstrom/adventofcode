from day2_puzzle1 import read_input


def int_computer(noun, verb):
    """Executes optcode commands and updates intcode list read from file"""
    file = 'inputs/day2_input.txt'
    commands = read_input(file)
    commands[1] = noun
    commands[2] = verb

    # print(commands[:12])

    index = 0
    length = len(commands)

    try:
        while index < length:
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
                # print("Something went wrong. Unknown optcode.")
                pass

            index += 4

        return commands
    except IndexError:
        return [0]


if __name__ == '__main__':
    for i in range(0, 100):
        for j in range(0, 100):
            n = i
            v = j
            goal = int_computer(n, v)[0]
            #print(goal)
            if goal == 19690720:
                print("Noun: ", n)
                print("Verb: ", v)
                print("Answer: ", 100 * n + v)
                break
