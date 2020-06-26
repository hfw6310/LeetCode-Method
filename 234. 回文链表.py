# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        # 堆栈
        stack = []
        # step1: push
        curr = head
        while (curr):
            stack.append(curr)
            curr = curr.next
        # step2: pop and compare
        node1 = head
        while (stack):
            node2 = stack.pop()
            if node1.val != node2.val:
                return False
            node1 = node1.next
        return True
        '''
        #递归
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()
        '''