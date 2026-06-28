class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        m = x
        r = 0
        while m != 0:
            r = r * 10 + (m % 10)
            m //= 10
        return x == r
        