import re
from typing import Set, Tuple, Callable

def find_tags(texto: str, reemplazador: Callable = None) -> Tuple[Set, str]:
    # Expresión regular para encontrar etiquetas que no estén dentro de bloques de código
    tag_pattern = re.compile(r'(?<!`)\B#(\w+)\b(?!`)')
    
    # Encontrar todas las etiquetas en el texto
    tags = set(tag_pattern.findall(texto))
    
    # Si se proporciona un reemplazador, reemplazar las etiquetas en el texto
    if reemplazador is not None:
        def replace_tag(match):
            return reemplazador(match.group(1))
        texto = tag_pattern.sub(replace_tag, texto)
    
    return tags, texto