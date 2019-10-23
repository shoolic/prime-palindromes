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


def find_first_greater_prime_palindrome_brute(N):
    while True:
       N += 1
       if str(N) == str(N)[::-1] and is_prime(N):
            return N
    return 0

def main():
    # N = int(input())
    # print(find_first_greater_prime_palindrome(N))
    n = 1
    while n < 10 ** 50:   
        avg = 0
        for c in range(1,10):
            start = time.process_time_ns()
            left_part_str = str(n)
            full_str = left_part_str + left_part_str[::-1][1:]
            palindrome = int(full_str)
            avg =+ (time.process_time_ns() - start)
        print(avg/10)
        n *= 10


if __name__ == "__main__":
    main()
