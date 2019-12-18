def is_valid_pw_1(pw):
    """
    Rules for a valid pw:
    - It is a six-digit number.
    - The value is within the range given in your puzzle input.
    - Two adjacent digits are the same (like 22 in 122345).
    - Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    pw = str(pw)
    if check_adj_digits(pw) and check_incr_digits(pw):
        return True
    return False


def is_valid_pw_2(pw):
    """
    Rules for a valid pw:
    - It is a six-digit number.
    - The value is within the range given in your puzzle input.
    - Two adjacent digits are the same (like 22 in 122345), BUT not part of larger group of matching digits.
    - Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    """
    pw = str(pw)
    if check_incr_digits(pw) and check_max_two_adj_digits(pw):
        return True

    return False


def check_adj_digits(pw):
    for i in range(1, len(pw)):
        if pw[i-1] == pw[i]:
            return True

    return False


def check_incr_digits(pw):
    for i in range(1, len(pw)):
        if pw[i] < pw[i-1]:
            return False

    return True


def check_max_two_adj_digits(pw):
    count_occur = {}

    for i in range(1, len(pw)):
        if pw[i-1] == pw[i]:
            if pw[i] in count_occur:
                count_occur[pw[i]] += 1
            else:
                count_occur[pw[i]] = 1

    for val in count_occur.values():
        if val == 1:
            return True

    return False


def count_valid_pws(pw_scope):
    pw_counter_1 = 0
    pw_counter_2 = 0

    for pw in range(pw_scope[0], pw_scope[1] + 1):
        if is_valid_pw_1(pw):
            pw_counter_1 += 1
        if is_valid_pw_2(pw):
            pw_counter_2 += 1

    return pw_counter_1, pw_counter_2


if __name__ == "__main__":
    input_range = [271973, 785961]
    answ1, answ2 = count_valid_pws(input_range)
    print("Puzzle 1: ", answ1)
    print("Puzzle 2: ", answ2)



