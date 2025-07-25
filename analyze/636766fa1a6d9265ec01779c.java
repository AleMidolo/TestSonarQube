public class TokenParser {

    /**
     * Analizza un token fino a quando non viene incontrato uno dei caratteri terminatori forniti.
     * @param terminators l'array di caratteri terminatori. Qualsiasi di questi caratteri, quando incontrato, segna la fine del token
     * @return il token
     */
    private String parseToken(final char[] terminators) {
        StringBuilder token = new StringBuilder();
        int ch;

        try {
            while ((ch = System.in.read()) != -1) {
                char currentChar = (char) ch;
                if (isTerminator(currentChar, terminators)) {
                    break;
                }
                token.append(currentChar);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return token.toString();
    }

    private boolean isTerminator(char currentChar, char[] terminators) {
        for (char terminator : terminators) {
            if (currentChar == terminator) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        TokenParser parser = new TokenParser();
        char[] terminators = {' ', '\n', '\t', ',', '.'};
        String token = parser.parseToken(terminators);
        System.out.println("Parsed token: " + token);
    }
}