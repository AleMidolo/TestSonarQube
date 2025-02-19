@Override
public int available() throws IOException {
    // Assuming 'inputStream' is an instance of InputStream that you are wrapping
    return inputStream.available();
}