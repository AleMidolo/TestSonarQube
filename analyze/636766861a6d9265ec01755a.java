import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class UriMatcher {
    private final Pattern pattern;

    public UriMatcher(String template) {
        // Convert the template into a regex pattern
        String regex = template.replace("{", "(?<").replace("}", ">[^/]+)");
        this.pattern = Pattern.compile(regex);
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

    public static class MatchResult {
        private final Matcher matcher;

        public MatchResult(Matcher matcher) {
            this.matcher = matcher;
        }

        public String getGroup(String name) {
            return matcher.group(name);
        }
    }

    public static void main(String[] args) {
        UriMatcher uriMatcher = new UriMatcher("/users/{userId}/posts/{postId}");
        MatchResult result = uriMatcher.match("/users/123/posts/456");
        if (result != null) {
            System.out.println("Matched userId: " + result.getGroup("userId"));
            System.out.println("Matched postId: " + result.getGroup("postId"));
        } else {
            System.out.println("No match found.");
        }
    }
}