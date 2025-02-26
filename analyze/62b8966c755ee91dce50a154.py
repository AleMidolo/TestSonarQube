def isoparse(self, dt_str):
    """
    एक ISO-8601 दिनांक और समय स्ट्रिंग को :class:`datetime.datetime` में पार्स करें।

    एक ISO-8601 दिनांक और समय स्ट्रिंग में एक दिनांक भाग होता है, जिसके बाद वैकल्पिक रूप से 
    समय भाग हो सकता है। दिनांक और समय भाग एक एकल कैरेक्टर सेपरेटर द्वारा अलग किए जाते हैं, 
    जो आधिकारिक मानक में ``T`` होता है। अधूरे दिनांक प्रारूप (जैसे ``YYYY-MM``) को समय भाग 
    के साथ *संयोजित नहीं* किया जा सकता।

    समर्थित दिनांक प्रारूप:

    सामान्य:
    - ``YYYY``
    - ``YYYY-MM`` या ``YYYYMM``
    - ``YYYY-MM-DD`` या ``YYYYMMDD``

    असामान्य:
    - ``YYYY-Www`` या ``YYYYWww`` - ISO सप्ताह (दिन डिफ़ॉल्ट रूप से 0 होता है)
    - ``YYYY-Www-D`` या ``YYYYWwwD`` - ISO सप्ताह और दिन

    ISO सप्ताह और दिन की संख्या :func:`datetime.date.isocalendar` के समान तर्क का पालन करती है।

    समर्थित समय प्रारूप:
    - ``hh``
    - ``hh:mm`` या ``hhmm``
    - ``hh:mm:ss`` या ``hhmmss``
    - ``hh:mm:ss.ssssss`` (6 उप-सेकंड अंकों तक)

    मध्यरात्रि (`hh`) के लिए एक विशेष मामला है, क्योंकि मानक 00:00 और 24:00 दोनों को 
    प्रतिनिधित्व के रूप में समर्थन करता है। दशमलव सेपरेटर एक डॉट या कॉमा हो सकता है।

    .. चेतावनी::

        सेकंड के अलावा अन्य भिन्नात्मक घटकों के लिए समर्थन ISO-8601 मानक का हिस्सा है, 
        लेकिन वर्तमान में इस पार्सर में लागू नहीं किया गया है।

    समर्थित समय क्षेत्र ऑफसेट प्रारूप:
    - `Z` (UTC)
    - `±HH:MM`
    - `±HHMM`
    - `±HH`

    ऑफसेट को :class:`dateutil.tz.tzoffset` ऑब्जेक्ट्स के रूप में दर्शाया जाएगा, 
    सिवाय UTC के, जिसे :class:`dateutil.tz.tzutc` के रूप में दर्शाया जाएगा। UTC के 
    समकक्ष समय क्षेत्र ऑफसेट (जैसे `+00:00`) को भी :class:`dateutil.tz.tzutc` के रूप में 
    दर्शाया जाएगा।

    :param dt_str:
        एक स्ट्रिंग या स्ट्रीम जिसमें केवल एक ISO-8601 दिनांक और समय स्ट्रिंग हो।

    :return:
        एक :class:`datetime.datetime` लौटाता है जो स्ट्रिंग का प्रतिनिधित्व करता है। 
        निर्दिष्ट नहीं किए गए घटक उनके न्यूनतम मान पर डिफ़ॉल्ट होते हैं।

    .. चेतावनी::

        संस्करण 2.7.0 से, पार्सर की सख्ती को अनुबंध का स्थिर हिस्सा नहीं माना जाना चाहिए। 
        कोई भी मान्य ISO-8601 स्ट्रिंग जो डिफ़ॉल्ट सेटिंग्स के साथ सही ढंग से पार्स होती है, 
        भविष्य के संस्करणों में सही ढंग से पार्स होती रहेगी, लेकिन अमान्य स्ट्रिंग्स जो 
        वर्तमान में विफल होती हैं (जैसे ``2017-01-01T00:00+00:00:00``) भविष्य के संस्करणों 
        में विफल होने की गारंटी नहीं है यदि वे एक मान्य दिनांक को एन्कोड करती हैं।

    .. versionadded:: 2.7.0
    """
    from datetime import datetime, timedelta, timezone
    import re

    # Define regex patterns for parsing
    date_patterns = [
        r'(\d{4})-(\d{2})-(\d{2})',  # YYYY-MM-DD
        r'(\d{4})-(\d{2})',          # YYYY-MM
        r'(\d{4})',                   # YYYY
        r'(\d{4})W(\d{2})',           # YYYY-Www
        r'(\d{4})W(\d{2})(\d{1})'     # YYYY-Www-D
    ]
    
    time_patterns = [
        r'(\d{2}):(\d{2}):(\d{2})(\.\d+)?',  # hh:mm:ss[.sss...]
        r'(\d{2}):(\d{2})(\.\d+)?',          # hh:mm[.sss...]
        r'(\d{2})(\.\d+)?',                   # hh[.sss...]
    ]
    
    offset_patterns = [
        r'Z',                               # UTC
        r'([+-]\d{2}):?(\d{2})?',           # ±HH:MM
        r'([+-]\d{2})(\d{2})?',              # ±HHMM
        r'([+-]\d{2})'                       # ±HH
    ]
    
    # Combine patterns
    full_pattern = r'^\s*(' + '|'.join(date_patterns) + r')' + \
                   r'(T(' + '|'.join(time_patterns) + r')' + \
                   r'(?:(?P<offset>' + '|'.join(offset_patterns) + r'))?)?\s*$'
    
    match = re.match(full_pattern, dt_str)
    if not match:
        raise ValueError("Invalid ISO-8601 date string")
    
    # Extract date components
    date_parts = match.groups()[:3]
    if date_parts[0]:  # YYYY-MM-DD
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
    elif date_parts[3]:  # YYYY-Www-D
        year, week, day = int(date_parts[3]), int(date_parts[4]), int(date_parts[5])
        # Calculate the date from ISO week
        jan1 = datetime(year, 1, 1)
        first_monday = jan1 + timedelta(days=(7 - jan1.weekday()) % 7)
        date = first_monday + timedelta(weeks=week - 1, days=day - 1)
        year, month, day = date.year, date.month, date.day
    elif date_parts[4]:  # YYYY-Www
        year, week = int(date_parts[4]), int(date_parts[5])
        # Calculate the date from ISO week
        jan1 = datetime(year, 1, 1)
        first_monday = jan1 + timedelta(days=(7 - jan1.weekday()) % 7)
        date = first_monday + timedelta(weeks=week - 1)
        year, month, day = date.year, date.month, date.day
    elif date_parts[6]:  # YYYY-MM
        year, month = int(date_parts[6]), int(date_parts[7])
        day = 1
    else:  # YYYY
        year = int(date_parts[8])
        month = day = 1

    # Extract time components
    time_parts = match.group(10)
    if time_parts:
        time_components = time_parts.split(':')
        hour = int(time_components[0])
        minute = int(time_components[1]) if len(time_components) > 1 else 0
        second = int(time_components[2]) if len(time_components) > 2 else 0
        microsecond = int(time_components[3][1:]) if len(time_components) > 3 else 0
    else:
        hour = minute = second = microsecond = 0

    # Handle offset
    offset_str = match.group('offset')
    if offset_str == 'Z':
        tzinfo = timezone.utc
    elif offset_str:
        if ':' in offset_str:
            sign, hours, minutes = re.match(r'([+-])(\d{2}):?(\d{2})?', offset_str).groups()
            offset = int(hours) * 3600 + (int(minutes) if minutes else 0) * 60
        else:
            sign, hours = re.match(r'([+-])(\d{2})', offset_str).groups()
            offset = int(hours) * 3600
        if sign == '-':
            offset = -offset
        tzinfo = timezone(timedelta(seconds=offset))
    else:
        tzinfo = None

    # Create datetime object
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo)