public int nonZeros(int row) {
    int count = 0;
    // Assuming we have a 2D array called 'matrix' where 'row' is the index of the row we are checking
    for (int col = 0; col < matrix[row].length; col++) {
        if (matrix[row][col] != 0) {
            count++;
        }
    }
    return count;
}