def _verify(iface, candidate, tentative=False, vtype=None):
    """
    *iface* को सही ढंग से प्रदान करने के लिए *candidate* की पुष्टि करें।

    इसमें निम्नलिखित शामिल हैं:

    - यह सुनिश्चित करना कि उम्मीदवार यह दावा करता है कि वह इंटरफ़ेस प्रदान करता है, 
      ``iface.providedBy`` का उपयोग करके (जब तक *tentative* `True` नहीं है, 
      इस स्थिति में इस चरण को छोड़ दिया जाता है)। इसका मतलब है कि उम्मीदवार की कक्षा 
      यह घोषित करती है कि वह इंटरफ़ेस को `implements <zope.interface.implementer>` करती है, 
      या उम्मीदवार स्वयं यह घोषित करता है कि वह इंटरफ़ेस को 
      `provides <zope.interface.provider>` करता है।

    - यह सुनिश्चित करना कि उम्मीदवार सभी आवश्यक विधियों (methods) को परिभाषित करता है।

    - यह सुनिश्चित करना कि विधियों के पास सही हस्ताक्षर (signature) हैं 
      (जहां तक संभव हो)।

    - यह सुनिश्चित करना कि उम्मीदवार सभी आवश्यक गुणों (attributes) को परिभाषित करता है।

    :return bool: यदि सभी जांचें सफल होती हैं, तो एक सत्य मान (true value) लौटाता है।
    :raises zope.interface.Invalid: यदि उपरोक्त में से कोई भी शर्त पूरी नहीं होती है।

    .. versionchanged:: 5.0
        यदि कई विधियां या गुण अमान्य हैं, तो सभी त्रुटियों को एकत्रित और रिपोर्ट किया जाता है। 
        पहले, केवल पहली त्रुटि की रिपोर्ट की जाती थी। 
        एक विशेष मामले में, यदि केवल एक त्रुटि मौजूद है, तो इसे पहले की तरह अकेले उठाया जाता है।
    """
    from zope.interface import providedBy, Invalid
    from inspect import signature, Signature

    errors = []

    if not tentative and not providedBy(candidate).isinstance(iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = getattr(iface, '__required_methods__', [])
    for method in required_methods:
        if not hasattr(candidate, method):
            errors.append(f"{candidate} is missing required method {method}")
        else:
            method_signature = signature(getattr(candidate, method))
            iface_signature = signature(getattr(iface, method))
            if method_signature != iface_signature:
                errors.append(f"{method} in {candidate} has incorrect signature")

    required_attributes = getattr(iface, '__required_attributes__', [])
    for attr in required_attributes:
        if not hasattr(candidate, attr):
            errors.append(f"{candidate} is missing required attribute {attr}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid(errors)

    return True