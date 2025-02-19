public static final <V> void swap(V[] arr, int i, int j) {
    if (arr == null || i < 0 || j < 0 || i >= arr.length || j >= arr.length) {
        throw new IllegalArgumentException("Invalid index or array is null");
    }
    V temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}