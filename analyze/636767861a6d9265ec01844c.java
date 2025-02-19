public void removeAppender(String name) {
    if (name == null || name.isEmpty()) {
        return;
    }
    for (Iterator<Appender> iterator = appenders.iterator(); iterator.hasNext();) {
        Appender appender = iterator.next();
        if (appender.getName().equals(name)) {
            iterator.remove();
            break;
        }
    }
}