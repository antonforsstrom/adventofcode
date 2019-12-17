import day3_puzzle1


def steps(wire1, wire2):
    """Calculates most time efficient intersection, i.e. the one reached with the least total steps from origin"""
    points1= day3_puzzle1.get_visited_points(wire1)
    points2 = day3_puzzle1.get_visited_points(wire2)
    intersections = day3_puzzle1.intersections(points1, points2)

    # Number of steps required to get to each intersection
    numbr_steps = []
    for intersection in intersections:

        # Correct for 0-indexing
        steps_wire1 = points1.index(intersection) + 1
        steps_wire2 = points2.index(intersection) + 1

        total_steps = steps_wire1 + steps_wire2

        numbr_steps.append(total_steps)

    return numbr_steps


def min_steps(wire1: list, wire2: list):
    steps_list = steps(wire1, wire2)
    min_steps_list = min(steps_list)

    return min_steps_list


if __name__ == "__main__":
    filename = 'inputs/day3_input.txt'
    wires = day3_puzzle1.read_input(filename)
    print("Min distance: ", min_steps(wires[0], wires[1]))
