public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("Coda: [");
    // Assuming there is a method to get the elements of the queue
    for (Object element : this.getElements()) {
        sb.append(element.toString()).append(", ");
    }
    if (sb.length() > 6) {
        sb.setLength(sb.length() - 2); // Remove the last comma and space
    }
    sb.append("]");
    return sb.toString();
}