public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }
    
    StringBuilder result = new StringBuilder();
    boolean isEscaped = false;

    for (int i = 0; i < str.length(); i++) {
        char currentChar = str.charAt(i);
        
        if (isEscaped) {
            switch (currentChar) {
                case 'n':
                    result.append('\n');
                    break;
                case 't':
                    result.append('\t');
                    break;
                case 'r':
                    result.append('\r');
                    break;
                case 'b':
                    result.append('\b');
                    break;
                case 'f':
                    result.append('\f');
                    break;
                case '\\':
                    result.append('\\');
                    break;
                case '\'':
                    result.append('\'');
                    break;
                case '\"':
                    result.append('\"');
                    break;
                default:
                    result.append(currentChar);
                    break;
            }
            isEscaped = false;
        } else {
            if (currentChar == '\\') {
                isEscaped = true;
            } else {
                result.append(currentChar);
            }
        }
    }

    return result.toString();
}