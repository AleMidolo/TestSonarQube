import re
from typing import Set, Tuple, Callable

def find_tags(texto: str, reemplazador: Callable = None) -> Tuple[Set, str]:
    # Expresión regular para encontrar etiquetas que no estén dentro de bloques de código
    tag_pattern = re.compile(r'(?<!`)\b(\w+)\b(?!`)')
    
    # Encontrar todas las coincidencias de etiquetas
    tags = set(tag_pattern.findall(texto))
    
    # Si se proporciona un reemplazador, reemplazar las etiquetas en el texto
    if reemplazador is not None:
        def replace_tag(match):
            return reemplazador(match.group(1))
        
        texto_reemplazado = tag_pattern.sub(replace_tag, texto)
    else:
        texto_reemplazado = texto
    
    return tags, texto_reemplazado