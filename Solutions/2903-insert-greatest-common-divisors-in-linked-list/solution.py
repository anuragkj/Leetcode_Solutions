class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        def _calculate_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if not head.next:
            return head
        node1 = head
        node2 = head.next
        while node2:
            gcd_value = _calculate_gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)
            node1.next = gcd_node
            gcd_node.next = node2
            node1 = node2
            node2 = node2.next

        return head
