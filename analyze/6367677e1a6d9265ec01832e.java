import java.util.logging.Logger;

public class LoggerChecker {
    
    /** 
     * Controlla se il logger con il nome specificato esiste nella gerarchia. Se sì, restituisce il suo riferimento, altrimenti restituisce <code>null</code>.
     * @param name Il nome del logger da cercare.
     */
    public Logger exists(String name) {
        Logger logger = Logger.getLogger(name);
        return logger.getHandlers().length > 0 ? logger : null;
    }

    public static void main(String[] args) {
        LoggerChecker checker = new LoggerChecker();
        Logger logger = checker.exists("myLogger");
        if (logger != null) {
            System.out.println("Logger found: " + logger.getName());
        } else {
            System.out.println("Logger not found.");
        }
    }
}