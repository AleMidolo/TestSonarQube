public boolean isCompatible(DataTable dataset) {
    if (dataset == null) {
        return false;
    }
    // Assuming DataTable has a method to get the bucket identifier
    return this.getBucketIdentifier().equals(dataset.getBucketIdentifier());
}