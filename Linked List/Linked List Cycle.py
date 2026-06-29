class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        b = set()
        while head:
            if head in b:
                return True
            b.add(head)
            head = head.next
        return False
        