@Override 
public void generateGraph(Graph<V,E> target, Map<String,V> resultMap) {
    // Assuming V is the type of vertices and E is the type of edges
    List<V> setA = new ArrayList<>();
    List<V> setB = new ArrayList<>();
    
    // Populate setA and setB from resultMap
    for (Map.Entry<String, V> entry : resultMap.entrySet()) {
        if (setA.size() < resultMap.size() / 2) {
            setA.add(entry.getValue());
        } else {
            setB.add(entry.getValue());
        }
    }
    
    // Create edges between every vertex in setA and every vertex in setB
    for (V vertexA : setA) {
        for (V vertexB : setB) {
            target.addEdge(vertexA, vertexB);
        }
    }
}