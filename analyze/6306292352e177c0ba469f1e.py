def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re
    
    # Regular expression for finding URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Find all HTML links
    html_link_pattern = r'<a[^>]*>(.*?)<\/a>'
    
    # Process existing HTML links - add target="_blank" and rel="noopener noreferrer"
    def process_html_link(match):
        link = match.group(0)
        if 'target=' not in link:
            link = link.replace('<a ', '<a target="_blank" ')
        if 'rel=' not in link:
            link = link.replace('<a ', '<a rel="noopener noreferrer" ')
        return link
    
    # Process plain text URLs - convert to HTML links
    def process_url(match):
        url = match.group(0)
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{match.group(0)}</a>'
    
    # First process existing HTML links
    text = re.sub(html_link_pattern, process_html_link, text)
    
    # Then find and process plain text URLs, but ignore URLs that are already part of an HTML link
    processed_text = ''
    last_end = 0
    
    for match in re.finditer(html_link_pattern, text):
        # Add text before the link
        processed_text += re.sub(url_pattern, process_url, text[last_end:match.start()])
        # Add the link itself unchanged
        processed_text += match.group(0)
        last_end = match.end()
    
    # Process remaining text after last link
    processed_text += re.sub(url_pattern, process_url, text[last_end:])
    
    return processed_text