private void addReverse(final File[] files) {
    if (files == null) {
        return;
    }
    for (int i = files.length - 1; i >= 0; i--) {
        addFile(files[i]);
    }
}

private void addFile(File file) {
    // Implementazione per aggiungere il file
}