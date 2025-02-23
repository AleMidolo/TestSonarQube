def process_text_links(text):
    """
    Process links in text, adding some attributes and linkifying textual links.
    """
    import re

    # Function to convert plain text URLs into HTML links
    def linkify(match):
        url = match.group(0)
        return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{url}</a>'

    # Regular expression to find URLs in the text
    url_pattern = r'(https?://[^\s]+)'

    # Replace plain text URLs with linkified HTML links
    processed_text = re.sub(url_pattern, linkify, text)

    return processed_text