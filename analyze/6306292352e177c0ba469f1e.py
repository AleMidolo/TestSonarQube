def process_text_links(text):
    """
    Elabora i collegamenti nel testo, aggiungendo alcuni attributi e trasformando i collegamenti testuali in link cliccabili.
    """
    import re
    
    # Pattern per trovare URL nel testo
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Pattern per trovare link in formato [testo](url)
    markdown_pattern = r'\[(.*?)\]\((.*?)\)'
    
    # Sostituisce gli URL semplici con link HTML
    text = re.sub(url_pattern, r'<a href="\1" target="_blank" rel="noopener noreferrer">\1</a>', text)
    
    # Sostituisce i link in formato markdown con link HTML
    text = re.sub(markdown_pattern, r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', text)
    
    return text