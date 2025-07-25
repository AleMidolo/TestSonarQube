import java.util.HashSet;
import java.util.Set;

public class Graph<V> {
    private Set<V> vertices;
    private Set<Edge<V>> edges;

    public Graph() {
        this.vertices = new HashSet<>();
        this.edges = new HashSet<>();
    }

    public void addVertex(V vertex) {
        vertices.add(vertex);
    }

    public void addEdge(V from, V to) {
        edges.add(new Edge<>(from, to));
        addVertex(from);
        addVertex(to);
    }

    /** 
     * Calcola tutti i vertici che hanno un grado positivo iterando intenzionalmente sugli archi. Questo mantiene la complessità a $O(m)$ dove $m$ è il numero di archi.
     * @return insieme di vertici con grado positivo
     */
    private Set<V> initVisibleVertices() {
        Set<V> visibleVertices = new HashSet<>();
        for (Edge<V> edge : edges) {
            visibleVertices.add(edge.from);
            visibleVertices.add(edge.to);
        }
        return visibleVertices;
    }

    private static class Edge<V> {
        V from;
        V to;

        Edge(V from, V to) {
            this.from = from;
            this.to = to;
        }
    }
}