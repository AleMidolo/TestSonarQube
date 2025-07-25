import com.google.gson.JsonObject;
import java.util.HashMap;
import java.util.Map;

private Map<String, Object> buildContent(JsonObject jsonObject) {
    Map<String, Object> content = new HashMap<>();
    
    if (jsonObject.has("ATS")) {
        content.put("ATS", jsonObject.get("ATS").getAsString());
    }
    
    return content;
}