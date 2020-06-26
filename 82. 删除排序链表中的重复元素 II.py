# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1000)
        dummy.next = head
        #print(dummy)
        slow = dummy
        fast = dummy.next
        #print(fast)
        while fast:
            if  fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next

        slow.next = fast
        #print("slow:",slow)
        return dummy.next

        '''
        '''
        #递归
        if not head:
            return head
        if head.next and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head

        '''
        thead = ListNode('a')
        thead.next = head
        pre, cur = None, thead
        while cur:
            pre = cur
            cur = cur.next
            while cur and cur.next and cur.next.val == cur.val:
                t = cur.val
                while cur and cur.val == t:
                    cur = cur.next
                pre.next = cur
        return thead.next