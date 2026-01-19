from datetime import datetime

def string_to_datetime(self, string):
    """
    समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
    :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
    :return: datetime उदाहरण
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    # Try common datetime formats
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue
    
    # If standard formats don't work, try parsing flexible format
    # Handle cases like "2001-7-18 1:1:1" where single digits aren't zero-padded
    try:
        parts = string.split()
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else "0:0:0"
        
        date_components = date_part.replace('/', '-').split('-')
        year = int(date_components[0])
        month = int(date_components[1])
        day = int(date_components[2])
        
        time_components = time_part.split(':')
        hour = int(time_components[0]) if len(time_components) > 0 else 0
        minute = int(time_components[1]) if len(time_components) > 1 else 0
        second = int(time_components[2]) if len(time_components) > 2 else 0
        
        return datetime(year, month, day, hour, minute, second)
    except (ValueError, IndexError):
        raise ValueError(f"Unable to parse datetime string: {string}")