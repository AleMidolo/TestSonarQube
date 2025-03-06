def _normalizeargs(sequence, output=None):
    """
    Normalizza gli argomenti della dichiarazione

    Gli argomenti di normalizzazione possono contenere Dichiarazioni, tuple o singole
    interfacce.

    Qualsiasi cosa diversa da interfacce individuali o specifiche di implementazione verrà espansa.
    """
    if output is None:
        output = []
    
    for item in sequence:
        if isinstance(item, (list, tuple)):
            _normalizeargs(item, output)
        else:
            output.append(item)
    
    return output