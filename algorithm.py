import math
import time
import matplotlib.pyplot as plt
import numpy as np


def is_prime(n):
    return is_prime_sqrt_std(n)


def is_prime_sqrt_std(n):
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def generate_palindrome_from_half(left_half):
    left_part_str = str(left_half)

    # change = {'2': '3', '4': '7', '5': '7', '6': '7', '8': '9'}

    # if left_part_str[0] in change.keys():
    #     print("zamieniam")
    #     left_part_str = change[left_part_str[0]] + "0" * (len(left_part_str) -
    #                                                       1)

    full_str = left_part_str + left_part_str[::-1][1:]
    palindrome = int(full_str)

    return palindrome


def get_num_length(n):
    return math.floor(math.log10(n)) + 1


def get_left_half_num(n):
    n_str = str(n)
    half_length = math.ceil(len(n_str) / 2)
    return int(n_str[0:half_length])


def get_adjusted_left_half(left_half, N):
    if get_num_length(N) % 2 == 0:
        return 10**math.ceil(math.log10(N))
    elif generate_palindrome_from_half(left_half) <= N:
        return left_half + 1


def find_first_greater_prime_palindrome(N):
    # palindromes less than or equal to 11 should be considered
    # outside the main algorithm to simplify it
    palindromes = [2, 3, 5, 7, 11]
    for p in palindromes:
        if N < p:
            return p

    # forbidden = [2,4,5,6,8,0]
    # test = int(str(N)[0])
    # if test in forbidden:
    #     test+=1
    #     return find_first_greater_prime_palindrome(int(str(test) + "0" * (len(str(N))-1)))

    change = {'2': '3', '4': '7', '5': '7', '6': '7', '8': '9'}
    N_str = str(N)
    if N_str[0] in change.keys():
        N = int(change[N_str[0]] + "0" * (len(N_str) - 1))

    left_half = get_left_half_num(N)
    # every palindrome greater than 11 with even number of digits is divisable by 11
    # to skip generating palindromes with even number of digits
    # round left_half up to the nearest power of 10
    if get_num_length(N) % 2 == 0:
        left_half = 10**(math.floor(math.log10(left_half)) + 1)
    elif generate_palindrome_from_half(left_half) <= N:
        left_half += 1

    return find_prime_palindrome_from_half(left_half)


def find_prime_palindrome_from_half(left_half):
    while True:
        palindrome = generate_palindrome_from_half(left_half)

        if is_prime(palindrome):
            return palindrome

        left_half += 1

    return 0


def find_first_greater_prime_palindrome_brute(N):
    while True:
        N += 1
        if str(N) == str(N)[::-1] and is_prime(N):
            return N
    return 0
