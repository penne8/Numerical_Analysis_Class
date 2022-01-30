import math


def most_significant(num: int, digits_to_keep: int):
    """ return the digits_to_keep most significant digits of num
        return: (the kept digits, the number of non-significant (zeroedout) digits) """

    assert digits_to_keep > 0, 'digits_to_keep should be positive'
    num_digits = math.floor(math.log10(num)) + 1
    non_significant = max(0, num_digits - digits_to_keep)
    return (num // (10 ** non_significant)), non_significant


def special_adder(small_mantissa: int, small_exp: int, large_mantissa: int, large_exp: int):
    if small_exp > large_exp:
        # calculate c + acc
        # better to add larger (= acc) to smaller (= c)
        special_adder(large_mantissa, large_exp, small_mantissa, small_exp)

    # bring to the same exp
    diff_exp = large_exp - small_exp
    large_mantissa *= (10 ** diff_exp)
    new_mantissa, new_exp = most_significant(small_mantissa + large_mantissa, 3)
    new_exp += small_exp
    return new_mantissa, new_exp


def accumulator(n: int):
    acc_mantissa = 1
    acc_exp = -3
    c_mantissa = 4
    c_exp = -3
    for i in range(n):
        acc_mantissa, acc_exp = special_adder(acc_mantissa, acc_exp, c_mantissa, c_exp)

    return acc_mantissa * (10 ** acc_exp)


def print_num_and_error(n: int):
    acc = accumulator(n)
    print(f"approx for {n} itr: {acc}")
    real = round(0.001 + 0.004 * n, 5)
    print(f"real for {n} itr:   {real}")
    err = round(abs(real - acc), 5)
    print(f"absolute error at {n} itr = {err}")
    print("")
    return err


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("-------------a-------------")
    err_70 = print_num_and_error(70)
    err_7000 = print_num_and_error(7000)
    # --> the acc error grows as n grows because in this special_adder method with only 3 significant digits,
    # --> we get that the number wont pass the value 1, because 1*(10^0) + 4*(10^-3) = 1 + 0 = 1

    print("-------------b-------------")
    err_72 = print_num_and_error(72)
    err_8000 = print_num_and_error(8000)
    err_8002 = print_num_and_error(8002)

    diff_70_72 = round(abs(err_70 - err_72), 5)
    print(f"the error difference between 70 itr and 72 itr = {diff_70_72}")
    diff_8000_8002 = round(abs(err_8000 - err_8002), 5)
    print(f"the error difference between 8000 itr and 8002 itr = {diff_8000_8002}")
    # --> the error difference is differ a lot because the acc error grows over time as n grows,
    # --> as explainec in the previous section