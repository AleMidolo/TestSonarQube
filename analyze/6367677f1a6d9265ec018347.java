public synchronized void send(final String message) {
    // Assuming we have a list of clients to send the message to
    for (Client client : clients) {
        try {
            client.getOutputStream().write((message + "\n").getBytes());
            client.getOutputStream().flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}