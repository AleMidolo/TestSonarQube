private void check(String modelName) throws IllegalStateException {
    // Simulating a check for continuous sharding key indices
    int[] shardingKeyIndices = getShardingKeyIndices(modelName);
    
    for (int i = 0; i < shardingKeyIndices.length - 1; i++) {
        if (shardingKeyIndices[i] + 1 != shardingKeyIndices[i + 1]) {
            throw new IllegalStateException("Sharding key indices are not continuous for model: " + modelName);
        }
    }
}

// Dummy method to simulate retrieval of sharding key indices
private int[] getShardingKeyIndices(String modelName) {
    // This should return the actual sharding key indices based on the modelName
    return new int[]{0, 1, 2}; // Example of continuous indices
}