def validate_fixity(self, fixity, manifest_files):
    """
    इन्वेंटरी में फिक्सिटी ब्लॉक को सत्यापित करें।
    फिक्सिटी ब्लॉक की संरचना की जांच करें और सुनिश्चित करें कि केवल वे फाइलें
    जो मैनिफेस्ट में सूचीबद्ध हैं, वही संदर्भित की गई हैं।
    """
    if not isinstance(fixity, dict):
        raise ValueError("फिक्सिटी ब्लॉक एक डिक्शनरी होना चाहिए।")
    
    if not isinstance(manifest_files, list):
        raise ValueError("मैनिफेस्ट फाइलें एक सूची होनी चाहिए।")
    
    for file_name, checksum in fixity.items():
        if file_name not in manifest_files:
            raise ValueError(f"फाइल '{file_name}' मैनिफेस्ट में सूचीबद्ध नहीं है।")
    
    return True