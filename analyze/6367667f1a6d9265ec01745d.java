import java.net.URI;
import java.util.ArrayList;
import java.util.List;

public static List<PathSegmentImpl> decodePath(URI u, boolean decode) {
    List<PathSegmentImpl> segments = new ArrayList<>();
    String path = u.getPath();
    
    // Ignore the leading '/' if it's an absolute path
    if (path.startsWith("/")) {
        path = path.substring(1);
    }
    
    String[] pathSegments = path.split("/");
    
    for (String segment : pathSegments) {
        if (decode) {
            segment = decodeSegment(segment);
        }
        segments.add(new PathSegmentImpl(segment));
    }
    
    return segments;
}

private static String decodeSegment(String segment) {
    try {
        return java.net.URLDecoder.decode(segment, "UTF-8");
    } catch (Exception e) {
        // Handle exception (e.g., log it)
        return segment; // Return the original segment if decoding fails
    }
}

class PathSegmentImpl {
    private String segment;

    public PathSegmentImpl(String segment) {
        this.segment = segment;
    }

    public String getSegment() {
        return segment;
    }
}