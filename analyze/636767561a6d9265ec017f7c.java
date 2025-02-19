protected GraphPath<V,E> edgeSetToTour(Set<E> tour, Graph<V,E> graph) {
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
    return new GraphPathImpl<>(graph, vertices);
}