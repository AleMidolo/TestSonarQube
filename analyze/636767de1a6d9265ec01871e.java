public class ShardingChecker {

    /**
     * @param modelName nome del modello dell'entità
     * @throws IllegalStateException se gli indici della chiave di sharding non sono continui
     */
    private void check(String modelName) throws IllegalStateException {
        // Simulated logic for checking sharding key continuity
        int[] shardingKeys = getShardingKeys(modelName);
        
        for (int i = 0; i < shardingKeys.length - 1; i++) {
            if (shardingKeys[i] + 1 != shardingKeys[i + 1]) {
                throw new IllegalStateException("Sharding keys are not continuous for model: " + modelName);
            }
        }
    }

    // Simulated method to retrieve sharding keys based on model name
    private int[] getShardingKeys(String modelName) {
        // This is just a placeholder. In a real implementation, this would fetch the actual keys.
        return new int[]{1, 2, 3, 5}; // Example of non-continuous keys
    }

    public static void main(String[] args) {
        ShardingChecker checker = new ShardingChecker();
        try {
            checker.check("ExampleModel");
        } catch (IllegalStateException e) {
            System.out.println(e.getMessage());
        }
    }
}