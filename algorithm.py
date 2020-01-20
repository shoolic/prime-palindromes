import math


def is_prime(n):
    return is_prime_sqrt_std(n)


def is_prime_sqrt_std(n):
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def generate_palindrome_from_half(left_half):
    left_half_str = str(left_half)

    # prevent mirroring left half if first digit is 2, 4, 5, 6, 8 (for sure it will not be prime)
    left_half_str = adjust_l_str_first_digit(left_half_str)

    full_str = left_half_str + left_half_str[::-1][1:]
    palindrome = int(full_str)

    return palindrome


def get_num_length(n):
    return math.floor(math.log10(n)) + 1


def get_left_half_num(n):
    n_str = str(n)
    half_length = math.ceil(len(n_str) / 2)
    return int(n_str[0:half_length])


def adjust_n_first_digit(N):
    change = {'2': '3', '4': '7', '5': '7', '6': '7', '8': '9'}
    N_str = str(N)
    if N_str[0] in change.keys():
        N = int(change[N_str[0]] + "0" * (len(N_str) - 1))

    return N


def adjust_l_str_first_digit(left_half_str):
    change = {'2': '3', '4': '7', '5': '7', '6': '7', '8': '9'}

    if left_half_str[0] in change.keys():
        left_half_str = change[left_half_str[0]] + left_half_str[1:]

    return left_half_str


def find_first_greater_prime_palindrome(N):
    # palindromes less than or equal to 11 should be considered
    # outside the main algorithm to simplify it
    palindromes = [2, 3, 5, 7, 11]
    for p in palindromes:
        if N < p:
            return p

    # prevent mirroring N if first digit is 2, 4, 5, 6, 8 (for sure it will not be prime)
    N = adjust_n_first_digit(N)

    # every palindrome greater than 11 with even number of digits is divisable by 11
    # to skip generating palindromes with even number of digits
    # round left_half up to the nearest power of 10
    left_half = get_left_half_num(N)

    if get_num_length(N) % 2 == 0:
        left_half = 10**(math.floor(math.log10(left_half)) + 1)
    # fix left half if it generates palindrome less than N
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
