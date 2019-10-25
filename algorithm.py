import math
import time
import matplotlib.pyplot as plt


def is_prime(n):
    return is_prime_sqrt_std(n)


def is_prime_sqrt_std(n):
    for i in range(2, round(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def generate_palindrome_from_half(left_half):
    left_part_str = str(left_half)
    full_str = left_part_str + left_part_str[::-1][1:]
    palindrome = int(full_str)

    return palindrome

def get_num_length(n):
    return math.ceil(math.log10(n))

def get_left_half_num(n):
    n_str = str(n)
    half_length =  math.ceil(len(n_str) / 2)
    return int(n_str[0: half_length])


def get_adjusted_left_half(left_half, N):
    if get_num_length(N) % 2 == 0:
        return 10 ** math.ceil(math.log10(N))
    elif generate_palindrome_from_half(left_half) <= N:
        return left_half + 1


def find_first_greater_prime_palindrome(N):
    # palindromes less than or equal to 11 should be considered 
    # outside the main algorithm to simplify it
    palindromes = [2, 3, 5, 7, 11]
    for p in palindromes:
        if N < p:
            return p

    left_half = get_left_half_num(N)

    # every palindrome greater than 11 with even number of digits is divisable by 11
    # to skip generating palindromes with even number of digits 
    # round left_half up to the nearest power of 10
    if get_num_length(N) % 2 == 0:
        left_half = 10 ** math.ceil(math.log10(N))
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

def measure_time_brute(N_arr, reapeats):
    avg_times = []

    for N in N_arr:
        avg_time = 0

        for _ in range(0, reapeats):
            start = time.process_time_ns()
            find_first_greater_prime_palindrome_brute(N)
            avg_time += time.process_time_ns() - start

        avg_time /= reapeats
        avg_times.append(avg_time)

    return avg_times
        
def measure_time(N_arr, reapeats):
    avg_times = []

    for N in N_arr:
        print("normal", N_arr)
        avg_time = 0

        for _ in range(0, reapeats):
            start = time.process_time_ns()
            find_first_greater_prime_palindrome(N)
            avg_time += time.process_time_ns() - start

        avg_time /= reapeats
        avg_times.append(avg_time)

    return avg_times

def main():
    N = int(input())
    print(find_first_greater_prime_palindrome(N))
    # x = range(10 ** 5,  10 ** 7, 10 ** 4)
    # x = [10 ** 4, 10 ** 5, 10 ** 6, 10 ** 7, 10 ** 8]

    # y = measure_time(x, 3)
    # y_b = measure_time_brute(x, 3)
    # plt.plot(x, y_b, 'r')
    # plt.plot(x, y, 'g')
    # plt.ylabel('time [ns]')
    # plt.xlabel('n')
    # plt.savefig("compare_big.png")


if __name__ == "__main__":
    main()
