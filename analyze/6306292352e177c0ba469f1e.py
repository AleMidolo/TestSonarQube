def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    import re

    # Función para reemplazar enlaces de texto por hipervínculos
    def replace_link(match):
        url = match.group(1)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    # Expresión regular para encontrar enlaces
    link_pattern = r'(https?://[^\s]+)'

    # Reemplazar enlaces en el texto
    processed_text = re.sub(link_pattern, replace_link, text)

    return processed_text