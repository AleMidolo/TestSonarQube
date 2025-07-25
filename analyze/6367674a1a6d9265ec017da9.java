import java.util.NoSuchElementException;

class ListNode<E> {
    E data;
    ListNode<E> next;
    ListNode<E> prev;

    ListNode(E data) {
        this.data = data;
    }
}

class DoublyLinkedList<E> {
    private ListNode<E> head;
    private ListNode<E> tail;

    public void addListNode(ListNode<E> node) {
        if (node == null) {
            throw new IllegalArgumentException("Node cannot be null");
        }
        if (head == null) {
            head = tail = node;
            node.next = node.prev = null;
        } else {
            tail.next = node;
            node.prev = tail;
            node.next = null;
            tail = node;
        }
    }

    public void removeListNode(ListNode<E> node) {
        if (node == null || head == null) {
            throw new NoSuchElementException("Node not found or list is empty");
        }
        if (node == head) {
            head = head.next;
            if (head != null) {
                head.prev = null;
            } else {
                tail = null;
            }
        } else if (node == tail) {
            tail = tail.prev;
            tail.next = null;
        } else {
            node.prev.next = node.next;
            node.next.prev = node.prev;
        }
    }

    private void moveAllListNodes(DoublyLinkedList<E> list) {
        if (list == null || list.head == null) {
            return;
        }
        ListNode<E> current = list.head;
        while (current != null) {
            ListNode<E> nextNode = current.next;
            this.addListNode(current);
            list.removeListNode(current);
            current = nextNode;
        }
    }
}