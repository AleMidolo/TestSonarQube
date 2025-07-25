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
            # Remove any whitespace and convert to string
            bookmark = str(value).strip()
            if bookmark:  # Only add non-empty bookmarks
                bookmarks.append(bookmark)
        except (ValueError, TypeError):
            # Skip invalid values
            continue
            
    return cls(bookmarks)