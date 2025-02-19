public boolean isAttached(Appender appender) {
    if (appender == null) {
        return false;
    }
    for (Appender attachedAppender : this.appenders) {
        if (attachedAppender.equals(appender)) {
            return true;
        }
    }
    return false;
}