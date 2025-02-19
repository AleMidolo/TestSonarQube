private String unescapeId(String input) {
    if (input == null) {
        return null;
    }
    StringBuilder output = new StringBuilder();
    boolean escape = false;
    
    for (char c : input.toCharArray()) {
        if (escape) {
            switch (c) {
                case 'n':
                    output.append('\n');
                    break;
                case 't':
                    output.append('\t');
                    break;
                case '\\':
                    output.append('\\');
                    break;
                case '"':
                    output.append('"');
                    break;
                default:
                    output.append(c);
                    break;
            }
            escape = false;
        } else {
            if (c == '\\') {
                escape = true;
            } else {
                output.append(c);
            }
        }
    }
    
    return output.toString();
}