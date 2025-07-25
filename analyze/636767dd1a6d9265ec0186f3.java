import java.util.HashMap;
import java.util.Map;

public class ColumnName {
    private Map<String, String> nameMapping;

    public ColumnName() {
        nameMapping = new HashMap<>();
    }

    /** 
     * Mantieni lo stesso nome da sostituire come {@link ColumnName#overrideName(String,String)}
     * @param oldName da sostituire.
     * @param newName da utilizzare a livello di archiviazione.
     */
    public void overrideName(String oldName, String newName) {
        if (oldName == null || newName == null) {
            throw new IllegalArgumentException("Names cannot be null");
        }
        nameMapping.put(oldName, newName);
    }

    public String getNewName(String oldName) {
        return nameMapping.getOrDefault(oldName, oldName);
    }

    public static void main(String[] args) {
        ColumnName columnName = new ColumnName();
        columnName.overrideName("old_column", "new_column");
        System.out.println(columnName.getNewName("old_column")); // Output: new_column
        System.out.println(columnName.getNewName("another_column")); // Output: another_column
    }
}