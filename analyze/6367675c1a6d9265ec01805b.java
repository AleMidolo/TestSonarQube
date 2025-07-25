public void removeFromTreeEdgeList() {
    // Assuming there are two doubly linked lists for edges: leftEdgeList and rightEdgeList
    EdgeNode currentLeft = leftEdgeList.head;
    EdgeNode currentRight = rightEdgeList.head;

    // Remove this edge from the left edge list
    while (currentLeft != null) {
        if (currentLeft.edge.equals(this)) {
            if (currentLeft.prev != null) {
                currentLeft.prev.next = currentLeft.next;
            } else {
                leftEdgeList.head = currentLeft.next; // Update head if it's the first element
            }
            if (currentLeft.next != null) {
                currentLeft.next.prev = currentLeft.prev;
            }
            break; // Exit after removing the edge
        }
        currentLeft = currentLeft.next;
    }

    // Remove this edge from the right edge list
    while (currentRight != null) {
        if (currentRight.edge.equals(this)) {
            if (currentRight.prev != null) {
                currentRight.prev.next = currentRight.next;
            } else {
                rightEdgeList.head = currentRight.next; // Update head if it's the first element
            }
            if (currentRight.next != null) {
                currentRight.next.prev = currentRight.prev;
            }
            break; // Exit after removing the edge
        }
        currentRight = currentRight.next;
    }
}

// Assuming EdgeNode and EdgeList classes are defined as follows:
class EdgeNode {
    Edge edge;
    EdgeNode next;
    EdgeNode prev;

    EdgeNode(Edge edge) {
        this.edge = edge;
        this.next = null;
        this.prev = null;
    }
}

class EdgeList {
    EdgeNode head;

    EdgeList() {
        this.head = null;
    }
}

// Assuming Edge class is defined
class Edge {
    // Edge properties and methods
}