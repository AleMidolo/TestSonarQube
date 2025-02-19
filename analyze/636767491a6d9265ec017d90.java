public static final <V> void reverse(V[] arr, int from, int to) {
    if (arr == null || from < 0 || to >= arr.length || from >= to) {
        throw new IllegalArgumentException("Invalid indices or array is null");
    }
    while (from < to) {
        V temp = arr[from];
        arr[from] = arr[to];
        arr[to] = temp;
        from++;
        to--;
    }
}