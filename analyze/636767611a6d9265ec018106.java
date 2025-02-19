public double vertexWeight(Set<V> v) {
    double totalWeight = 0.0;
    for (V vertex : v) {
        // Assuming there is a method getIncomingEdges that returns the incoming edges for the vertex
        for (Edge<V> edge : getIncomingEdges(vertex)) {
            totalWeight += edge.getWeight();
        }
    }
    return totalWeight;
}