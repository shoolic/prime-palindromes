# Python3 implementation of above approach 
import math 
  
# Function to check whether a number is prime 
def is_prime(n): 
    return n > 1 and all(n % d for d in range(2, int(math.sqrt(n)) + 1)) 
  
# function to generate next smallest prime palindrome 
def NextprimePalindrome(N): 
  
    for k in range(1, 10**6): 
  
        # Check for odd-length palindromes 
        s = str(k) 
        x = int(s + s[-2::-1])  # eg. s = '1234' to x = int('1234321') 
  
        if x >= N and is_prime(x): 
            return x 
  
        # Check for even-length palindromes 
        s = str(k) 
        x = int(s + s[-1::-1])  # eg. s = '1234' to x = int('12344321') 
  
        if x >= N and is_prime(x): 
            return x 
  
# Driver code 
N = 930
  
# Function call to print answer 
print(NextprimePalindrome(N)) 
  
# This code is written by 
# Sanjit_Prasad 