def integral(bins, edges):
    """
    histogram के लिए इंटीग्रल (स्केल) की गणना करें।

    *bins* में मान (values) होते हैं, और *edges* इंटीग्रेशन के लिए जाल (mesh) बनाते हैं।  
    इनका प्रारूप (format) :class:`.histogram` विवरण में परिभाषित है।
    """
    import numpy as np

    # Calculate the integral of the histogram
    integral_values = np.cumsum(bins) * np.diff(edges, prepend=edges[0])
    
    return integral_values