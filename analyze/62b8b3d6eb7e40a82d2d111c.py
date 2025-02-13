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
        if isinstance(item, tuple):
            output.extend(_normalizeargs(item))
        elif isinstance(item, list):
            output.extend(_normalizeargs(item))
        elif isinstance(item, dict):
            for key, value in item.items():
                output.append((key, _normalizeargs(value)))
        else:
            output.append(item)

    return output