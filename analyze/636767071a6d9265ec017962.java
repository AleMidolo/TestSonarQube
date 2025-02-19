public void putAllWriteable(BeanMap map) {
    if (map == null) {
        throw new IllegalArgumentException("The provided BeanMap cannot be null.");
    }
    
    for (String propertyName : map.getPropertyNames()) {
        if (map.isWriteable(propertyName)) {
            Object value = map.get(propertyName);
            this.put(propertyName, value);
        }
    }
}