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
    date_pattern = r'(\d{4})(?:-(\d{2})(?:-(\d{2}))?)?(?:W(\d{2})(?:-?(\d))?)?'
    time_pattern = r'(\d{2})(?::(\d{2})(?::(\d{2})(?:\.(\d+))?)?)?'
    offset_pattern = r'Z|([+-]\d{2}):?(\d{2})?|([+-]\d{2})(\d{2})?|([+-]\d{2})'

    # Split date and time
    if 'T' in dt_str:
        date_str, time_str = dt_str.split('T', 1)
    else:
        date_str, time_str = dt_str, ''

    # Parse date
    date_match = re.match(date_pattern, date_str)
    if not date_match:
        raise ValueError("Invalid date format")

    year, month, day, week, weekday = date_match.groups()
    year = int(year)
    if month is not None:
        month = int(month)
    if day is not None:
        day = int(day)
    if week is not None:
        week = int(week)
    if weekday is not None:
        weekday = int(weekday)

    if week is not None:
        # ISO week date
        if weekday is None:
            weekday = 1  # Default to Monday
        date = datetime.fromisocalendar(year, week, weekday)
    else:
        # Regular date
        if month is None:
            month = 1  # Default to January
        if day is None:
            day = 1  # Default to the first day of the month
        date = datetime(year, month, day)

    # Parse time
    time_match = re.match(time_pattern, time_str)
    if time_match:
        hour, minute, second, microsecond = time_match.groups()
        hour = int(hour) if hour else 0
        minute = int(minute) if minute else 0
        second = int(second) if second else 0
        microsecond = int(microsecond.ljust(6, '0')) if microsecond else 0
    else:
        hour, minute, second, microsecond = 0, 0, 0, 0

    # Handle midnight case
    if hour == 24:
        hour = 0
        date += timedelta(days=1)

    # Combine date and time
    dt = date.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)

    # Parse offset
    offset_match = re.search(offset_pattern, dt_str)
    if offset_match:
        if offset_match.group(0) == 'Z':
            tzinfo = timezone.utc
        else:
            sign = offset_match.group(1) or offset_match.group(3) or offset_match.group(5)
            if sign:
                sign = 1 if sign[0] == '+' else -1
                hours = int(offset_match.group(2) or offset_match.group(4) or offset_match.group(6))
                minutes = int(offset_match.group(2) or 0)
                tzinfo = timezone(timedelta(hours=sign * hours, minutes=sign * minutes))
            else:
                tzinfo = None
    else:
        tzinfo = None

    if tzinfo:
        dt = dt.replace(tzinfo=tzinfo)

    return dt