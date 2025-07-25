def next_version(version):
    """
    दिए गए संस्करण पैटर्न के अनुसार अगला संस्करण पहचानकर्ता प्राप्त करें।

    यह फ़ंक्शन शून्य-प्रिफिक्स (zero-prefixed) और गैर-शून्य-प्रिफिक्स (non-zero prefixed) दोनों प्रकार के संस्करणों को संभालने में सक्षम होना चाहिए।
    """
    # Split the version into its components
    parts = version.split('.')
    
    # Convert the last part to an integer and increment it
    last_part = int(parts[-1]) + 1
    
    # Replace the last part with the incremented value
    parts[-1] = str(last_part)
    
    # Join the parts back together
    next_version = '.'.join(parts)
    
    return next_version