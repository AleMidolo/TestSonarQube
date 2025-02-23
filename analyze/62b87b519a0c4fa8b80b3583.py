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
        return self.scale_value  # Assuming scale_value is an attribute of the class

    if not isinstance(other, (int, float)):
        raise ValueError("The scale value must be a numeric type.")

    if self.scale_value is None or self.scale_value == 0:
        raise LenaValueError("Cannot rescale when the scale is unknown or zero.")

    # Assuming self.coordinates is a list of coordinates
    for i in range(len(self.coordinates)):
        if i == len(self.coordinates) - 1:  # Only scale the last coordinate
            self.coordinates[i] *= other

    self.scale_value = other  # Update the scale value