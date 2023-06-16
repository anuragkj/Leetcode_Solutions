# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sol = ListNode()
        it = sol
        carry = 0
        while(l1 is not None or l2 is not None):
            if (l1 is None):
                it.val = (l2.val + carry)%10 
                carry = (l2.val + carry)//10
                l2 = l2.next            
            elif (l2 is None):
                it.val = (l1.val + carry)%10 
                carry = (l1.val + carry)//10
                l1 = l1.next
            else:
                it.val = (l1.val + l2.val + carry)%10 
                carry = (l1.val + l2.val + carry)//10
                l1 = l1.next
                l2 = l2.next
            if(l1 is not None or l2 is not None):
                it.next = ListNode()
                it = it.next
        if carry != 0:
            it.next = ListNode(carry)
        return sol



