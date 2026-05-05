# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None

        ln = 0
        tmp = head
        tail = None
        while tmp != None:
            tail = tmp
            tmp = tmp.next
            ln += 1
        
        k = k % ln
        
        tail.next = head
        
        ans = None
        while ln - k != 0:
            ans = head
            head = head.next
            ln -= 1
        
        ans.next = None
        
        return head
