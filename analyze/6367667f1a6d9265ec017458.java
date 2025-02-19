public AtmosphereFramework removeAtmosphereHandler(String mapping) {
    if (mapping == null || mapping.isEmpty()) {
        return this; // or throw an IllegalArgumentException
    }
    
    // Assuming handlers is a Map<String, AtmosphereHandler> that stores the mappings
    AtmosphereHandler handler = handlers.remove(mapping);
    
    if (handler != null) {
        // Perform any additional cleanup if necessary
        return this; // Return the current instance
    }
    
    return this; // Return the current instance even if nothing was removed
}