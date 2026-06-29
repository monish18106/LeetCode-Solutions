class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        s = f = dummy
        for _ in range(n+1):
            f = f.next
        while f:
            s = s.next
            f = f.next
        s.next = s.next.next
        return dummy.next