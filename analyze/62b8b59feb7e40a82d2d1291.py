def _getTargetClass(self):
    """
    इसका उपयोग उस कार्यान्वयन (implementation) को लौटाने के लिए करें,
    जिसका उपयोग किया जा रहा है, बिना 'Py' या 'Fallback' प्रत्यय (suffix) के।
    """
    class_name = self.__class__.__name__
    if class_name.endswith('Py') or class_name.endswith('Fallback'):
        return class_name[:-2] if class_name.endswith('Py') else class_name[:-8]
    return class_name