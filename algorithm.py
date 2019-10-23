import math

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


def main():
    N = int(input())
    digits = str(N)

    left_part_str = digits[0: math.ceil(len(digits) / 2)]
    left_part_num = int(left_part_str)

    if len(digits) % 2 == 0:
        left_part_num = 10 ** (math.floor(math.log10(left_part_num)) + 1)

    while True:
        left_part_str = str(left_part_num)
        full_str = left_part_str + left_part_str[::-1][1:]
        full_num = int(full_str)

        if full_num > N and is_prime(full_num):
            print (full_num)
            return 0
    
        left_part_num += 1

        if left_part_num % 10 == 0 :
            left_part_num *= 10


if __name__ == "__main__":
    main()
