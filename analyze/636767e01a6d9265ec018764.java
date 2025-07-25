import com.google.gson.JsonObject;
import java.util.List;

class KeyStringValuePair {
    private String key;
    private String value;

    public KeyStringValuePair(String key, String value) {
        this.key = key;
        this.value = value;
    }

    public String getKey() {
        return key;
    }

    public String getValue() {
        return value;
    }
}

public class PropertyConverter {

    /** 
     * Converte le proprietà del processo in dati sorgente
     */
    private JsonObject convertProperties(List<KeyStringValuePair> properties) {
        JsonObject jsonObject = new JsonObject();
        for (KeyStringValuePair pair : properties) {
            jsonObject.addProperty(pair.getKey(), pair.getValue());
        }
        return jsonObject;
    }
}