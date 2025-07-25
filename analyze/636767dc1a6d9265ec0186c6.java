public class FieldChecker {

    private Fields storedFields;

    /**
     * Restituisce true quando i campi di input sono già stati memorizzati nelle proprietà.
     */
    private boolean containsAllFields(Fields fields) {
        if (storedFields == null || fields == null) {
            return false;
        }
        
        return storedFields.equals(fields);
    }

    // Assuming Fields class has been defined elsewhere
    public void setStoredFields(Fields fields) {
        this.storedFields = fields;
    }
    
    public static void main(String[] args) {
        // Example usage
        FieldChecker checker = new FieldChecker();
        Fields fields1 = new Fields(); // Assume Fields has a default constructor
        Fields fields2 = new Fields(); // Assume Fields has a default constructor
        
        checker.setStoredFields(fields1);
        System.out.println(checker.containsAllFields(fields2)); // Should print false
    }
}