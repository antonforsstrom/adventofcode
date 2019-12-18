import day4


# Puzzle 1
def test_is_valid_pw_1():
    valid_pw = "111111"
    decr_pw = "223450"
    no_double = "123789"

    assert day4.is_valid_pw_1(valid_pw) == True
    assert day4.is_valid_pw_1(decr_pw) == False
    assert day4.is_valid_pw_1(no_double) == False


# Puzzle 2
def test_is_valid_pw_2():
    valid_pw_1 = "112233"
    invalid_pw = "123444"
    valid_pw_2 = "111122"

    assert day4.is_valid_pw_2(valid_pw_1) == True
    assert day4.is_valid_pw_2(invalid_pw) == False
    assert day4.is_valid_pw_2(valid_pw_2) == True
