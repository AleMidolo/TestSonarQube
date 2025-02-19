private Set<V> initVisibleVertices() {
    Set<V> visibleVertices = new HashSet<>();
    for (Edge<V> edge : edges) {
        V source = edge.getSource();
        V target = edge.getTarget();
        visibleVertices.add(source);
        visibleVertices.add(target);
    }
    return visibleVertices;
}