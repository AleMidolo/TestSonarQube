def integral(bins, edges):
    """
    हिस्टोग्राम के लिए इंटीग्रल (स्केल) की गणना करें।

    *bins* में मान (values) होते हैं, और *edges* इंटीग्रेशन के लिए जाल (mesh) बनाते हैं।  
    इनका प्रारूप (format) :class:`.histogram` विवरण में परिभाषित है।
    """
    total = 0.0
    for i in range(len(bins)):
        bin_width = edges[i+1] - edges[i]
        total += bins[i] * bin_width
    return total