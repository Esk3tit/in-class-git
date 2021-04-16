def calc(a, b):
    sum = a + b
    # print(sum)
    diff = a - b
    mult = a * b
    div = a / b
    print_calc(sum, diff, mult, div)


def print_calc(sum, diff, mult, div):
    print(f"{sum}")
    print(f"{diff}")
    print(f"{mult}")
    print(f"{div}")


# Test code
calc(3, 4)
