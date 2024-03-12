class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front

        while start is not None:
            prefix_sum = 0
            end = start.next

            while end is not None:
                # Add end's value to the prefix sum
                prefix_sum += end.val
                # Delete zero sum consecutive sequence 
                # by setting node before sequence to node after
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next

            start = start.next

        return front.next
