class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = [0,1,2,3,4,5,6,7,8,9]
        f = f""
        for i in s:
            if (65 <= ord(i) <= 90) or  (97 <= ord(i) <= 122) or ("0" <= i <= "9"):
                f  += i
        if f.lower() == f[::-1].lower():
            return True
        else:
            return False

        