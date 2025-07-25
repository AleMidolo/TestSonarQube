import java.awt.geom.Point2D;

public class PointComparator {
    /** 
     * Confronta due punti per uguaglianza utilizzando una tolleranza di 1e-9.
     * @param p1 il primo punto
     * @param p2 il secondo punto
     * @return se i due punti sono uguali o meno
     */
    public static boolean equals(Point2D p1, Point2D p2) {
        if (p1 == null || p2 == null) {
            return false;
        }
        double tolerance = 1e-9;
        return Math.abs(p1.getX() - p2.getX()) < tolerance && Math.abs(p1.getY() - p2.getY()) < tolerance;
    }
}