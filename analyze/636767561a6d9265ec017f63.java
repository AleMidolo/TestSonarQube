import java.util.Iterator;
import java.util.List;

public class GraphIterator implements Iterator<Vertex> {
    private List<Vertex> vertices;
    private boolean[] visited;
    private int currentIndex;

    public GraphIterator(List<Vertex> vertices) {
        this.vertices = vertices;
        this.visited = new boolean[vertices.size()];
        this.currentIndex = 0;
    }

    /** 
     * Controlla se esistono vertici non visitati.
     * @return true se esistono vertici non visitati.
     */
    @Override
    public boolean hasNext() {
        while (currentIndex < vertices.size()) {
            if (!visited[currentIndex]) {
                return true;
            }
            currentIndex++;
        }
        return false;
    }

    @Override
    public Vertex next() {
        if (!hasNext()) {
            throw new NoSuchElementException();
        }
        Vertex vertex = vertices.get(currentIndex);
        visited[currentIndex] = true;
        currentIndex++;
        return vertex;
    }
    
    // Assuming Vertex is a class defined elsewhere
    public static class Vertex {
        // Vertex properties and methods
    }
}