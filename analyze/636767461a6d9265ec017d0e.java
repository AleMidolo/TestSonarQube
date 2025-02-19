private Pair<List<Integer>, Long> computeSuffixSum(List<Integer> bounds) {
    List<Integer> suffixSums = new ArrayList<>();
    long totalSum = 0;
    
    // Calculate total sum
    for (int num : bounds) {
        totalSum += num;
    }
    
    // Calculate suffix sums
    int suffixSum = 0;
    for (int i = bounds.size() - 1; i >= 0; i--) {
        suffixSum += bounds.get(i);
        suffixSums.add(suffixSum);
    }
    
    // Reverse the suffix sums list to maintain the original order
    Collections.reverse(suffixSums);
    
    return new Pair<>(suffixSums, totalSum);
}