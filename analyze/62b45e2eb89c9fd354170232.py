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
    
    # Handle carry-over for parts other than the last one
    for i in range(len(parts) - 1, 0, -1):
        if parts[i] > 9:
            parts[i] = 0
            parts[i - 1] += 1
    
    # Convert parts back to strings
    parts = [str(part) for part in parts]
    
    # Join the parts with '.' to form the new version string
    new_version = '.'.join(parts)
    
    return new_version