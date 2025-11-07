# Maximum Depth of Binary Tree

## Problem Statement
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Examples

**Example 1:**
```
Input: root = [3,9,20,null,null,15,7]
       3
      / \
     9  20
        / \
       15  7
Output: 3
Explanation: The maximum depth is 3 (3 -> 20 -> 15 or 3 -> 20 -> 7)
```

**Example 2:**
```
Input: root = [1,null,2]
       1
        \
         2
Output: 2
```

**Example 3:**
```
Input: root = []
Output: 0
```

## Constraints
- The number of nodes in the tree is in the range [0, 10^4]
- -100 <= Node.val <= 100

## Approach

### Method 1: Recursive DFS (Depth-First Search)
Recursively calculate the maximum depth of left and right subtrees, then return the maximum + 1.

**Algorithm:**
1. Base case: If root is None, return 0
2. Recursively calculate left subtree depth
3. Recursively calculate right subtree depth
4. Return max(left_depth, right_depth) + 1

**Time Complexity:** O(n) - Visit each node once
**Space Complexity:** O(h) - Recursion stack, where h is height (O(n) worst case for skewed tree, O(log n) for balanced tree)

### Method 2: Iterative BFS (Level-Order Traversal)
Use a queue to perform level-order traversal and count the number of levels.

**Time Complexity:** O(n) - Visit each node once
**Space Complexity:** O(w) - Queue size, where w is maximum width of tree

## Solution

See `solution.py` for implementation.

## Test Cases
```
Test Case 1: root = [3,9,20,null,null,15,7]
Expected: 3

Test Case 2: root = [1,null,2]
Expected: 2

Test Case 3: root = []
Expected: 0
```

## Notes
- This is a fundamental tree problem that demonstrates recursion
- The recursive solution is elegant and easy to understand
- Can be solved iteratively using BFS for practice

## Related Problems
- Minimum Depth of Binary Tree
- Balanced Binary Tree
- Diameter of Binary Tree

## References
- [LeetCode #104 - Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
