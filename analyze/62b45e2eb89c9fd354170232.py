def next_version(version):
    """
    दिए गए संस्करण पैटर्न के अनुसार अगला संस्करण पहचानकर्ता प्राप्त करें।

    यह फ़ंक्शन शून्य-प्रिफिक्स (zero-prefixed) और गैर-शून्य-प्रिफिक्स (non-zero prefixed) दोनों प्रकार के संस्करणों को संभालने में सक्षम होना चाहिए।
    """
    # Split the version into its components
    parts = version.split('.')
    
    # Convert the last part to an integer and increment it
    last_part = int(parts[-1]) + 1
    
    # Check if we need to carry over
    if last_part == 10:
        last_part = 0
        # Increment the second last part
        if len(parts) > 1:
            second_last_part = int(parts[-2]) + 1
            parts[-2] = str(second_last_part)
        else:
            parts.append('1')  # If there's no second last part, we add it
    
    # Update the last part
    parts[-1] = str(last_part)
    
    # Join the parts back together
    return '.'.join(parts)