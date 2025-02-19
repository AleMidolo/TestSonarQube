private boolean unlink(ListNodeImpl<E> node) {
    if (node == null) {
        return false;
    }

    ListNodeImpl<E> prev = node.prev;
    ListNodeImpl<E> next = node.next;

    if (prev != null) {
        prev.next = next;
    }

    if (next != null) {
        next.prev = prev;
    }

    node.prev = null;
    node.next = null;

    return true;
}