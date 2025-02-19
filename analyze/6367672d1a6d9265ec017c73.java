import java.util.HashMap;

public class MessagePrinter {
    private HashMap<String, Integer> messageTimestamps;

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
}