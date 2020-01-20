# AAL

A project for Analysis of algorithms classes at Faculty of Electronics and Information Technology, Warsaw University of Technology. The aim of the project is to invent and implement algorithm for finding first prime palindrome greater than `N`.

## Author

Maciej Szulik

## Problem description

Find a first prime palindromic number greater than `N`.

### Algorithm input

N - natural number in the range from `1` to `10^8`.

### Algorithm output

First prime palindromic number greater than `N`.

## Algorithm

- Let L be the left half of N. Examples:
  - N = 1234; L = 12
  - N = 12345; L = 123
- Let P be the palindromic number created by mirroring L without duplicating (mirroring) the unity digit of L. Examples:
  - L = 99; P= 999
  - L = 123; P = 12321
- Important note: every palindromic number with an even number of digits, except of 11, is not prime (it is divisible by 11), so the algorithm skips generating palindromes with even number of digits. First 5 steps of the algorithm explicite return next prime palindromes to simplify the main loop.

### Main algorithm

1. If `N < 2`, return `2`.
1. If `N < 3`, return `3`.
1. If `N < 5`, return `5`.
1. If `N < 7`, return `7`.
1. If `N < 11`, return `11`.
1. Take the left half of `N`.
1. If `N` has an even number of digits, round `L` up to the first power of `10`. Go to 9.
1. If after mirroring `L`, `P` will be smaller than N, increment L.
1. Mirror `L` to generate `P`.
1. If `P` is a prime number, return `P`.
1. Increment `L` and go to 9.

## Program

### Requirements

- `Python 3.7+`
- `matplotlib`
- `numpy`

### Usage

Run

`python3 prime_palindrome_finder.py --help`

to see how to use program.

### Source files

- `prime_palindrome_finder.py` - ui module
- `algorithm.py` - algorithm module
- `analytics.py` - analytics tools module
