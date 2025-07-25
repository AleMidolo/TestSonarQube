import org.jgrapht.Graph;
import org.jgrapht.alg.shortestpath.DijkstraShortestPath;
import org.jgrapht.graph.DefaultEdge;
import org.jgrapht.graph.DefaultWeightedEdge;
import org.jgrapht.graph.SimpleWeightedGraph;
import org.jgrapht.traverse.BreadthFirstIterator;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

public class GraphTour<V, E extends DefaultEdge> {

    /** 
     * Trasforma una rappresentazione di un insieme in un percorso di grafo.
     * @param tour un insieme contenente i bordi del tour
     * @param graph il grafo
     * @return un percorso di grafo
     */
    protected GraphPath<V, E> edgeSetToTour(Set<E> tour, Graph<V, E> graph) {
        List<V> vertices = new ArrayList<>();
        for (E edge : tour) {
            V source = graph.getEdgeSource(edge);
            V target = graph.getEdgeTarget(edge);
            if (!vertices.contains(source)) {
                vertices.add(source);
            }
            if (!vertices.contains(target)) {
                vertices.add(target);
            }
        }
        
        return new GraphPath<V, E>() {
            @Override
            public List<E> getEdgeList() {
                List<E> edgeList = new ArrayList<>(tour);
                return edgeList;
            }

            @Override
            public V getStartVertex() {
                return vertices.get(0);
            }

            @Override
            public V getEndVertex() {
                return vertices.get(vertices.size() - 1);
            }

            @Override
            public double getWeight() {
                double weight = 0.0;
                for (E edge : tour) {
                    weight += graph.getEdgeWeight(edge);
                }
                return weight;
            }
        };
    }
}