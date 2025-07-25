import javax.servlet.http.HttpServletRequest;
import org.atmosphere.cpr.AtmosphereRequest;

public class RequestWrapper {

    /** 
     * Fornisce un {@link HttpServletRequest}.
     * @param request {@link HttpServletRequest}
     * @return un {@link AtmosphereRequest}
     */
    public static AtmosphereRequest wrap(HttpServletRequest request) {
        // Create a new AtmosphereRequest using the provided HttpServletRequest
        return new AtmosphereRequest() {
            @Override
            public HttpServletRequest getRequest() {
                return request;
            }

            // Implement other methods as needed
            // This is a simplified version; you may need to implement additional methods
        };
    }
}