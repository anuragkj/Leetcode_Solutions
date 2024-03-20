class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        merge_array = []
        
        # Add list1 node values before `a` to the array.
        index = 0
        current1 = list1
        while index < a:
            merge_array.append(current1.val)
            current1 = current1.next
            index += 1

        # Add list2 node values to the array
        current2 = list2
        while current2 is not None:
            merge_array.append(current2.val)
            current2 = current2.next

        # Find node b + 1
        while index < b + 1:
            current1 = current1.next
            index += 1

        # Add list1 node values after `b` to the array.
        while current1 is not None:
            merge_array.append(current1.val)
            current1 = current1.next

        # Build a linked list with the result by iterating over the array
        # in reverse order and inserting new nodes to the front of the list
        result_list = None
        for i in range(len(merge_array)):
            new_node = ListNode(merge_array.pop(), result_list)
            result_list = new_node
        return result_list
