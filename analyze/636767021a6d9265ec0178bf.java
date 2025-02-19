@Override
protected Object convertToType(final Class<?> type, final Object value) throws Exception {
    if (value == null) {
        return null;
    }
    if (type == Character.class) {
        if (value instanceof String) {
            String strValue = (String) value;
            if (strValue.length() == 1) {
                return strValue.charAt(0);
            } else {
                throw new Exception("Cannot convert String to Character: String length is not 1.");
            }
        } else if (value instanceof Character) {
            return value;
        } else {
            throw new Exception("Cannot convert " + value.getClass().getName() + " to Character.");
        }
    }
    throw new Exception("Unsupported conversion to type: " + type.getName());
}