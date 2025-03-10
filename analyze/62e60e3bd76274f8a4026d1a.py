def from_raw_values(cls, values):
    """
    कच्चे बुकमार्क स्ट्रिंग मानों की सूची से एक Bookmarks ऑब्जेक्ट बनाएं।

    इस विधि का उपयोग करने की आवश्यकता नहीं होनी चाहिए जब तक कि आप 
    बुकमार्क्स को डीसिरियलाइज़ (deserialize) करना न चाहें।

    :param values: ASCII स्ट्रिंग मान (कच्चे बुकमार्क्स)
    :type values: Iterable[str]
    """
    # Assuming the Bookmarks class is defined elsewhere
    bookmarks = cls()
    for value in values:
        # Process each raw value and add it to the Bookmarks object
        # This is a placeholder for the actual deserialization logic
        bookmark = process_raw_value(value)  # Replace with actual processing logic
        bookmarks.add(bookmark)
    return bookmarks

# Placeholder function for processing raw values
def process_raw_value(value):
    # Implement the logic to convert raw value to a bookmark object
    return value  # Replace with actual processing logic