import numpy as np


def read_masses(file):
    """Read input for masses of modules"""

    masses = []
    with open(file, 'r') as f:
        for mass in f:
            masses.append(float(mass.rstrip('2')))

    return masses


def total_fuel_req(file):
    """Calculate total fuel requirement based on masses"""
    masses = np.floor(np.asarray(read_masses(file), dtype=float) / 3) - 2
    return masses.sum()


#if __name__ == '__main__':
file_name = "inputs/day1_input.txt"
print("Total fuel requirement: ", total_fuel_req(file_name))
