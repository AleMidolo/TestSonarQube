public class StringUnescaper {

    /** 
     * <p>Rimuove l'escape da qualsiasi letterale Java trovato nella <code>String</code>. Ad esempio, trasformerà una sequenza di <code>'\'</code> e <code>'n'</code> in un carattere di nuova linea, a meno che il <code>'\'</code> non sia preceduto da un altro <code>'\'</code>.</p>
     * @param str la <code>String</code> da desescapare, può essere null
     * @return una nuova <code>String</code> desescapata, <code>null</code> se l'input è una stringa null
     */
    public static String unescapeJava(String str) throws Exception {
        if (str == null) {
            return null;
        }

        StringBuilder result = new StringBuilder();
        boolean isEscaped = false;

        for (char c : str.toCharArray()) {
            if (isEscaped) {
                switch (c) {
                    case 'n':
                        result.append('\n');
                        break;
                    case 't':
                        result.append('\t');
                        break;
                    case 'r':
                        result.append('\r');
                        break;
                    case 'f':
                        result.append('\f');
                        break;
                    case 'b':
                        result.append('\b');
                        break;
                    case '\"':
                        result.append('\"');
                        break;
                    case '\'':
                        result.append('\'');
                        break;
                    case '\\':
                        result.append('\\');
                        break;
                    default:
                        result.append(c);
                        break;
                }
                isEscaped = false;
            } else {
                if (c == '\\') {
                    isEscaped = true;
                } else {
                    result.append(c);
                }
            }
        }

        // If the last character was an escape character, append it
        if (isEscaped) {
            result.append('\\');
        }

        return result.toString();
    }

    public static void main(String[] args) {
        try {
            String input = "Hello\\nWorld! This is a test\\tstring with escaped characters.";
            String output = unescapeJava(input);
            System.out.println(output);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}