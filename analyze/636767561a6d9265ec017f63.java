@Override
public boolean hasNext() {
    for (boolean visited : visitedVertices) {
        if (!visited) {
            return true;
        }
    }
    return false;
}