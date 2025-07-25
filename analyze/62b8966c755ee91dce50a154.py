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
        r'(\d{4})-(\d{2})',           # YYYY-MM
        r'(\d{4})',                    # YYYY
        r'(\d{4})W(\d{2})',            # YYYY-Www
        r'(\d{4})W(\d{2})-(\d)',       # YYYY-Www-D
    ]

    time_patterns = [
        r'(\d{2}):(\d{2}):(\d{2})(\.\d+)?',  # hh:mm:ss[.sss...]
        r'(\d{2}):(\d{2})(\.\d+)?',          # hh:mm[.sss...]
        r'(\d{2})(\.\d+)?',                  # hh[.sss...]
    ]

    offset_patterns = [
        r'Z',                               # UTC
        r'([+-]\d{2}):?(\d{2})?',           # ±HH:MM
        r'([+-]\d{2})(\d{2})?',              # ±HHMM
        r'([+-]\d{2})'                       # ±HH
    ]

    # Combine patterns
    date_regex = re.compile(r'|'.join(date_patterns))
    time_regex = re.compile(r'|'.join(time_patterns))
    offset_regex = re.compile(r'|'.join(offset_patterns))

    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''

    # Parse date
    date_match = date_regex.fullmatch(date_str)
    if not date_match:
        raise ValueError(f"Invalid date format: {date_str}")

    year, month, day = 1, 1, 1  # Default values
    if date_match.group(1):  # YYYY-MM-DD
        year = int(date_match.group(1))
        month = int(date_match.group(2)) if date_match.group(2) else 1
        day = int(date_match.group(3)) if date_match.group(3) else 1
    elif date_match.group(4):  # YYYY-Www
        year = int(date_match.group(5))
        week = int(date_match.group(6))
        day = 1  # Default to first day of the week
        # Calculate the date from the week number
        date = datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w").date()
        year, month, day = date.year, date.month, date.day
    elif date_match.group(7):  # YYYY-Www-D
        year = int(date_match.group(8))
        week = int(date_match.group(9))
        day = int(date_match.group(10))
        date = datetime.strptime(f'{year}-W{week}-{day}', "%Y-W%W-%w").date()
        year, month, day = date.year, date.month, date.day

    # Parse time
    hour, minute, second, microsecond = 0, 0, 0, 0  # Default values
    if time_str:
        time_match = time_regex.fullmatch(time_str)
        if not time_match:
            raise ValueError(f"Invalid time format: {time_str}")

        hour = int(time_match.group(1)) if time_match.group(1) else 0
        minute = int(time_match.group(2)) if time_match.group(2) else 0
        second = int(time_match.group(3)) if time_match.group(3) else 0
        microsecond = int(float(time_match.group(4) or 0) * 1_000_000) if time_match.group(4) else 0

    # Parse offset
    tzinfo = timezone.utc  # Default to UTC
    if time_str:
        offset_match = offset_regex.search(time_str)
        if offset_match:
            if offset_match.group(1) == 'Z':
                tzinfo = timezone.utc
            else:
                sign = 1 if offset_match.group(2) == '+' else -1
                hours = int(offset_match.group(3) or 0)
                minutes = int(offset_match.group(4) or 0)
                tzinfo = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))

    # Create datetime object
    return datetime(year, month, day, hour, minute, second, microsecond, tzinfo=tzinfo)