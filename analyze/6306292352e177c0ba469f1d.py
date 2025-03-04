def find_tags(texto: str, reemplazador: callable = None) -> Tuple[Set, str]:
    """
    Encuentra etiquetas en el texto.

    Intenta ignorar las etiquetas dentro de bloques de código.

    Opcionalmente, si se pasa un "replacer", también reemplazará la palabra de la etiqueta con el resultado de la función "replacer" llamada con la palabra de la etiqueta.

    Devuelve un conjunto de etiquetas y el texto original o reemplazado.
    """
    tags = set()
    texto_modificado = texto
    in_code_block = False
    lines = texto.split('\n')
    
    for i, line in enumerate(lines):
        # Check for code block markers
        if line.strip().startswith('