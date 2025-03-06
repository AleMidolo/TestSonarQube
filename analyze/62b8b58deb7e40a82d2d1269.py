def directlyProvidedBy(object): # pylint:disable=redefined-builtin
    """
    दिए गए ऑब्जेक्ट द्वारा सीधे प्रदान किए गए इंटरफेस को लौटाएं

    लौटाई गई वैल्यू `~zope.interface.interfaces.IDeclaration` है।
    provides = getattr(object, "__provides__", None)
    if (
            provides is None # कोई स्पेसिफिकेशन नहीं
            # हो सकता है कि हमें implements स्पेसिफिकेशन मिला हो, 
            # एक ऑप्टिमाइज़ेशन के रूप में। यदि ऐसा है, तो यह ऐसा है 
            # जैसे केवल एक बेस हो, जिसे हम क्लास-प्रदत्त घोषणाओं को 
            # बाहर करने के लिए हटा देते हैं:

    दिए गए ऑब्जेक्ट द्वारा सीधे प्रदान किए गए इंटरफ़ेस लौटाता है

    लौटाया गया मान `~zope.interfaces.interfaces.ideclaration` है।
    """
    provides = getattr(object, "__provides__", None)
    if provides is None:
        return None
    return provides