def _c_optimizations_available():
    """
    C ऑप्टिमाइज़ेशन मॉड्यूल लौटाएं, यदि उपलब्ध हो, अन्यथा एक झूठा मान।  

    यदि ऑप्टिमाइज़ेशन आवश्यक हैं लेकिन उपलब्ध नहीं हैं, तो यह `ImportError` उत्पन्न करता है।  

    यह यह नहीं बताता कि इन्हें उपयोग करना चाहिए या नहीं।  
    """
    try:
        import _c_optimizations
        return _c_optimizations
    except ImportError:
        return False