def is_none_string(val: any) -> bool:
    """
    यह फ़ंक्शन जांचता है कि दी गई स्ट्रिंग None मान का प्रतिनिधित्व करती है या नहीं।
    """
    if isinstance(val, str):
        # Convert string to lowercase and remove whitespace
        val = val.lower().strip()
        # Check if string represents None
        return val in ['none', 'null', 'nil']
    return False