protected void appendDetail(StringBuffer buffer, String fieldName, byte[] array) {
    if (array == null) {
        buffer.append(fieldName).append(" = null");
        return;
    }
    buffer.append(fieldName).append(" = [");
    for (int i = 0; i < array.length; i++) {
        buffer.append(array[i]);
        if (i < array.length - 1) {
            buffer.append(", ");
        }
    }
    buffer.append("]");
}