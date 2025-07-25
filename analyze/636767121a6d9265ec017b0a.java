public class HeaderParser {

    /** 
     * Salta i byte fino alla fine della riga corrente.
     * @param headerPart Le intestazioni che vengono analizzate.
     * @param end Indice dell'ultimo byte che deve ancora essere elaborato.
     * @return Indice della sequenza \r\n, che indica la fine della riga.
     */
    private int parseEndOfLine(String headerPart, int end) {
        int i = end;
        while (i < headerPart.length()) {
            if (headerPart.charAt(i) == '\r') {
                if (i + 1 < headerPart.length() && headerPart.charAt(i + 1) == '\n') {
                    return i + 1; // Return the index after \r\n
                }
            }
            i++;
        }
        return headerPart.length(); // Return the length if \r\n is not found
    }

    public static void main(String[] args) {
        HeaderParser parser = new HeaderParser();
        String headers = "Header1: value1\r\nHeader2: value2\r\n";
        int endIndex = parser.parseEndOfLine(headers, 0);
        System.out.println("End of line index: " + endIndex);
    }
}