def add_argument(self, arg, required=False, arg_type=str):
    """
        self.types और self.required में एक तर्क जोड़ता है।
        यह जांचता है कि क्या यह एक आवश्यक तर्क है और तर्क प्रकार को संग्रहीत करता है।
        यदि तर्क को आवश्यक के रूप में सेट किया गया है, तो इसे आवश्यक सेट में जोड़ा जाएगा।
        तर्क प्रकार और नाम को types शब्दकोश में कुंजी-मूल्य जोड़ों के रूप में संग्रहीत किया जाता है।
        :param arg: str, तर्क का नाम
        :param required: bool, क्या तर्क आवश्यक है, डिफ़ॉल्ट False है
        :param arg_type:str, तर्क प्रकार, डिफ़ॉल्ट str है
        >>> parser.add_argument('arg1', True, 'int')
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'int'}
        """
    self.types[arg] = arg_type
    if required:
        self.required.add(arg)