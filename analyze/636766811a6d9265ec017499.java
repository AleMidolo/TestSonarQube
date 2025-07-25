import java.util.List;

public class InterceptorChecker {

    /** 
     * <p> Controlla nella lista specificata se esiste almeno un'istanza della data classe di implementazione {@link AtmosphereInterceptor interceptor}. </p>
     * @param interceptorList gli interceptor
     * @param c               la classe dell'interceptor
     * @return {@code false} se un'istanza della classe esiste già nella lista, {@code true} altrimenti
     */
    private boolean checkDuplicate(final List<AtmosphereInterceptor> interceptorList, Class<? extends AtmosphereInterceptor> c) {
        for (AtmosphereInterceptor interceptor : interceptorList) {
            if (interceptor.getClass().equals(c)) {
                return false; // Esiste già un'istanza della classe
            }
        }
        return true; // Non esiste alcuna istanza della classe
    }
}

class AtmosphereInterceptor {
    // Implementazione della classe AtmosphereInterceptor
}