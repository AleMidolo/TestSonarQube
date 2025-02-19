@Override 
public AtmosphereResource addEventListener(AtmosphereResourceEventListener e) {
    // Implementation to add the event listener
    if (e == null) {
        throw new IllegalArgumentException("Event listener cannot be null");
    }
    // Assuming there's a list to hold the listeners
    eventListeners.add(e);
    return this; // Returning the current instance for method chaining
}