import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class TelnetServer {
    private final List<PrintWriter> clientWriters = new ArrayList<>();

    public synchronized void send(final String message) {
        for (PrintWriter writer : clientWriters) {
            writer.println(message);
            writer.flush();
        }
    }

    public synchronized void addClient(Socket clientSocket) {
        try {
            PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true);
            clientWriters.add(writer);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public synchronized void removeClient(PrintWriter writer) {
        clientWriters.remove(writer);
    }
}