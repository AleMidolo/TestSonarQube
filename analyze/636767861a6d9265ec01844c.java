import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class AppenderManager {
    private List<String> appenders;

    public AppenderManager() {
        this.appenders = new ArrayList<>();
    }

    /**
     * Rimuove l'appender con il nome passato come parametro dalla lista degli appenders.  
     */
    public void removeAppender(String name) {
        Iterator<String> iterator = appenders.iterator();
        while (iterator.hasNext()) {
            String appender = iterator.next();
            if (appender.equals(name)) {
                iterator.remove();
                break;
            }
        }
    }

    public void addAppender(String name) {
        appenders.add(name);
    }

    public List<String> getAppenders() {
        return appenders;
    }
}