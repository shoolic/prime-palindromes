import math
import time

def is_prime(x):
    for i in range(2, round(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

def gen_palindrome_from_half(left_part_num, odd_digits):
        left_part_str = str(left_part_num)
        full_str = left_part_str + left_part_str[::-1][odd_digits:]
        palindrome = int(full_str)
        return palindrome

def find_first_greater_prime_palindrome(N):
    digits = str(N)

    left_part_str = digits[0: math.ceil(len(digits) / 2)]
    left_part_num = int(left_part_str)

    odd_digits = len(digits) % 2
    more_digits_checker = 10 ** len(left_part_str)

    while True:
        palindrome = gen_palindrome_from_half(left_part_num, odd_digits)

        if palindrome > N and is_prime(palindrome):
            return palindrome
    
        left_part_num += 1

        if left_part_num % more_digits_checker == 0:
            if odd_digits == 1:
                left_part_num = int(left_part_num / 10) 
                odd_digits = 0
            else:
                more_digits_checker *= 10
                odd_digits = 1
    return 0

def find_first_greater_prime_palindrome2(N):
    palindromes = [2, 2, 3, 5, 5, 7, 7, 11, 11, 11, 11]
    if N < 11:
        return palindromes[N]

    digits = str(N)

    left_part_str = digits[0: math.ceil(len(digits) / 2)]
    left_part_num = int(left_part_str)
    
    right_part_str = digits[-math.ceil(len(digits) / 2):]
    right_part_num = int(right_part_str)

    if right_part_num > left_part_num:
        left_part_num += 1

    if len(digits) % 2 == 0:
        left_part_num = 10 ** (math.floor(math.log10(left_part_num)) + 1)

    while True:
        palindrome = gen_palindrome_from_half(left_part_num, 1)

        if palindrome > N and is_prime(palindrome):
            return palindrome
    
        left_part_num += 1

    return 0

def find_first_greater_prime_palindrome_brute(N):
    while True:
       N += 1
       if str(N) == str(N)[::-1] and is_prime(N):
            return N
    return 0

def main():
    # N = int(input())
    # print(find_first_greater_prime_palindrome(N))
    for N in range(1, 10 ** 5):
        p1 = find_first_greater_prime_palindrome2(N)
        p2 =  find_first_greater_prime_palindrome_brute(N)
        if p1 != p2:
            print(N, p1, p2)


if __name__ == "__main__":
    main()
