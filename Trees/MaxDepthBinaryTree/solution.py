"""
Maximum Depth of Binary Tree - Recursive Solution

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    Calculate the maximum depth of a binary tree.
    
    Args:
        root: TreeNode - Root of the binary tree
    
    Returns:
        int - Maximum depth of the tree
    """
    # Base case: empty tree has depth 0
    if root is None:
        return 0
    
    # Recursive case: calculate depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    # Return the maximum depth + 1 (for current node)
    return max(left_depth, right_depth) + 1


def maxDepthIterative(root):
    """
    Calculate maximum depth using iterative BFS (level-order traversal).
    
    Args:
        root: TreeNode - Root of the binary tree
    
    Returns:
        int - Maximum depth of the tree
    """
    if root is None:
        return 0
    
    from collections import deque
    
    queue = deque([root])
    depth = 0
    
    while queue:
        depth += 1
        level_size = len(queue)
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth


# Test cases
if __name__ == "__main__":
    # Test case 1: [3,9,20,null,null,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    print(f"Test 1 - Recursive: {maxDepth(root1)}")
    print(f"Test 1 - Iterative: {maxDepthIterative(root1)}")
    print()
    
    # Test case 2: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    print(f"Test 2 - Recursive: {maxDepth(root2)}")
    print(f"Test 2 - Iterative: {maxDepthIterative(root2)}")
    print()
    
    # Test case 3: []
    root3 = None
    print(f"Test 3 - Recursive: {maxDepth(root3)}")
    print(f"Test 3 - Iterative: {maxDepthIterative(root3)}")
