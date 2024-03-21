# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''Recursive Solution'''
        # Base Case Check: if the linked list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Recursive Call: reverse the sublist starting from the next node
        new_head = self.reverseList(head.next)

        # Reverse Pointers:
        # 1. Set the next node's next pointer to the current node (reversing the direction)
        front = head.next
        front.next = head
        # 2. Set the current node's next pointer to None (break the original link)
        head.next = None

        # Return the new head of the reversed sublist
        return new_head

        
