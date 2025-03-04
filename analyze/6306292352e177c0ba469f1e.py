def process_text_links(text):
    import re
    
    # Regular expression to find URLs in text
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Process each URL and convert to hyperlink
    for url in urls:
        # Create HTML hyperlink
        hyperlink = f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
        
        # Replace URL with hyperlink in text
        text = text.replace(url, hyperlink)
        
    return text