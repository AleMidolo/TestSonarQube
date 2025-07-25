import java.util.Map;

public class BipartiteGraphGenerator<V, E> {

    /**
     * Costruisce un grafo bipartito completo
     */
    @Override
    public void generateGraph(Graph<V, E> target, Map<String, V> resultMap) {
        if (resultMap == null || resultMap.size() < 2) {
            throw new IllegalArgumentException("resultMap must contain at least two vertices.");
        }

        // Split the vertices into two sets
        V[] vertices = (V[]) resultMap.values().toArray();
        int mid = vertices.length / 2;

        // Add edges between the two sets
        for (int i = 0; i < mid; i++) {
            for (int j = mid; j < vertices.length; j++) {
                target.addEdge(vertices[i], vertices[j]);
            }
        }
    }
}

// Assuming a simple Graph interface for demonstration purposes
interface Graph<V, E> {
    void addEdge(V source, V destination);
}