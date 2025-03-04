def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re
    
    # Regular expression for finding URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Regular expression for finding HTML links
    html_link_pattern = r'<a[^>]*>(.*?)<\/a>'
    
    # First process existing HTML links
    def add_attributes(match):
        link = match.group(0)
        if 'target=' not in link:
            link = link.replace('<a ', '<a target="_blank" rel="noopener noreferrer" ')
        return link
    
    text = re.sub(html_link_pattern, add_attributes, text)
    
    # Then convert plain URLs to HTML links
    def linkify(match):
        url = match.group(0)
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{match.group(0)}</a>'
    
    # Only linkify URLs that aren't already part of an HTML link
    parts = re.split(html_link_pattern, text)
    for i in range(0, len(parts), 2):
        parts[i] = re.sub(url_pattern, linkify, parts[i])
    
    return ''.join(parts)