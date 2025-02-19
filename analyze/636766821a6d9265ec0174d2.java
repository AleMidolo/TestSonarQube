public static AtmosphereRequest wrap(HttpServletRequest request) {
    if (request == null) {
        throw new IllegalArgumentException("HttpServletRequest cannot be null");
    }
    return new AtmosphereRequest(request);
}