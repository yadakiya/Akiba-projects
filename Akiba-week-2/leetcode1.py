
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False

        original = x
        reversed_number = 0

        # Reverse the number using arithmetic
        while x > 0:
            digit = x % 10
            reversed_number = reversed_number * 10 + digit
            x = x // 10

        return original == reversed_number