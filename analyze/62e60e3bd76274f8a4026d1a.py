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
            # Remove any leading/trailing whitespace
            value = value.strip()
            
            # Skip empty lines
            if not value:
                continue
                
            # Parse the raw bookmark string and create bookmark object
            bookmark = cls._parse_raw_bookmark(value)
            if bookmark:
                bookmarks.append(bookmark)
                
        except Exception:
            # Skip any invalid bookmarks
            continue
            
    return cls(bookmarks)

@classmethod
def _parse_raw_bookmark(cls, raw_string):
    """Helper method to parse a single raw bookmark string"""
    try:
        # Split on first whitespace to separate URL from title
        parts = raw_string.split(None, 1)
        if len(parts) == 2:
            url, title = parts
        else:
            url = parts[0]
            title = ""
            
        return {"url": url, "title": title}
        
    except Exception:
        return None