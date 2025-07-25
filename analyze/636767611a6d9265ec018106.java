import java.util.Set;

public class Graph<V> {
    
    // Assuming there's a method to get the incoming edges for a vertex
    private Set<Edge<V>> getIncomingEdges(V vertex) {
        // Implementation to retrieve incoming edges for the vertex
        return null; // Placeholder
    }

    // Assuming Edge class has a method to get the weight
    private class Edge<V> {
        private double weight;

        public double getWeight() {
            return weight;
        }
    }

    /** 
     * Calcola la somma dei pesi che entrano in un vertice
     * @param v il vertice
     * @return la somma dei pesi che entrano in un vertice
     */
    public double vertexWeight(Set<V> v) {
        double totalWeight = 0.0;
        for (V vertex : v) {
            Set<Edge<V>> incomingEdges = getIncomingEdges(vertex);
            for (Edge<V> edge : incomingEdges) {
                totalWeight += edge.getWeight();
            }
        }
        return totalWeight;
    }
}