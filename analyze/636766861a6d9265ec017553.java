public final boolean isTemplateVariablePresent(String name) {
    // Supponiamo di avere una lista di variabili di template
    List<String> templateVariables = Arrays.asList("var1", "var2", "var3"); // Esempio di variabili di template

    // Controlla se il nome fornito è presente nella lista delle variabili di template
    return templateVariables.contains(name);
}