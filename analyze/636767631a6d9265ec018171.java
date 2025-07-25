class ListNodeImpl<E> {
    E value;
    ListNodeImpl<E> next;
    ListNodeImpl<E> prev;

    ListNodeImpl(E value) {
        this.value = value;
    }
}

public class LinkedList<E> {
    private ListNodeImpl<E> head;
    private ListNodeImpl<E> tail;

    /** 
     * Rimuove il nodo non nullo {@code node} dalla lista. 
     */
    private boolean unlink(ListNodeImpl<E> node) {
        if (node == null) {
            return false;
        }

        if (node.prev != null) {
            node.prev.next = node.next;
        } else {
            head = node.next; // node is head
        }

        if (node.next != null) {
            node.next.prev = node.prev;
        } else {
            tail = node.prev; // node is tail
        }

        node.next = null;
        node.prev = null;
        return true;
    }
}