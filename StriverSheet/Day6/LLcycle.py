# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        if head == None:
            return False

        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False
