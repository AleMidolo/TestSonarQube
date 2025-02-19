void removeSelf() {
    // Assuming there is a reference to the parent structure
    if (parent != null) {
        parent.removeBucket(this);
    }
    // Additional cleanup code if necessary
    this.clearData();
}