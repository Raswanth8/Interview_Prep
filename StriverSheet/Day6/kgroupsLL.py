# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        length = self.getLength(head)

        dummy.next = head

        pre = dummy

        while(length >= k):
            cur = pre.next
            nex = cur.next

            for i in range(1, k):
                cur.next = nex.next
                nex.next = pre.next
                pre.next = nex
                nex = cur.next

            pre = cur
            length -= k
        return dummy.next

    def getLength(self, head):
        length = 0
        while head != None:
            length += 1
            head = head.next
        return length
