import java.util.NoSuchElementException;

class ListNode<E> {
    E data;
    ListNode<E> next;
    ListNode<E> previous;

    public ListNode(E data) {
        this.data = data;
        this.next = null;
        this.previous = null;
    }

    /**
     * {@inheritDoc}
     */
    @Override
    public ListNode<E> previousNode() {
        if (this.previous == null) {
            throw new NoSuchElementException("No previous node exists.");
        }
        return this.previous;
    }
}