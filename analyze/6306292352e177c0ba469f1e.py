def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    import re

    # Patrón para detectar URLs
    url_pattern = r'(https?://[^\s<>]+)'
    
    # Patrón para detectar enlaces de texto [texto](url)
    text_link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

    # Primero procesar los enlaces de texto
    text = re.sub(text_link_pattern, 
                  lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener noreferrer">{m.group(1)}</a>', 
                  text)

    # Luego procesar las URLs directas
    text = re.sub(url_pattern,
                  lambda m: f'<a href="{m.group(1)}" target="_blank" rel="noopener noreferrer">{m.group(1)}</a>',
                  text)

    return text