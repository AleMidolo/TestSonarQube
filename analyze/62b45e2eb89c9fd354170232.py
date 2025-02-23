def next_version(version):
    """
    दिए गए संस्करण पैटर्न के अनुसार अगला संस्करण पहचानकर्ता प्राप्त करें।

    यह फ़ंक्शन शून्य-प्रिफिक्स (zero-prefixed) और गैर-शून्य-प्रिफिक्स (non-zero prefixed) दोनों प्रकार के संस्करणों को संभालने में सक्षम होना चाहिए।
    """
    # Split the version into its components
    parts = version.split('.')
    
    # Convert the last part to an integer and increment it
    last_part = int(parts[-1]) + 1
    
    # Check if we need to carry over to the next part
    if last_part >= 10:
        parts[-1] = str(last_part % 10)
        for i in range(len(parts) - 2, -1, -1):
            if last_part // 10 > 0:
                parts[i] = str(int(parts[i]) + 1)
                last_part //= 10
            else:
                break
        if last_part // 10 > 0:
            parts.insert(0, str(last_part // 10))
    else:
        parts[-1] = str(last_part)
    
    # Join the parts back together
    return '.'.join(parts)