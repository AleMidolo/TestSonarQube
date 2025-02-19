import java.util.logging.Logger;

public Logger exists(String name) {
    Logger logger = Logger.getLogger(name);
    return logger.getParent() != null ? logger : null;
}