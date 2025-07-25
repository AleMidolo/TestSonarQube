from zope.interface import providedBy, Invalid
from zope.interface.verify import verifyObject as zope_verifyObject

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
    if not tentative and not providedBy(candidate).isOrExtends(iface):
        raise Invalid(f"The candidate does not provide the interface {iface}.")

    try:
        zope_verifyObject(iface, candidate)
    except Invalid as e:
        raise Invalid(f"Verification failed: {e}")

    return True