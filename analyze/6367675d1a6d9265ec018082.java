import java.util.Objects;

class Edge {
    private final Node from;
    private final Node to;

    public Edge(Node from, Node to) {
        this.from = from;
        this.to = to;
    }

    public Node getFrom() {
        return from;
    }

    public Node getTo() {
        return to;
    }
}

class Node {
    private final String name;
    private final boolean isVirtual;

    public Node(String name, boolean isVirtual) {
        this.name = name;
        this.isVirtual = isVirtual;
    }

    public String getName() {
        return name;
    }

    public boolean isVirtual() {
        return isVirtual;
    }
}

class Graph {
    private Node currentNode;
    private Node nextNode;

    public Graph(Node currentNode, Node nextNode) {
        this.currentNode = currentNode;
        this.nextNode = nextNode;
    }

    /**
     * Restituisce un arco che collega il nodo precedentemente restituito con il nodo che verrà restituito successivamente. Se uno dei nodi menzionati è virtuale, l'arco sarà incidente al suo corrispondente reale.
     * @return un arco dal nodo corrente al nodo successivo
     */
    public Edge edgeToNext() {
        Node fromNode = currentNode.isVirtual() ? getRealNode(currentNode) : currentNode;
        Node toNode = nextNode.isVirtual() ? getRealNode(nextNode) : nextNode;
        return new Edge(fromNode, toNode);
    }

    private Node getRealNode(Node virtualNode) {
        // Logic to get the real node corresponding to the virtual node
        // This is a placeholder implementation
        return new Node(virtualNode.getName() + "_real", false);
    }
}