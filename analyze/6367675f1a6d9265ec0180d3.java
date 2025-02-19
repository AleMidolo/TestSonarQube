public static <V,E> IsomorphicGraphMapping<V,E> identity(Graph<V,E> graph) {
    IsomorphicGraphMapping<V,E> mapping = new IsomorphicGraphMapping<>();
    for (V vertex : graph.getVertices()) {
        mapping.addMapping(vertex, vertex);
    }
    return mapping;
}