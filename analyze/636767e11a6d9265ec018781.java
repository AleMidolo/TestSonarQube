@Override 
public void accept(final METRICS data) {
    // Implementazione della logica per unire i dati nella cache con il valore esistente
    if (data != null) {
        // Supponiamo di avere una mappa per memorizzare i dati nella cache
        for (Map.Entry<KeyType, ValueType> entry : data.getEntries()) {
            KeyType key = entry.getKey();
            ValueType value = entry.getValue();
            // Unire il valore esistente con il nuovo valore
            if (cache.containsKey(key)) {
                ValueType existingValue = cache.get(key);
                // Logica per unire existingValue e value
                ValueType mergedValue = mergeValues(existingValue, value);
                cache.put(key, mergedValue);
            } else {
                cache.put(key, value);
            }
        }
    }
}

// Metodo per unire i valori
private ValueType mergeValues(ValueType existingValue, ValueType newValue) {
    // Implementare la logica di unione specifica per il tipo di valore
    // Questo è solo un esempio
    return existingValue.add(newValue); // Supponendo che ValueType abbia un metodo add
}