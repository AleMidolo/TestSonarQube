import org.atmosphere.cpr.AtmosphereResource;
import org.atmosphere.cpr.Action;

public class MyAtmosphereHandler {

    /**
     * Sospende automaticamente il {@link AtmosphereResource} in base al valore di {@link AtmosphereResource.TRANSPORT}.
     * @param r un {@link AtmosphereResource}
     * @return {@link Action#CONTINUE}
     */
    @Override
    public Action inspect(AtmosphereResource r) {
        // Check the transport type and suspend the resource accordingly
        if (r.getTransport() != null) {
            // Logic to suspend the resource based on transport type
            // For example, if the transport is WebSocket, we might want to suspend it
            if (r.getTransport().equals(AtmosphereResource.TRANSPORT.WEBSOCKET)) {
                r.suspend();
            }
        }
        return Action.CONTINUE;
    }
}