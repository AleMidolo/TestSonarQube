def is_none_string(val: any) -> bool:
    """
    यह फ़ंक्शन जांचता है कि दी गई स्ट्रिंग None मान का प्रतिनिधित्व करती है या नहीं।
    """
    if isinstance(val, str):
        return val.lower() in ['none', 'null', 'nil', 'nan']
    return False