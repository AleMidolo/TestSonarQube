private boolean checkDuplicate(final List<AtmosphereInterceptor> interceptorList, Class<? extends AtmosphereInterceptor> c) {
    for (AtmosphereInterceptor interceptor : interceptorList) {
        if (interceptor.getClass().equals(c)) {
            return false; // An instance of the class already exists in the list
        }
    }
    return true; // No instance of the class found in the list
}