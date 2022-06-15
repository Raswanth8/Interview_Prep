# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return head

        tail = head
        length = 1  # edge case
        while tail.next != None:
            length += 1
            tail = tail.next

        for i in range(length - k % length):
            tail.next = head
            head = head.next
            tail = tail.next
            tail.next = None

        return head
