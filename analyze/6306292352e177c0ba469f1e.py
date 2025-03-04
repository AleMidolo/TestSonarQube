def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    import re

    # Patrón para detectar URLs
    url_pattern = r'(https?://[^\s<>"\'\(\)]+)'
    
    # Patrón para detectar enlaces de texto [texto](url)
    text_link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'

    # Reemplazar URLs simples con hipervínculos
    text = re.sub(url_pattern, 
                  r'<a href="\1" target="_blank" rel="noopener noreferrer">\1</a>', 
                  text)

    # Reemplazar enlaces de texto con hipervínculos
    text = re.sub(text_link_pattern,
                  r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
                  text)

    return text