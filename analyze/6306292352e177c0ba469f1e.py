def process_text_links(text):
    import re
    
    # Regular expression pattern to find URLs in text
    url_pattern = r'(https?://[^\s<>"]+|www\.[^\s<>"]+)'
    
    # Function to replace URLs with HTML links
    def replace_with_link(match):
        url = match.group(0)
        # Add https:// if URL starts with www.
        if url.startswith('www.'):
            url = 'https://' + url
        # Create HTML link with target="_blank" to open in new tab
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Replace all URLs in text with HTML links
    processed_text = re.sub(url_pattern, replace_with_link, text)
    
    return processed_text