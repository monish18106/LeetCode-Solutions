class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        f = ""
        while curr:
            f += str(curr.val)
            curr = curr.next
        if f == f[::-1]:
            return True
        else:
            return False