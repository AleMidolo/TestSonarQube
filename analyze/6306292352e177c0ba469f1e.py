def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    import re

    # Expresión regular para encontrar enlaces
    url_pattern = r'(https?://[^\s]+)'
    
    # Función para reemplazar el enlace encontrado
    def replace_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Reemplazar los enlaces en el texto
    processed_text = re.sub(url_pattern, replace_link, text)
    
    return processed_text