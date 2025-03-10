def data(self, *keys):
    """
    यह मेथड इस रिकॉर्ड की कुंजियों और मानों (keys and values) को एक डिक्शनरी (dictionary) के रूप में लौटाता है। आप वैकल्पिक रूप से केवल कुछ विशेष मानों को इंडेक्स (index) या कुंजी (key) के आधार पर शामिल कर सकते हैं। जो कुंजियाँ प्रदान की गई हैं लेकिन रिकॉर्ड में मौजूद नहीं हैं, उन्हें :const:`None` मान के साथ सम्मिलित किया जाएगा। यदि कोई इंडेक्स सीमा से बाहर है, तो :exc:`IndexError` उत्पन्न होगा।

    पैरामीटर (Parameters): 
    - keys: उन आइटम्स के इंडेक्स या कुंजियाँ जिन्हें शामिल करना है; यदि कोई कुंजी प्रदान नहीं की गई है, तो सभी मान शामिल किए जाएंगे।  

    वापसी मान (Return): 
    -मानों का शब्दकोश, फ़ील्ड नाम द्वारा कुंजीबद्ध

    अपवाद (Raises): 
    - :exc:`IndexError` यदि कोई सीमा से बाहर का इंडेक्स निर्दिष्ट किया गया है।
    """
    if not keys:
        return self.__dict__
    
    result = {}
    for key in keys:
        if isinstance(key, int):
            if key < 0 or key >= len(self.__dict__):
                raise IndexError("Index out of range")
            key = list(self.__dict__.keys())[key]
        if key in self.__dict__:
            result[key] = self.__dict__[key]
        else:
            result[key] = None
    return result