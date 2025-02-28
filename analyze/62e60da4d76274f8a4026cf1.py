def values(self, *keys):
    """
    रिकॉर्ड के मान (values) लौटाता है, और वैकल्पिक रूप से केवल कुछ विशिष्ट मानों को शामिल करने के लिए इंडेक्स या कुंजी द्वारा फ़िल्टर करता है।

    पैरामीटर (Parameters): 
    - keys: उन आइटम्स के इंडेक्स या कुंजियाँ (keys) जिन्हें शामिल करना है; यदि कोई कुंजी प्रदान नहीं की जाती है, तो सभी मान (values) शामिल किए जाएंगे।  

    वापसी (Return):
    - मानों (values) की सूची।  

    वापसी प्रकार (Return Type):
    - सूची (list)
    """
    if not keys:
        return list(self.__dict__.values())
    else:
        return [self.__dict__[key] for key in keys if key in self.__dict__]