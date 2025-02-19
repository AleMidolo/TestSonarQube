@Override
public ListNode<E> nodoPrecedente() {
    if (this.prev != null) {
        return this.prev;
    } else {
        return null; // or throw an exception if appropriate
    }
}