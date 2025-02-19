private void pop(final String descriptor) {
    // Controlla se il descrittore è un tipo di metodo
    if (descriptor.startsWith("(") && descriptor.contains(")")) {
        // Estrae i tipi di argomento dal descrittore
        int start = descriptor.indexOf('(') + 1;
        int end = descriptor.indexOf(')');
        String args = descriptor.substring(start, end);
        
        // Rimuove i tipi di argomento dallo stack
        for (String type : args.split(",")) {
            removeTypeFromStack(type.trim());
        }
    } else {
        // Rimuove il tipo specificato dallo stack
        removeTypeFromStack(descriptor);
    }
}

// Metodo ausiliario per rimuovere un tipo dallo stack
private void removeTypeFromStack(String type) {
    // Logica per rimuovere il tipo dallo stack
    // Implementazione specifica dipendente dal contesto
}