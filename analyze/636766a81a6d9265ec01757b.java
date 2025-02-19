@SuppressWarnings("unchecked") 
public String toString(JSONWriter.Feature... features) {
    JSONObject jsonObject = new JSONObject();
    // Assuming we have some data to serialize, for example:
    jsonObject.put("key1", "value1");
    jsonObject.put("key2", "value2");
    
    // Create a JSONWriter with the specified features
    JSONWriter writer = new JSONWriter();
    for (JSONWriter.Feature feature : features) {
        writer.config(feature, true);
    }
    
    // Serialize the JSONObject to a JSON string
    return writer.write(jsonObject);
}