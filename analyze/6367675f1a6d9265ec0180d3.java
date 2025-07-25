import java.util.HashMap;
import java.util.Map;

public class GraphUtils {

    /** 
     * Calcola un automorfismo identitario (cioè una mappatura di un grafo in cui ogni vertice si mappa su se stesso).
     * @param graph il grafo di input
     * @param <V> il tipo di vertice del grafo
     * @param <E> il tipo di arco del grafo
     * @return una mappatura da grafo a grafo
     */
    public static <V, E> IsomorphicGraphMapping<V, E> identity(Graph<V, E> graph) {
        Map<V, V> mapping = new HashMap<>();
        
        for (V vertex : graph.getVertices()) {
            mapping.put(vertex, vertex);
        }
        
        return new IsomorphicGraphMapping<>(mapping);
    }
}

class Graph<V, E> {
    // Assume this class has necessary methods like getVertices()
    public Iterable<V> getVertices() {
        // Implementation here
        return null; // Placeholder
    }
}

class IsomorphicGraphMapping<V, E> {
    private final Map<V, V> mapping;

    public IsomorphicGraphMapping(Map<V, V> mapping) {
        this.mapping = mapping;
    }

    public Map<V, V> getMapping() {
        return mapping;
    }
}