private static <V,E>boolean isClique(Graph<V,E> graph, Set<V> vertices) {
    // Controlla se il numero di vertici è 0 o 1, in tal caso è un clique
    if (vertices.size() <= 1) {
        return true;
    }

    // Controlla ogni coppia di vertici nel set
    for (V v1 : vertices) {
        for (V v2 : vertices) {
            if (!v1.equals(v2)) {
                // Se non esiste un arco tra v1 e v2, non è un clique
                if (!graph.containsEdge(v1, v2)) {
                    return false;
                }
            }
        }
    }
    return true;
}