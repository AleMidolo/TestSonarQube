protected Label readLabel(final int bytecodeOffset, final Label[] labels) {
    if (labels[bytecodeOffset] != null) {
        return labels[bytecodeOffset];
    }
    labels[bytecodeOffset] = new Label();
    return labels[bytecodeOffset];
}