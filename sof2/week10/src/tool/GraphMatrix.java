package tool;

import java.util.List;
import java.util.Set;

public class GraphMatrix<V, E extends Edge<V>> implements IGraph<V, E> {
    int[][] matrix;
    

    @Override
    public Set<V> getVertices() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Set<E> getEdges() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean containsVertex(V vertex) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean containsEdge(E edge) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public Set<V> getNeighbors(V vertex) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Set<E> getInEdges(V vertex) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Set<E> getOutEdges(V vertex) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public List<Set<V>> getComponents() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public boolean addEdge(V source, V target) {
        // TODO Auto-generated method stub
        return false;
    }

    @Override
    public boolean addVertex(V vertex) {
        // TODO Auto-generated method stub
        return false;
    }
    
}
