private void reload(List<Set<Integer>> bucketsByLabel, List<Integer> labels, int minLabel) {
    // Get the bucket with the minimum label
    Set<Integer> minLabelBucket = bucketsByLabel.get(minLabel);
    
    // Get the bucket with label 0
    Set<Integer> zeroLabelBucket = bucketsByLabel.get(0);
    
    // Move all vertices from the minLabel bucket to the zero label bucket
    for (Integer vertex : minLabelBucket) {
        zeroLabelBucket.add(vertex);
        labels.set(vertex, 0); // Update the label of the vertex to 0
    }
    
    // Clear the minLabel bucket
    minLabelBucket.clear();
}