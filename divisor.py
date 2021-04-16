import math

def divisor(n):

    divisor_list = list()

    # Simple divisor that iterates up to n
    # Not super efficient but gets the job done
    for i in range(1, n + 1):

        if n % i == 0:

            # If there is no remainder, then i is divisor
            # Add to divisor list
            divisor_list.append(i)

    return divisor_list


def print_divisor(lst):

    # Print divisor list
    for div in lst:
        print(f"{div} ")


# Test run code
div_list = divisor(100)
print_divisor(div_list)