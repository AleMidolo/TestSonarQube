import re

def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    # Expresión regular para encontrar URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    
    # Función para reemplazar URLs con hipervínculos
    def replace_with_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Reemplazar todas las URLs en el texto con hipervínculos
    processed_text = url_pattern.sub(replace_with_link, text)
    
    return processed_text