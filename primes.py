"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

def checkPrime(number):
    isPrime = True
    for y in range(2, int(math.sqrt(number) + 1)):
        if number % y == 0:
            isPrime = False
            break
    return isPrime


def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("number of primes needs to be greater than 0")
    list = []
    list.append(2)
    number = 3
    while len(list) < number_of_primes:
        if checkPrime(number):
            list.append(number)
        number += 1
    return list
primes(3)



