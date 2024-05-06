class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head

        # Add nodes to the stack
        while current:
            stack.append(current)
            current = current.next

        current = stack.pop()
        maximum = current.val
        result_list = ListNode(maximum)

        # Remove nodes from the stack and add to result
        while stack:
            current = stack.pop()
            # Current should not be added to the result
            if current.val < maximum:
                continue
            # Add new node with current's value to front of the result
            else:
                new_node = ListNode(current.val)
                new_node.next = result_list
                result_list = new_node
                maximum = current.val

        return result_list
