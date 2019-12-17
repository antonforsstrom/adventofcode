import numpy as np
from day1_puzzle1 import read_masses


def rec_fuel_req(mass):
    """Calculates total fuel required for a module with mass <mass>"""
    total_fuel_mass = np.floor(float(mass) / 3) - 2
    temp_fuel_mass = total_fuel_mass

    while temp_fuel_mass > 0:
        temp_fuel_mass = np.floor(float(temp_fuel_mass) / 3) - 2

        if temp_fuel_mass <= 0:
            temp_fuel_mass = 0

        total_fuel_mass += temp_fuel_mass

    return total_fuel_mass


def total_rec_fuel_req(file_name):
    masses = read_masses(file_name)
    total_fuel_req = list(map(rec_fuel_req, masses))
    total_fuel_req = np.asarray(total_fuel_req)
    return total_fuel_req.sum()


if __name__ == '__main__':
    file_name = 'inputs/day1_input.txt'
    print(total_rec_fuel_req(file_name))