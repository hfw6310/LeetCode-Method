# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        #分治法
        if not lists:
            return
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        '''
        """
        #优先级队列法
        import heapq #堆数据结构
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head) #  heappop(heap) -从堆中弹出最小值 
            p.next = ListNode(val)
            p = p.next

            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

        return dummy.next
        """
        '''
        import heapq #堆数据结构
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            while lists[i] :
                heapq.heappush(head, (lists[i].val, i)) #!!!
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head) # heappop(heap) -从堆中弹出最小值 
            p.next = ListNode(val)
            p = p.next
        return dummy.next
        '''
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            while lists[i]:
                heapq.heappush(head, lists[i].val)
                lists[i] = lists[i].next
        while head:
            tmp = heapq.heappop(head)
            p.next = ListNode(tmp)
            p = p.next
        return dummy.next