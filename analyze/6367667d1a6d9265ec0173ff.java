import javax.servlet.http.HttpServletRequest;

public class MeteorLookup {

    /**
     * Recupera un'istanza di {@link Meteor} basata su {@link HttpServletRequest}.
     * @param r {@link HttpServletRequest}
     * @return un {@link Meteor} o null se non trovato
     */
    public static Meteor lookup(HttpServletRequest r) {
        // Simulazione di recupero di un'istanza di Meteor
        String meteorId = r.getParameter("meteorId");
        
        if (meteorId == null || meteorId.isEmpty()) {
            return null; // Se non c'è un ID meteor, restituisce null
        }
        
        // Logica per cercare un'istanza di Meteor basata sull'ID
        // Questo è solo un esempio, in un'applicazione reale si dovrebbe cercare in un database o in una collezione
        Meteor meteor = findMeteorById(meteorId);
        
        return meteor;
    }

    private static Meteor findMeteorById(String meteorId) {
        // Simulazione di ricerca di un Meteor
        // In un'applicazione reale, qui ci sarebbe la logica per recuperare l'oggetto Meteor da un database
        if ("123".equals(meteorId)) {
            return new Meteor(meteorId, "Meteor Name"); // Restituisce un esempio di Meteor
        }
        return null; // Se non trovato
    }
}

class Meteor {
    private String id;
    private String name;

    public Meteor(String id, String name) {
        this.id = id;
        this.name = name;
    }

    // Getters e Setters
    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}