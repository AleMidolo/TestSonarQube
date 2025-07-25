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
                   r'(T(' + '|'.join(time_patterns) + r'))?' + \
                   r'(\s*(' + '|'.join(offset_patterns) + r'))?\s*$'
    
    match = re.match(full_pattern, dt_str)
    if not match:
        raise ValueError("Invalid ISO-8601 date string")
    
    # Extract date components
    date_parts = match.groups()[:6]
    year, month, day = None, None, None
    
    if date_parts[0]:  # YYYY-MM-DD
        year, month, day = int(date_parts[0]), int(date_parts[1]), int(date_parts[2])
    elif date_parts[3]:  # YYYY-Www-D
        year, week, day = int(date_parts[3]), int(date_parts[4]), int(date_parts[5])
        # Calculate the date from ISO week
        jan1 = datetime(year, 1, 1)
        first_monday = jan1 + timedelta(days=(7 - jan1.weekday()) % 7)
        date = first_monday + timedelta(weeks=week - 1, days=day - 1)
        year, month, day = date.year, date.month, date.day
    elif date_parts[3]:  # YYYY-Www
        year, week = int(date_parts[3]), int(date_parts[4])
        # Calculate the date from ISO week
        jan1 = datetime(year, 1, 1)
        first_monday = jan1 + timedelta(days=(7 - jan1.weekday()) % 7)
        date = first_monday + timedelta(weeks=week - 1)
        year, month, day = date.year, date.month, date.day
    elif date_parts[0]:  # YYYY-MM
        year, month = int(date_parts[0]), int(date_parts[1])
        day = 1  # Default to the first day of the month
    elif date_parts[0]:  # YYYY
        year = int(date_parts[0])
        month, day = 1, 1  # Default to the first day of the first month

    # Extract time components
    time_parts = match.groups()[6:10]
    hour, minute, second, microsecond = 0, 0, 0, 0
    
    if time_parts[0]:  # hh:mm:ss[.sss...]
        hour, minute, second = int(time_parts[0]), int(time_parts[1]), int(time_parts[2])
        if time_parts[3]:
            microsecond = int(float(time_parts[3]) * 1_000_000)
    elif time_parts[0]:  # hh:mm[.sss...]
        hour, minute = int(time_parts[0]), int(time_parts[1])
        if time_parts[2]:
            microsecond = int(float(time_parts[2]) * 1_000_000)
    elif time_parts[0]:  # hh[.sss...]
        hour = int(time_parts[0])
        if time_parts[1]:
            microsecond = int(float(time_parts[1]) * 1_000_000)

    # Handle midnight case
    if hour == 24:
        hour = 0
        day += 1  # Increment day

    # Extract offset
    offset_parts = match.groups()[10:14]
    tzinfo = None
    
    if offset_parts[0] == 'Z':
        tzinfo = timezone.utc
    elif offset_parts[1]:
        sign = 1 if offset_parts[1][0] == '+' else -1
        hours = int(offset_parts[1][1:3])
        minutes = int(offset_parts[1][3:5]) if len(offset_parts[1]) > 3 else 0
        tzinfo = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
    elif offset_parts[2]:
        sign = 1 if offset_parts[2][0] == '+' else -1
        hours = int(offset_parts[2][1:3])
        tzinfo = timezone(timedelta(hours=sign * hours))
    
    # Create datetime object
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo)