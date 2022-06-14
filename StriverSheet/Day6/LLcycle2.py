# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        fast, slow = head, head
        entry = head

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                while entry != slow:
                    entry = entry.next
                    slow = slow.next
                return slow

        return None
