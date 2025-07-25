public class Entity {
    
    /**
     * @return l'id della riga
     */
    public String id(String entityId) {
        // Assuming the entityId is the row ID we want to return
        return entityId;
    }

    public static void main(String[] args) {
        Entity entity = new Entity();
        String rowId = entity.id("12345");
        System.out.println("L'id della riga è: " + rowId);
    }
}