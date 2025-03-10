def force_string(obj):
    """
    यह फ़ंक्शन UTF-8 का उपयोग करके `obj` के लिए संबंधित बाइट्स ऑब्जेक्ट लौटाता है, यदि `obj` एक स्ट्रिंग है।
    """
    if isinstance(obj, str):
        return obj.encode('utf-8')
    else:
        raise TypeError("Input must be a string")