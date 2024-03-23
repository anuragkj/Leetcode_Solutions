class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list_values = []
        curr = head
        while curr:
            list_values.append(curr.val)
            curr = curr.next
        
        # Reorder the list using for loop
        curr = head
        for i in range(len(list_values)):
            if i % 2 == 0:
                curr.val = list_values[i // 2]
            else:
                curr.val = list_values[len(list_values) - (i + 1) // 2]
            curr = curr.next
