def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re
    
    # Regular expression for finding URLs
    url_pattern = r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})'
    
    # Find existing <a> tags
    a_tag_pattern = r'<a[^>]*>.*?</a>'
    
    # Split text to preserve existing <a> tags
    parts = re.split(a_tag_pattern, text)
    links = re.findall(a_tag_pattern, text)
    
    result = []
    for i, part in enumerate(parts):
        # Process plain text parts
        processed_part = re.sub(
            url_pattern,
            lambda m: f'<a href="{m.group(0)}" target="_blank" rel="noopener noreferrer">{m.group(0)}</a>',
            part
        )
        result.append(processed_part)
        
        # Add back preserved <a> tags
        if i < len(links):
            # Add target and rel attributes to existing links if they don't have them
            link = links[i]
            if 'target=' not in link:
                link = link.replace('<a ', '<a target="_blank" ')
            if 'rel=' not in link:
                link = link.replace('<a ', '<a rel="noopener noreferrer" ')
            result.append(link)
    
    return ''.join(result)