@Override 
public Action inspect(AtmosphereResource r) {
    // Check the transport type of the AtmosphereResource
    if (r.getTransport() != null) {
        // Suspend the resource based on the transport type
        r.suspend();
    }
    // Return the action to continue processing
    return Action.CONTINUE;
}