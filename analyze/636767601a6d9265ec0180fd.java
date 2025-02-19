protected void addToIndex(V sourceVertex, V targetVertex, E e) {
    // Assuming there is a map to hold the edges indexed by source and target vertices
    Map<V, Map<V, List<E>>> index = new HashMap<>();

    // Get the map for the source vertex, or create a new one if it doesn't exist
    Map<V, List<E>> targetMap = index.computeIfAbsent(sourceVertex, k -> new HashMap<>());

    // Get the list of edges for the target vertex, or create a new one if it doesn't exist
    List<E> edges = targetMap.computeIfAbsent(targetVertex, k -> new ArrayList<>());

    // Add the edge to the list
    edges.add(e);
}