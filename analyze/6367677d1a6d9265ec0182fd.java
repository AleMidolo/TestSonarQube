public static boolean toBoolean(String value, boolean dEfault) {
    if (value == null) {
        return dEfault;
    }
    value = value.trim().toLowerCase();
    if (value.equals("true")) {
        return true;
    } else if (value.equals("false")) {
        return false;
    } else {
        return dEfault;
    }
}