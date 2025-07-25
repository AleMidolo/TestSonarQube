import org.jgrapht.Graph;
import org.jgrapht.GraphType;
import org.jgrapht.alg.clique.CliqueFinder;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.SimpleGraph;

import java.util.HashSet;
import java.util.Set;

public class CliqueChecker {

    /** 
     * Controlla se il sottografo di <code>graph</code> indotto dai dati <code>vertices</code> è completo, cioè un clique.
     * @param graph il grafo.
     * @param vertices i vertici da cui indurre il sottografo.
     * @return true se il sottografo indotto è un clique.
     */
    private static <V, E> boolean isClique(Graph<V, E> graph, Set<V> vertices) {
        // Check if the vertices set is empty or contains only one vertex
        if (vertices.isEmpty() || vertices.size() == 1) {
            return true;
        }

        // Check if all pairs of vertices are connected
        for (V v1 : vertices) {
            for (V v2 : vertices) {
                if (!v1.equals(v2) && !graph.containsEdge(v1, v2)) {
                    return false; // Found a pair that is not connected
                }
            }
        }
        return true; // All pairs are connected
    }

    public static void main(String[] args) {
        // Example usage
        Graph<String, DefaultEdge> graph = new SimpleGraph<>(DefaultEdge.class);
        graph.addVertex("A");
        graph.addVertex("B");
        graph.addVertex("C");
        graph.addEdge("A", "B");
        graph.addEdge("B", "C");
        graph.addEdge("A", "C");

        Set<String> vertices = new HashSet<>();
        vertices.add("A");
        vertices.add("B");
        vertices.add("C");

        boolean result = isClique(graph, vertices);
        System.out.println("Is the induced subgraph a clique? " + result);
    }
}