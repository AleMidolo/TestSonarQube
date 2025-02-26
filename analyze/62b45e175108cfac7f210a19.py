def validate_fixity(self, fixity, manifest_files):
    """
    इन्वेंटरी में फिक्सिटी ब्लॉक को सत्यापित करें।
    फिक्सिटी ब्लॉक की संरचना की जांच करें और सुनिश्चित करें कि केवल वे फाइलें
    जो मैनिफेस्ट में सूचीबद्ध हैं, वही संदर्भित की गई हैं।
    """
    # Check if fixity is a dictionary
    if not isinstance(fixity, dict):
        raise ValueError("Fixity must be a dictionary.")

    # Check if all files in fixity are in manifest_files
    for file in fixity.keys():
        if file not in manifest_files:
            raise ValueError(f"File '{file}' in fixity is not listed in manifest files.")

    # Check the structure of the fixity block
    for file, checksum in fixity.items():
        if not isinstance(checksum, str):
            raise ValueError(f"Checksum for file '{file}' must be a string.")
        if len(checksum) == 0:
            raise ValueError(f"Checksum for file '{file}' cannot be empty.")

    return True