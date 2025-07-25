def scale(self, other=None, recompute=False):
    """
    हिस्टोग्राम का स्केल (इंटीग्रल) गणना करें या सेट करें।

    यदि *other* ``None`` है, तो इस हिस्टोग्राम का स्केल लौटाएं।  
    यदि इसका स्केल पहले गणना नहीं किया गया है,  
    तो इसे गणना करके संग्रहीत किया जाएगा ताकि बाद में उपयोग किया जा सके  
    (जब तक कि *recompute* को स्पष्ट रूप से न कहा जाए)।  
    ध्यान दें कि यदि हिस्टोग्राम को बदला (फिल किया) गया है,  
    तो यदि स्केल पहले से गणना किया गया था,  
    तो इसे स्पष्ट रूप से फिर से गणना करना आवश्यक है।  

    यदि एक फ्लोट *other* प्रदान किया गया है,  
    तो self को *other* के अनुसार पुनः स्केल करें।  

    ऐसे हिस्टोग्राम जिनका स्केल शून्य है,  
    उन्हें पुनः स्केल नहीं किया जा सकता।  
    यदि ऐसा करने का प्रयास किया जाता है,  
    तो :exc:`.LenaValueError` त्रुटि उत्पन्न की जाएगी।
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            self._scale = self._compute_scale()
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("other must be a float or int")
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale")
        self._scale = other
        self._rescale_histogram(other)

def _compute_scale(self):
    """
    हिस्टोग्राम का स्केल गणना करें।
    """
    # यहां स्केल गणना करने का तरीका लागू करें
    # उदाहरण के लिए, यह सभी बिन मानों का योग हो सकता है
    return sum(self.bins)

def _rescale_histogram(self, scale_factor):
    """
    हिस्टोग्राम को दिए गए स्केल फैक्टर के अनुसार पुनः स्केल करें।
    """
    # यहां हिस्टोग्राम को पुनः स्केल करने का तरीका लागू करें
    # उदाहरण के लिए, प्रत्येक बिन मान को scale_factor से गुणा करें
    self.bins = [bin_value * scale_factor for bin_value in self.bins]