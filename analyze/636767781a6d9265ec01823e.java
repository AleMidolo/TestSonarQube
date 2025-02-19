protected void append(LoggingEvent event) {
    // Get the message from the logging event
    String message = event.getMessage();
    
    // Iterate through all connected clients
    for (Client client : getConnectedClients()) {
        try {
            // Send the log message to the client
            client.sendMessage(message);
        } catch (IOException e) {
            // Handle any exceptions that occur while sending the message
            e.printStackTrace();
        }
    }
}

// Method to get all connected clients (stub for illustration)
private List<Client> getConnectedClients() {
    // This method should return a list of currently connected clients
    return new ArrayList<>();
}

// Client class stub for illustration
class Client {
    public void sendMessage(String message) throws IOException {
        // Logic to send message to the client
    }
}

// LoggingEvent class stub for illustration
class LoggingEvent {
    public String getMessage() {
        // Logic to retrieve the log message
        return "Log message";
    }
}