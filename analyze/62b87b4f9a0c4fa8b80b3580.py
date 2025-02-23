def integral(bins, edges):
    """
    histogram के लिए इंटीग्रल (स्केल) की गणना करें।

    *bins* में मान (values) होते हैं, और *edges* इंटीग्रेशन के लिए जाल (mesh) बनाते हैं।  
    इनका प्रारूप (format) :class:`.histogram` विवरण में परिभाषित है।
    """
    import numpy as np

    # Calculate the width of each bin
    bin_widths = np.diff(edges)

    # Calculate the integral by summing the product of bins and bin widths
    integral_values = np.cumsum(bins * bin_widths)

    return integral_values