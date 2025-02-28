def status_str(self, prefix=''):
    """
    सत्यापन लॉग (validation log) का स्ट्रिंग प्रतिनिधित्व लौटाएं, वैकल्पिक प्रीफिक्स के साथ।
    """
    log_str = ""
    for log_entry in self.validation_log:
        log_str += f"{prefix}{log_entry}\n"
    return log_str.strip()