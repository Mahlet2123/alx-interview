#!/usr/bin/python3
""" 0-minoperations module """


def minOperations(n):
    """ Computes the fewest number of operations needed to result
    in exactly n H characters. """
    if n <= 1:
        return 0

    operations = 0
    factor = 2  # Start with the first prime factor

    while n > 1:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
