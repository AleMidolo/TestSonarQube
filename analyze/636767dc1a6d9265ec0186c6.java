private boolean containsAllFields(Fields fields) {
    return fields != null && 
           fields.getField1() != null && 
           fields.getField2() != null && 
           fields.getField3() != null; // Assuming there are three fields to check
}