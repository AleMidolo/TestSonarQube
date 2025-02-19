private TreeNode<T> rotateRight(TreeNode<T> node) {
    if (node == null || node.left == null) {
        return node; // No rotation needed
    }
    
    TreeNode<T> newRoot = node.left; // New root will be the left child
    node.left = newRoot.right; // Move the right child of new root to be the left child of the current node
    newRoot.right = node; // Make the current node the right child of the new root
    
    return newRoot; // Return the new root
}