def is_local(host):
    """
    होस्ट की जाँच करता है कि क्या यह लोकलहोस्ट है।

    :param host: होस्टनाम या IP एड्रेस।
    :return: True यदि होस्ट लोकलहोस्ट है, अन्यथा False।
    """
    # List of common localhost hostnames and IPs
    localhost_values = [
        'localhost',
        '127.0.0.1',
        '::1',
        '0:0:0:0:0:0:0:1',
        '0.0.0.0'
    ]
    
    # Convert host to lowercase for case-insensitive comparison
    host = host.lower()
    
    # Check if host matches any localhost value
    if host in localhost_values:
        return True
        
    # Check if host starts with 127. (loopback IP range)
    if host.startswith('127.'):
        try:
            # Validate it's a proper IP address
            parts = host.split('.')
            if len(parts) == 4:
                for part in parts:
                    if not (part.isdigit() and 0 <= int(part) <= 255):
                        return False
                return True
        except:
            return False
            
    return False