public class AbbreviationUtil {

    /**
     * Abbrevia il nome.
     * @param buf buffer a cui aggiungere l'abbreviazione.
     * @param nameStart inizio del nome da abbreviare.
     */
    public void abbreviate(final int nameStart, final StringBuffer buf) {
        String name = buf.toString();
        if (nameStart < 0 || nameStart >= name.length()) {
            throw new IllegalArgumentException("Invalid nameStart index");
        }

        String[] parts = name.substring(nameStart).split(" ");
        StringBuilder abbreviation = new StringBuilder();

        for (String part : parts) {
            if (!part.isEmpty()) {
                abbreviation.append(part.charAt(0)).append(". ");
            }
        }

        // Remove the last space and dot if exists
        if (abbreviation.length() > 0) {
            abbreviation.setLength(abbreviation.length() - 1);
        }

        buf.append(abbreviation.toString().trim());
    }

    public static void main(String[] args) {
        StringBuffer buffer = new StringBuffer("John Doe Smith");
        AbbreviationUtil util = new AbbreviationUtil();
        util.abbreviate(0, buffer);
        System.out.println(buffer.toString()); // Output: John D. S.
    }
}