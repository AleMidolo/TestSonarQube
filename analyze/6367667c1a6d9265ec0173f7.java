public boolean hasBytes() {
    Object body = getBody(); // Assuming getBody() retrieves the body object
    return body instanceof byte[];
}