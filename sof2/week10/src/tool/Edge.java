package tool;

public abstract class Edge<T> {
    T source;
    T target;
    Double weight;

    public Edge(T source, T target) {
        this.source = source;
        this.target = target;
        this.weight = 1.0;
    }

    public Edge(T source, T target, Double weight) {
        this.source = source;
        this.target = target;
        this.weight = weight;
    }
    
    public T getSource() {
        return source;
    }

    public T getTarget() {
        return target;
    }

    public Double getWeight() {
        return weight;
    }
}