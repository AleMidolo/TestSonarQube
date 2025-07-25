def from_raw_values(cls, values):
    """
    कच्चे बुकमार्क स्ट्रिंग मानों की सूची से एक Bookmarks ऑब्जेक्ट बनाएं।

    इस विधि का उपयोग करने की आवश्यकता नहीं होनी चाहिए जब तक कि आप 
    बुकमार्क्स को डीसिरियलाइज़ (deserialize) करना न चाहें।

    :param values: ASCII स्ट्रिंग मान (कच्चे बुकमार्क्स)
    :type values: Iterable[str]
    """
    bookmarks = []
    for value in values:
        try:
            # Remove any whitespace and decode from ASCII
            cleaned_value = value.strip().encode('ascii', 'ignore').decode('ascii')
            if cleaned_value:  # Only add non-empty values
                bookmarks.append(cleaned_value)
        except (UnicodeError, AttributeError):
            # Skip any values that can't be properly encoded/decoded
            continue
            
    return cls(bookmarks)