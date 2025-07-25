def get_versions():
    """
    संस्करण जानकारी प्राप्त करें या यदि ऐसा करने में असमर्थ हैं तो डिफ़ॉल्ट मान लौटाएं।
    """
    try:
        import pkg_resources
        import platform
        import sys
        
        versions = {
            'python': sys.version.split()[0],
            'platform': platform.platform(),
            'packages': {
                dist.key: dist.version
                for dist in pkg_resources.working_set
            }
        }
        return versions
        
    except Exception:
        # Return default values if unable to get version info
        return {
            'python': 'unknown',
            'platform': 'unknown',
            'packages': {}
        }