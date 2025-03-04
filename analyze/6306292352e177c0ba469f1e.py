def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re
    
    # Regular expression for finding URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Find existing HTML links and add attributes
    html_link_pattern = r'<a[^>]*?href=[\'"](.*?)[\'"][^>]*?>(.*?)<\/a>'
    
    def replace_html_link(match):
        url = match.group(1)
        text = match.group(2)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{text}</a>'
    
    # First process existing HTML links
    text = re.sub(html_link_pattern, replace_html_link, text)
    
    # Then find and convert plain text URLs to links
    def replace_url(match):
        url = match.group(0)
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{match.group(0)}</a>'
    
    # Only convert URLs that aren't already part of an HTML link
    parts = re.split(html_link_pattern, text)
    result = []
    
    for i, part in enumerate(parts):
        if i % 3 == 0:  # Not part of an existing link
            result.append(re.sub(url_pattern, replace_url, part))
        else:  # Part of an existing link, keep as is
            result.append(part)
            
    return ''.join(result)