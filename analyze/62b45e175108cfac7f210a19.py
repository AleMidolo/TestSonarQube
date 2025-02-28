def validate_fixity(self, fixity, manifest_files):
    """
    इन्वेंटरी में फिक्सिटी ब्लॉक को सत्यापित करें।
    फिक्सिटी ब्लॉक की संरचना की जांच करें और सुनिश्चित करें कि केवल वे फाइलें
    जो मैनिफेस्ट में सूचीबद्ध हैं, वही संदर्भित की गई हैं।
    """
    if not isinstance(fixity, dict):
        raise ValueError("फिक्सिटी ब्लॉक एक डिक्शनरी होना चाहिए।")
    
    if not isinstance(manifest_files, list):
        raise ValueError("मैनिफेस्ट फाइल्स एक लिस्ट होनी चाहिए।")
    
    # फिक्सिटी ब्लॉक में सभी फाइलें मैनिफेस्ट में होनी चाहिए
    for file_name in fixity.keys():
        if file_name not in manifest_files:
            raise ValueError(f"फाइल '{file_name}' मैनिफेस्ट में सूचीबद्ध नहीं है।")
    
    # मैनिफेस्ट में सभी फाइलें फिक्सिटी ब्लॉक में होनी चाहिए
    for file_name in manifest_files:
        if file_name not in fixity:
            raise ValueError(f"फाइल '{file_name}' फिक्सिटी ब्लॉक में सूचीबद्ध नहीं है।")
    
    return True