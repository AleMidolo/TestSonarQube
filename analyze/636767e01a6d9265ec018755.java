private Map<String,Object> buildContent(JsonObject jsonObject) {
    Map<String, Object> content = new HashMap<>();
    
    if (jsonObject.has("ATS")) {
        content.put("ATS", jsonObject.get("ATS").getAsString());
    }
    
    // Add other content building logic here if needed
    
    return content;
}