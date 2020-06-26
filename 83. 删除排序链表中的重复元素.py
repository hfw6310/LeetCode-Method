# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1000)
        dummy.next = head
        #print(dummy)
        slow = dummy
        fast = dummy.next
        while fast :
            if slow.val == fast.val:
                fast = fast.next
                slow.next = fast
                #print(dummy)
            else:
                slow = slow.next
                fast = fast.next
                #print(dummy)
        return dummy.next