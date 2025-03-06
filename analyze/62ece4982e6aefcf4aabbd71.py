import re

def regex_dict(item):
    """
    Convertir claves `*.cpp` a claves de expresiones regulares.

    Dado un diccionario donde las claves son nombres de archivo con comodines, convierte únicamente las claves en expresiones regulares equivalentes y deja los valores intactos.

    Ejemplo
    rules = {
        '*.cpp': {'a': 'arf', 'b': 'bark', 'c': 'coo'},
        '*.h': {'h': 'help'}
    }

    regex_keys = regex_dict(rules)

        Argumentos:
            item (dict): Diccionario a convertir.

        Retorno:
            dict: Diccionario con claves convertidas a expresiones regulares.
    """
    regex_dict = {}
    for key, value in item.items():
        # Convertir el comodín * a .* en la expresión regular
        regex_key = re.escape(key).replace('\\*', '.*')
        regex_dict[regex_key] = value
    return regex_dict