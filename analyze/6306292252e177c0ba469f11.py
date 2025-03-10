from datetime import datetime

def format_dt(dt):
    """
    D* नोड्स जिस प्रकार की datetime अपेक्षा करते हैं, उस प्रारूप में datetime को प्रारूपित करें।
    """
    if isinstance(dt, datetime):
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        raise ValueError("Input must be a datetime object")