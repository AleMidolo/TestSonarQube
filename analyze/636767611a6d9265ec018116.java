private Set<V> intersection(Set<V> set1, Set<V> set2) {
    Set<V> intersectionSet = new HashSet<>(set1);
    intersectionSet.retainAll(set2);
    return intersectionSet;
}