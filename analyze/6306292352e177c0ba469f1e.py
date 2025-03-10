import re

def process_text_links(text):
    """
    Procesa los enlaces en el texto, añadiendo algunos atributos y convirtiendo enlaces de texto en hipervínculos.
    """
    # Expresión regular para encontrar URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    
    # Función para convertir URLs en hipervínculos
    def replace_with_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank">{url}</a>'
    
    # Reemplazar URLs en el texto con hipervínculos
    processed_text = url_pattern.sub(replace_with_link, text)
    
    return processed_text