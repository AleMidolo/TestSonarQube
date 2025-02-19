private void pop(final String descriptor) {
    // Controlla se il descrittore è un tipo di metodo
    if (descriptor.startsWith("(") && descriptor.contains(")")) {
        // Estrae i tipi di argomento dal descrittore
        int start = descriptor.indexOf('(') + 1;
        int end = descriptor.indexOf(')');
        String args = descriptor.substring(start, end);
        
        // Rimuove i tipi di argomento dallo stack
        while (args.length() > 0) {
            char type = args.charAt(0);
            args = args.substring(1);
            removeTypeFromStack(type);
        }
    } else {
        // Rimuove il tipo specificato dallo stack
        removeTypeFromStack(descriptor.charAt(0));
    }
}

private void removeTypeFromStack(char type) {
    // Logica per rimuovere il tipo dallo stack
    // Implementazione specifica dipendente dal contesto
}