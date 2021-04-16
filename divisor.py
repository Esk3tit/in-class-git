import math

def divisor(n):

    divisor_list = list()

    # We because the range is exclusive on the maximum value,
    # we end at sqrt(n) + 1 to include sqrt(n)
    for i in range(1, int(math.sqrt(n) + 1)):

        if n % i == 0:

            # If there is no remainder, then i is divisor
            # Add to divisor list
            divisor_list.append(i)


def print_divisor(lst):

    # Print divisor list
    for div in lst:
        print(f"{div} ")