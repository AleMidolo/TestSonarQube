private void moveAllListNodes(DoublyLinkedList<E> list) {
    if (list == null || list.isEmpty()) {
        return;
    }
    
    ListNode<E> currentNode = list.head;
    while (currentNode != null) {
        ListNode<E> nextNode = currentNode.next;
        this.addListNode(currentNode); // Add the node to this list
        list.removeListNode(currentNode); // Remove the node from the original list
        currentNode = nextNode;
    }
}