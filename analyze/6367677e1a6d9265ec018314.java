protected int removeUnusedNodes() {
    int removedCount = 0;
    // Assuming we have a method to get the root of the category tree
    CategoryNode root = getRoot();
    removedCount += removeUnusedNodesRecursively(root);
    return removedCount;
}

private int removeUnusedNodesRecursively(CategoryNode node) {
    if (node == null) {
        return 0;
    }

    int removedCount = 0;

    // Recursively check and remove unused child nodes
    List<CategoryNode> children = node.getChildren();
    for (int i = children.size() - 1; i >= 0; i--) {
        CategoryNode child = children.get(i);
        removedCount += removeUnusedNodesRecursively(child);
        if (child.isInactive()) {
            children.remove(i);
            removedCount++;
        }
    }

    return removedCount;
}