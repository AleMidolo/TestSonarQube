import java.util.HashMap;
import java.util.Map;

public class MessagePrinter {
    private Map<String, Integer> messageTimestamps;

    public MessagePrinter() {
        messageTimestamps = new HashMap<>();
    }

    /** 
     * Restituisce true se il messaggio deve essere stampato nel timestamp fornito, 
     * altrimenti restituisce false. Se questo metodo restituisce false, il messaggio 
     * non verrà stampato. Il timestamp è in granularità di secondi. 
     */
    public boolean shouldPrintMessage(int timestamp, String message) {
        if (!messageTimestamps.containsKey(message)) {
            messageTimestamps.put(message, timestamp);
            return true;
        }

        int lastTimestamp = messageTimestamps.get(message);
        if (timestamp - lastTimestamp >= 10) {
            messageTimestamps.put(message, timestamp);
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
        MessagePrinter printer = new MessagePrinter();
        System.out.println(printer.shouldPrintMessage(1, "foo")); // true
        System.out.println(printer.shouldPrintMessage(2, "foo")); // false
        System.out.println(printer.shouldPrintMessage(11, "foo")); // true
    }
}