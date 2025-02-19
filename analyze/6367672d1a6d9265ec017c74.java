public boolean remove(int val) {
    if (!contains(val)) {
        return false;
    }
    // Logic to remove the value from the set
    // Assuming we have an internal data structure like a HashSet or an array
    // Example with a HashSet
    return mySet.remove(val);
}