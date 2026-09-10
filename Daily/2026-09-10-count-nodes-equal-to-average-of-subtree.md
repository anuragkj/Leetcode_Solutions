# [2265] Count Nodes Equal to Average of Subtree

**Difficulty:** Medium &nbsp;·&nbsp; **Daily Challenge:** 2026-09-10 &nbsp;·&nbsp; [Open on LeetCode](https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/)

**Topics:** Tree, Depth-First Search, Binary Tree

> 🧠 Auto-generated study note. Read it, understand it, then **paste the solution yourself** on LeetCode. Nothing here is auto-submitted.

---

## Original Problem

Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

Note:

- The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

- A subtree of root is a tree consisting of root and all of its descendants.

Example 1:

Input: root = [4,8,5,0,1,null,6]
Output: 5
Explanation:
For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
For the node with value 0: The average of its subtree is 0 / 1 = 0.
For the node with value 1: The average of its subtree is 1 / 1 = 1.
For the node with value 6: The average of its subtree is 6 / 1 = 6.

Example 2:

Input: root = [1]
Output: 1
Explanation: For the node with value 1: The average of its subtree is 1 / 1 = 1.

Constraints:

- The number of nodes in the tree is in the range [1, 1000].

- 0 <= Node.val <= 1000

**Examples / sample tests:**

```
[4,8,5,0,1,null,6]
[1]
```

---

## Problem Summary
We need to count how many nodes in a given binary tree have a value equal to the rounded-down average of all values in their respective subtrees. The average is calculated as total sum divided by total count, using integer division.

## Intuition
To calculate the average of a subtree, we need two pieces of information: the **sum of all node values** in that subtree and the **total count of nodes** in that subtree. This sounds like a perfect job for a **Depth-First Search (DFS)**, specifically a **post-order traversal**.

Why post-order? Because for any given node, to calculate its subtree's sum and count, we first need to know the sum and count of its *left child's subtree* and its *right child's subtree*. Once we have these from the children, we can combine them with the current node's own value and count (which is 1) to get the total for the current node's subtree. This "bottom-up" aggregation is characteristic of post-order traversal.

## Approach
We will use a recursive helper function that performs a post-order traversal. This function will return the necessary information (sum and count) to its parent, and also check the condition for the current node.

1.  **Initialize a counter**: Create an instance variable `self.result = 0` in the `Solution` class to keep track of the number of nodes that satisfy the condition.
2.  **Define a recursive helper function `dfs(node)`**:
    *   This function will take a `TreeNode` as input.
    *   It will return a tuple `(subtree_sum, subtree_count)` representing the sum of values and the number of nodes in the subtree rooted at `node`.
    *   **Base Case**: If `node` is `None` (an empty subtree), return `(0, 0)` because an empty subtree has a sum of 0 and 0 nodes.
    *   **Recursive Step**:
        1.  Recursively call `dfs` for the `left` child: `(left_sum, left_count) = self.dfs(node.left)`.
        2.  Recursively call `dfs` for the `right` child: `(right_sum, right_count) = self.dfs(node.right)`.
        3.  Calculate the **total sum** for the current node's subtree: `current_sum = node.val + left_sum + right_sum`.
        4.  Calculate the **total count** for the current node's subtree: `current_count = 1 + left_count + right_count`. (The `1` is for the current `node` itself).
        5.  Calculate the **average** for the current node's subtree: `average = current_sum // current_count`. Remember to use integer division (`//`) as specified.
        6.  **Check Condition**: If `node.val == average`, increment `self.result`.
        7.  Finally, return `(current_sum, current_count)` to the parent call.
3.  **Initial Call**: Call `self.dfs(root)` from the main `averageOfSubtree` method.
4.  **Return Result**: After the DFS completes, return `self.result`.

## Visualization
The core idea is that each node passes up its subtree's total sum and node count to its parent.

```mermaid
graph TD
    subgraph Root Call
        A[dfs(root)]
    end

    subgraph Recursive Calls
        B[dfs(node)]
        C[dfs(node.left)]
        D[dfs(node.right)]
    end

    C -- (left_sum, left_count) --> B
    D -- (right_sum, right_count) --> B

    B -- Calculate current_sum, current_count --> E{Check if node.val == average}
    E -- If True --> F[Increment self.result]
    E -- Always --> G[Return (current_sum, current_count) to parent]

    A --> B
    B --> G
```

## Dry Run
Let's trace Example 1: `root = [4,8,5,0,1,null,6]`

| Node Value | `dfs` call | `left_sum`, `left_count` | `right_sum`, `right_count` | `current_sum` | `current_count` | `average` | `node.val == average?` | `self.result` | Return Value |
| :--------- | :--------- | :----------------------- | :------------------------- | :------------ | :-------------- | :-------- | :--------------------- | :------------ | :----------- |
| `None`     | `dfs(None)`| -                        | -                          | 0             | 0               | -         | -                      | 0             | `(0, 0)`     |
| **0**      | `dfs(0)`   | `(0,0)` from `dfs(None)` | `(0,0)` from `dfs(None)`   | 0             | 1               | 0         | `0 == 0` (True)        | 1             | `(0, 1)`     |
| **1**      | `dfs(1)`   | `(0,0)` from `dfs(None)` | `(0,0)` from `dfs(None)`   | 1             | 1               | 1         | `1 == 1` (True)        | 2             | `(1, 1)`     |
| **6**      | `dfs(6)`   | `(0,0)` from `dfs(None)` | `(0,0)` from `dfs(None)`   | 6             | 1               | 6         | `6 == 6` (True)        | 3             | `(6, 1)`     |
| **8**      | `dfs(8)`   | `(0,1)` from `dfs(0)`    | `(1,1)` from `dfs(1)`      | `8+0+1 = 9`   | `1+1+1 = 3`     | `9//3 = 3`| `8 == 3` (False)       | 3             | `(9, 3)`     |
| **5**      | `dfs(5)`   | `(0,0)` from `dfs(None)` | `(6,1)` from `dfs(6)`      | `5+0+6 = 11`  | `1+0+1 = 2`     | `11//2 = 5`| `5 == 5` (True)        | 4             | `(11, 2)`    |
| **4**      | `dfs(4)`   | `(9,3)` from `dfs(8)`    | `(11,2)` from `dfs(5)`     | `4+9+11 = 24` | `1+3+2 = 6`     | `24//6 = 4`| `4 == 4` (True)        | 5             | `(24, 6)`    |

The final `self.result` is **5**.

## Complexity
*   **Time Complexity**: O(N), where N is the number of nodes in the tree. Each node is visited exactly once by the `dfs` function, and constant time work is done at each node.
*   **Space Complexity**: O(H), where H is the height of the tree. This is due to the recursion stack. In the worst case (a skewed tree), H can be N, leading to O(N) space. In the best case (a balanced tree), H is log N, leading to O(log N) space.

## Edge Cases
*   **Single Node Tree**: `root = [1]`. The solution correctly handles this. `dfs(1)` will get `(0,0)` from both children, calculate `sum=1, count=1`, `avg=1`, and `1 == 1` will be true, incrementing `self.result` to 1.
*   **Empty Tree**: The problem constraints state the number of nodes is in the range `[1, 1000]`, so an empty tree is not possible.
*   **Nodes with value 0**: Handled correctly by sum and average calculations. For example, a node with value 0 and no children will have `sum=0, count=1`, `avg=0`, and `0 == 0` will be true.
*   **Skewed Trees**: A tree where all nodes are either left or right children (e.g., a linked list structure). The recursive DFS naturally handles this, though it might lead to O(N) space complexity for the recursion stack.

## Solution
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0  # Initialize a counter for nodes satisfying the condition

        # Helper function for DFS traversal
        # Returns (sum of subtree values, count of nodes in subtree)
        def dfs(node: TreeNode) -> (int, int):
            # Base case: if the node is None, it's an empty subtree
            # An empty subtree has a sum of 0 and 0 nodes.
            if not node:
                return (0, 0)

            # Recursively get sum and count for left subtree
            left_sum, left_count = dfs(node.left)
            # Recursively get sum and count for right subtree
            right_sum, right_count = dfs(node.right)

            # Calculate total sum for the current node's subtree
            # It's the current node's value + sum from left child + sum from right child
            current_subtree_sum = node.val + left_sum + right_sum
            
            # Calculate total count for the current node's subtree
            # It's 1 (for the current node) + count from left child + count from right child
            current_subtree_count = 1 + left_count + right_count

            # Calculate the average, using integer division as specified
            average = current_subtree_sum // current_subtree_count

            # Check if the current node's value equals the average of its subtree
            if node.val == average:
                self.result += 1  # If true, increment our global counter

            # Return the sum and count of the current subtree to its parent
            return (current_subtree_sum, current_subtree_count)

        # Start the DFS traversal from the root
        dfs(root)
        
        # Return the final count of nodes that met the condition
        return self.result

```

## Why This Works
This solution works because the **post-order traversal** (children processed before parent) guarantees that when we visit any node, we have already computed the total sum and node count for its entire left and right subtrees. This "bottom-up" aggregation of information allows us to correctly calculate the average for the current node's subtree and check the condition. The `self.result` counter correctly accumulates all nodes that satisfy the condition throughout the entire tree traversal.

---
<sub>Generated 2026-09-10 05:07 UTC by the Daily LeetCode Explainer (Gemini) • language: Python • not submitted automatically.</sub>
