def match_pubdate(node, pubdate_xpaths):
    """
    `pubdate_xpaths` सूची में पहला मेलित मान (match) लौटाता है।
    """
    for xpath in pubdate_xpaths:
        try:
            # Try to find matching element using xpath
            match = node.xpath(xpath)
            if match:
                # Return first matching value if found
                return match[0]
        except:
            # Skip any xpath that causes errors
            continue
    
    # Return None if no matches found
    return None