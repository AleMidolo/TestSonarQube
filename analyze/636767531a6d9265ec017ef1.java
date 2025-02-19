public static boolean equals(Point2D p1, Point2D p2) {
    final double TOLERANCE = 1e-9;
    if (p1 == null || p2 == null) {
        return false;
    }
    return Math.abs(p1.getX() - p2.getX()) < TOLERANCE && Math.abs(p1.getY() - p2.getY()) < TOLERANCE;
}