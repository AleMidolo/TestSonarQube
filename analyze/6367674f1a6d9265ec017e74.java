import java.util.LinkedList;

public class Queue<T> {
    private LinkedList<T> elements;

    public Queue() {
        elements = new LinkedList<>();
    }

    public void enqueue(T element) {
        elements.addLast(element);
    }

    public T dequeue() {
        if (elements.isEmpty()) {
            throw new IllegalStateException("Queue is empty");
        }
        return elements.removeFirst();
    }

    public boolean isEmpty() {
        return elements.isEmpty();
    }

    /**
     * Restituisce una rappresentazione testuale della coda.
     * @return una rappresentazione testuale della coda.
     */
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Queue: [");
        for (int i = 0; i < elements.size(); i++) {
            sb.append(elements.get(i));
            if (i < elements.size() - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        Queue<Integer> queue = new Queue<>();
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        System.out.println(queue.toString()); // Output: Queue: [1, 2, 3]
    }
}