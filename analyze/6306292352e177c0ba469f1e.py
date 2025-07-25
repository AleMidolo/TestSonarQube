def process_text_links(text):
    import re
    
    # Regular expression pattern to find URLs in text
    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
    
    # Find all URLs in the text
    urls = re.findall(url_pattern, text)
    
    # Replace each URL with an HTML hyperlink
    for url in urls:
        # If URL starts with www, add https://
        if url.startswith('www.'):
            full_url = 'https://' + url
        else:
            full_url = url
            
        # Create HTML hyperlink
        hyperlink = f'<a href="{full_url}" target="_blank" rel="noopener noreferrer">{url}</a>'
        
        # Replace URL with hyperlink in text
        text = text.replace(url, hyperlink)
        
    return text