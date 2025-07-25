def process_text_links(text):
    """
    Elabora i collegamenti nel testo, aggiungendo alcuni attributi e trasformando i collegamenti testuali in link cliccabili.
    """
    import re

    # Pattern per trovare URL nel testo
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Funzione per sostituire gli URL con link HTML
    def replace_with_link(match):
        url = match.group(0)
        # Se l'URL non inizia con http/https, aggiungi http://
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        # Crea il link HTML con attributi target="_blank" e rel="noopener noreferrer"
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{match.group(0)}</a>'
    
    # Sostituisci tutti gli URL trovati con i link HTML
    processed_text = re.sub(url_pattern, replace_with_link, text)
    
    return processed_text