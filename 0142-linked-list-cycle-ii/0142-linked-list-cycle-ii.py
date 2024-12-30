# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        seen = set()
        fast = head
        slow = head

        while slow:
            if slow in seen:
                return slow
            else:
                seen.add(slow)
                slow = slow.next
        
        return None