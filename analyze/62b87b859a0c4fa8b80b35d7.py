def to_csv(self, separator=",", header=None):
    """
    .. deprecated:: 0.5 Lena 0.5 में to_csv का उपयोग नहीं किया जाता है।
          Iterables को तालिकाओं (tables) में परिवर्तित किया जाता है।

    ग्राफ़ के बिंदुओं (points) को CSV में परिवर्तित करें।

    *separator* मानों को अलग करता है, डिफ़ॉल्ट रूप से यह कॉमा (comma) है।

    *header*, यदि ``None`` नहीं है, तो यह आउटपुट की पहली स्ट्रिंग होगी
    (नई पंक्ति स्वचालित रूप से जोड़ी जाती है)।

    चूंकि एक ग्राफ़ बहुआयामी (multidimensional) हो सकता है,
    प्रत्येक बिंदु के लिए पहले उसके निर्देशांक (coordinate) को स्ट्रिंग में परिवर्तित किया जाता है
    (*separator* द्वारा अलग किया गया), और फिर उसके मान (value) के प्रत्येक भाग को।

    :class:`Graph` को CSV में परिवर्तित करने के लिए, Lena अनुक्रम (sequence) के अंदर
    :class:`lena.output.ToCSV` का उपयोग करें।
    """
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header)
    
    for point in self.points:
        # Convert coordinates to string separated by the separator
        coords_str = separator.join(map(str, point.coordinates))
        # Convert values to string separated by the separator
        values_str = separator.join(map(str, point.values))
        # Combine coordinates and values into a single CSV line
        csv_line = f"{coords_str}{separator}{values_str}"
        csv_lines.append(csv_line)
    
    # Join all lines with newline characters to form the final CSV string
    return "\n".join(csv_lines)