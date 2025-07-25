def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re
    
    # Regular expression for finding URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Find all HTML links in text
    html_link_pattern = r'<a[^>]*>.*?</a>'
    html_links = re.findall(html_link_pattern, text)
    
    # Process existing HTML links - add target="_blank" and rel="noopener noreferrer"
    for link in html_links:
        new_link = link.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        text = text.replace(link, new_link)
    
    # Find all raw URLs that aren't already in HTML links
    def replace_url(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'
    
    # Replace raw URLs with HTML links
    processed_text = re.sub(url_pattern, replace_url, text)
    
    return processed_text