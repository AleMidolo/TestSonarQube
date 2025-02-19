public static Pair<Box2D, Box2D> splitAlongXAxis(Box2D box) {
    float centerX = (box.getMinX() + box.getMaxX()) / 2;
    Box2D box1 = new Box2D(box.getMinX(), box.getMinY(), centerX, box.getMaxY());
    Box2D box2 = new Box2D(centerX, box.getMinY(), box.getMaxX(), box.getMaxY());
    return new Pair<>(box1, box2);
}