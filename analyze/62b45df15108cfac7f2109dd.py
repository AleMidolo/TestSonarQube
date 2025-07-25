def status_str(self, prefix=''):
    """
    सत्यापन लॉग (validation log) का स्ट्रिंग प्रतिनिधित्व लौटाएं, वैकल्पिक प्रीफिक्स के साथ।
    """
    result = []
    for entry in self.log:
        if isinstance(entry, str):
            result.append(prefix + entry)
        else:
            result.append(prefix + str(entry))
    return '\n'.join(result)