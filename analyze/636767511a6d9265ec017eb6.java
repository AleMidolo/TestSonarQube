private OuterFaceCirculator selectOnOuterFace(Predicate<Node> predicate, Node start, Node stop, int dir) {
    OuterFaceCirculator circulator = new OuterFaceCirculator(start, dir);
    do {
        if (predicate.test(circulator.getNode())) {
            return circulator;
        }
        circulator = circulator.next();
    } while (!circulator.getNode().equals(stop));
    return circulator;
}