import algorithm

assert algorithm.find_first_greater_prime_palindrome(1) == 2

assert algorithm.find_first_greater_prime_palindrome(2) == 3

assert algorithm.find_first_greater_prime_palindrome(3) == 5
assert algorithm.find_first_greater_prime_palindrome(4) == 5

assert algorithm.find_first_greater_prime_palindrome(5) == 7
assert algorithm.find_first_greater_prime_palindrome(6) == 7

assert algorithm.find_first_greater_prime_palindrome(7) == 11
assert algorithm.find_first_greater_prime_palindrome(8) == 11
assert algorithm.find_first_greater_prime_palindrome(9) == 11
assert algorithm.find_first_greater_prime_palindrome(10) == 11

assert algorithm.find_first_greater_prime_palindrome(11) == 101

assert algorithm.find_first_greater_prime_palindrome(1000) == 10301

assert algorithm.find_first_greater_prime_palindrome(10230) == 10301
assert algorithm.find_first_greater_prime_palindrome(20137) == 30103

assert algorithm.find_first_greater_prime_palindrome(100000000) == 100030001
