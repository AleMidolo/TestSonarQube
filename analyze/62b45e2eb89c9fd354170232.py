def next_version(version):
    """
    दिए गए संस्करण पैटर्न के अनुसार अगला संस्करण पहचानकर्ता प्राप्त करें।

    यह फ़ंक्शन शून्य-प्रिफिक्स (zero-prefixed) और गैर-शून्य-प्रिफिक्स (non-zero prefixed) दोनों प्रकार के संस्करणों को संभालने में सक्षम होना चाहिए।
    """
    # Split the version string into parts
    parts = version.split('.')
    
    # Convert each part to an integer
    parts = [int(part) for part in parts]
    
    # Increment the last part
    parts[-1] += 1
    
    # Handle carry-over if any part exceeds 9
    for i in range(len(parts) - 1, 0, -1):
        if parts[i] > 9:
            parts[i] = 0
            parts[i - 1] += 1
    
    # Convert back to string
    next_version_str = '.'.join(map(str, parts))
    
    return next_version_str