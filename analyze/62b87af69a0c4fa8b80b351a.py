def is_fill_compute_el(obj):
    """
    यह फ़ंक्शन यह जांचता है कि दिए गए ऑब्जेक्ट में 'fill' और 'compute' नामक मेथड्स मौजूद हैं और वे निष्पादन योग्य (callable) हैं या नहीं।
    """
    return callable(getattr(obj, 'fill', None)) and callable(getattr(obj, 'compute', None))