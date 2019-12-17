import csv
import numpy as np


def read_input(file):
    """Reads input from file"""
    with open(file, 'r') as f:
        input_data = csv.reader(f, delimiter=',')
        input_data = [data for data in input_data]
    return input_data


def get_visited_points(wire):
    """Creates list with all x,y points passed

    :param wire: instructions for wire routing

    :returns: list of points representing coordinates for wire edges
    """

    # Divide wire routing instructions into direction and distance
    directions = []
    distances = []

    for command in wire:
        directions.append(command[0])
        distances.append(int(command[1:]))

    # print(directions)
    # print(distances)

    # Starting point (0, 0)
    x = y = 0
    visited_points = []

    # Append visited edges
    for direct, dist in zip(directions, distances):
        if direct == 'R':
            for i in range(1, dist + 1):
                x += 1
                visited_points.append((x, y))
        elif direct == 'L':
            for i in range(1, dist + 1):
                x -= 1
                visited_points.append((x, y))
        elif direct == 'U':
            for i in range(1, dist + 1):
                y += 1
                visited_points.append((x, y))
        elif direct == 'D':
            for i in range(1, dist + 1):
                y -= 1
                visited_points.append((x, y))

        visited_points.append((x, y))

    return visited_points


def intersections(wire1_points: list, wire2_points: list):
    """Compares two wires and identifies intersection points

    :param wire1_points: points visited by wire1
    :param wire2_points: points visted by wire2

    :returns: list of instersection points for the two wires
    """

    intersects = list(set(wire1_points).intersection(set(wire2_points)))

    return intersects


def manh_distance(intersects):
    """Calculates manhattan distance of intersection points to central port

    :param intersects: list of intersection points

    :returns: list of manhattan distance per point
    """
    distances = [abs(point[0]) + abs(point[1]) for point in intersects]
    return distances


def closest_intersection(wire1, wire2):
    """Calculates manhattan distance for the intersection points of two wires, to the central port """
    points1 = get_visited_points(wire1)
    points2 = get_visited_points(wire2)
    intersects = intersections(points1, points2)
    shortest_manh_dist = np.amin(np.asarray(manh_distance(intersects)))

    return shortest_manh_dist


if __name__ == "__main__":
    file = 'inputs/day3_input.txt'
    wires = read_input(file)
    print("Min distance: ", closest_intersection(wires[0], wires[1]))
