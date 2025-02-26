def verifyObject(iface, candidate, tentative=False):
    """
    *iface* को सही ढंग से प्रदान करने के लिए *candidate* की पुष्टि करें।

    इसमें निम्नलिखित शामिल हैं:

    - यह सुनिश्चित करना कि candidate यह दावा करता है कि वह इंटरफ़ेस प्रदान करता है, 
      ``iface.providedBy`` का उपयोग करके (जब तक *tentative* `True` न हो, 
      इस स्थिति में इस चरण को छोड़ दिया जाता है)। इसका मतलब है कि candidate की क्लास 
      यह घोषित करती है कि वह इंटरफ़ेस को `implements <zope.interface.implementer>` करती है, 
      या candidate स्वयं यह घोषित करता है कि वह इंटरफ़ेस को 
      `provides <zope.interface.provider>` करता है।

    - यह सुनिश्चित करना कि candidate सभी आवश्यक methods को परिभाषित करता है।

    - यह सुनिश्चित करना कि methods का signature सही है (जहां तक संभव हो)।

    - यह सुनिश्चित करना कि candidate सभी आवश्यक attributes को परिभाषित करता है।

    :return bool: यदि सभी जांचें सफल होती हैं, तो एक सत्य मान लौटाता है।
    :raises zope.interface.Invalid: यदि उपरोक्त में से कोई भी शर्त पूरी नहीं होती है।

    .. versionchanged:: 5.0
        यदि कई methods या attributes अमान्य हैं, तो सभी त्रुटियों को एकत्रित और रिपोर्ट किया जाता है। 
        पहले, केवल पहली त्रुटि रिपोर्ट की जाती थी। एक विशेष मामले में, यदि केवल एक त्रुटि मौजूद है, 
        तो इसे पहले की तरह अकेले उठाया जाता है।
    """
    from zope.interface import providedBy, Invalid
    from inspect import signature, Signature

    errors = []

    if not tentative and not providedBy(candidate, iface):
        errors.append(f"{candidate} does not provide {iface}")

    required_methods = iface.requiredMethods()
    for method in required_methods:
        if not hasattr(candidate, method):
            errors.append(f"{candidate} is missing required method {method}")
        else:
            method_signature = signature(getattr(candidate, method))
            iface_signature = signature(getattr(iface, method))
            if method_signature != iface_signature:
                errors.append(f"Method {method} signature does not match")

    required_attributes = iface.requiredAttributes()
    for attr in required_attributes:
        if not hasattr(candidate, attr):
            errors.append(f"{candidate} is missing required attribute {attr}")

    if errors:
        if len(errors) == 1:
            raise Invalid(errors[0])
        else:
            raise Invalid(errors)

    return True