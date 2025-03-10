def scale(self, other=None):
    """
    ग्राफ़ का स्केल प्राप्त करें या सेट करें।

    यदि *other* ``None`` है, तो इस ग्राफ़ का स्केल लौटाएं।

    यदि *other* एक संख्यात्मक मान है, तो ग्राफ़ को उस मान पर पुनः स्केल करें।
    यदि ग्राफ़ का स्केल अज्ञात है या शून्य है,
    तो पुनः स्केल करने पर :exc:`~.LenaValueError` उत्पन्न होगा।

    सार्थक परिणाम प्राप्त करने के लिए, ग्राफ़ के फ़ील्ड्स का उपयोग किया जाता है।
    केवल अंतिम निर्देशांक (coordinate) को पुनः स्केल किया जाता है।
    उदाहरण के लिए, यदि ग्राफ़ में *x* और *y* निर्देशांक हैं,
    तो *y* को पुनः स्केल किया जाएगा, और यदि ग्राफ़ 3-आयामी (3-dimensional) है,
    तो *z* को पुनः स्केल किया जाएगा।
    सभी त्रुटियों (errors) को उनके निर्देशांक के साथ पुनः स्केल किया जाता है।
    """
    if other is None:
        return self._scale
    elif isinstance(other, (int, float)):
        if self._scale is None or self._scale == 0:
            raise LenaValueError("ग्राफ़ का स्केल अज्ञात या शून्य है।")
        scale_factor = other / self._scale
        if hasattr(self, 'y'):
            self.y *= scale_factor
        if hasattr(self, 'z'):
            self.z *= scale_factor
        if hasattr(self, 'errors'):
            for error in self.errors:
                error *= scale_factor
        self._scale = other
    else:
        raise TypeError("अमान्य प्रकार। संख्यात्मक मान आवश्यक है।")