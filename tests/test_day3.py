import day3_puzzle1
import day3_puzzle2


# Puzzle 1
def test_closest_intersection():
    # Test case 1
    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    # Test case 2
    wire3 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire4 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

    assert day3_puzzle1.closest_intersection(wire1, wire2) == 159
    assert day3_puzzle1.closest_intersection(wire3, wire4) == 135


# Puzzle 2
def test_min_steps():
    # Test case 1
    wire1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    # Test case 2
    wire3 = ['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51']
    wire4 = ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']

    assert day3_puzzle2.min_steps(wire1, wire2) == 610
    assert day3_puzzle2.min_steps(wire3, wire4) == 410

