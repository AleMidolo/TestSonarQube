import javafx.util.Pair;

class Box2D {
    private double x;
    private double y;
    private double width;
    private double height;

    public Box2D(double x, double y, double width, double height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }
}

public class BoxSplitter {
    /** 
     * Divide una "Box2D" lungo l'asse x in due "Box2D" uguali.
     * @param box la scatola da dividere
     * @return una coppia con le due scatole risultanti
     */
    public static Pair<Box2D, Box2D> splitAlongXAxis(Box2D box) {
        double halfWidth = box.getWidth() / 2;
        Box2D box1 = new Box2D(box.getX(), box.getY(), halfWidth, box.getHeight());
        Box2D box2 = new Box2D(box.getX() + halfWidth, box.getY(), halfWidth, box.getHeight());
        return new Pair<>(box1, box2);
    }

    public static void main(String[] args) {
        Box2D box = new Box2D(0, 0, 4, 2);
        Pair<Box2D, Box2D> result = splitAlongXAxis(box);
        System.out.println("Box 1: (" + result.getKey().getX() + ", " + result.getKey().getY() + ", " + result.getKey().getWidth() + ", " + result.getKey().getHeight() + ")");
        System.out.println("Box 2: (" + result.getValue().getX() + ", " + result.getValue().getY() + ", " + result.getValue().getWidth() + ", " + result.getValue().getHeight() + ")");
    }
}