"""
Write a function which reduces fractions to their simplest form! Fractions will be presented as an array/tuple 
(depending on the language) of strictly positive integers, and the reduced fraction must be returned as an array/tuple:

    input:   [numerator, denominator]
    output:  [reduced numerator, reduced denominator]
    example: [45, 120] --> [3, 8]
All numerators and denominators will be positive integers.

Note: This is an introductory Kata for a series... coming soon!

"""

def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)

def reduce_fraction(fraction):
    numerator, denominator = fraction
    gcd = get_gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)