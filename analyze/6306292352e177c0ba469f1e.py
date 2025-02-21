def process_text_links(text):
    """
    Elabora i collegamenti nel testo, aggiungendo alcuni attributi e trasformando i collegamenti testuali in link cliccabili.
    """
    import re

    def replace_link(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    # Regex per trovare i collegamenti nel testo
    url_pattern = r'(https?://[^\s]+)'
    processed_text = re.sub(url_pattern, replace_link, text)

    return processed_text