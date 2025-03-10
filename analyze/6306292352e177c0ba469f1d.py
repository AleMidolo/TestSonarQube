import re
from typing import Set, Tuple, Callable

def find_tags(texto: str, reemplazador: Callable = None) -> Tuple[Set, str]:
    """
    Encuentra etiquetas en el texto.

    Intenta ignorar las etiquetas dentro de bloques de código.

    Opcionalmente, si se pasa un "replacer", también reemplazará la palabra de la etiqueta con el resultado de la función "replacer" llamada con la palabra de la etiqueta.

    Devuelve un conjunto de etiquetas y el texto original o reemplazado.
    """
    # Expresión regular para encontrar etiquetas que no estén dentro de bloques de código
    tag_pattern = re.compile(r'(?<!