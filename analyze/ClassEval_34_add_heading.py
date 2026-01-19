def add_heading(self, heading, level=1):
    """
    वर्ड दस्तावेज़ में एक शीर्षक जोड़ता है।
    :param heading: str, शीर्षक का पाठ।
    :param level: int, वैकल्पिक, शीर्षक का स्तर (1, 2, 3, आदि; डिफ़ॉल्ट 1 है)।
    :return: bool, यदि शीर्षक सफलतापूर्वक जोड़ा गया है तो True, अन्यथा False।
    """
    try:
        if not isinstance(heading, str):
            return False
        
        if not isinstance(level, int) or level < 1:
            return False
        
        # Assuming this is a method of a class that has a document object
        # Using python-docx library pattern
        if hasattr(self, 'document'):
            self.document.add_heading(heading, level=level)
            return True
        
        return False
    except Exception:
        return False