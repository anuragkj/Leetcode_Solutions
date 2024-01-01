class Solution:
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        while left and right:
            if left.val < right.val:
                temp.next = left
                temp = temp.next
                left = left.next
            else:
                temp.next = right
                temp = temp.next
                right = right.next
        while left:
            temp.next = left
            temp = temp.next
            left = left.next
        while right:
            temp.next = right
            temp = temp.next
            right = right.next
        return dummy.next
    
    def mergeSort(self, lists: List[ListNode], start: int, end: int) -> ListNode:
        if start == end:
            return lists[start]
        mid = start + (end - start) // 2
        left = self.mergeSort(lists, start, mid)
        right = self.mergeSort(lists, mid + 1, end)
        return self.merge(left, right)
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.mergeSort(lists, 0, len(lists) - 1)
