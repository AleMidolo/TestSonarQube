import java.util.regex.Matcher;
import java.util.regex.Pattern;

public final class UriMatcher {
    private final Pattern pattern;

    public UriMatcher(String template) {
        this.pattern = Pattern.compile(template);
    }

    /**
     * Confronta un URI con il modello.
     * @param uri l'uri da confrontare con il template.
     * @return il risultato della corrispondenza, altrimenti null se non si verifica alcuna corrispondenza.
     */
    public final MatchResult match(CharSequence uri) {
        Matcher matcher = pattern.matcher(uri);
        if (matcher.matches()) {
            return new MatchResult(matcher);
        }
        return null;
    }
}

class MatchResult {
    private final Matcher matcher;

    public MatchResult(Matcher matcher) {
        this.matcher = matcher;
    }

    // Additional methods to retrieve matched groups can be added here
}