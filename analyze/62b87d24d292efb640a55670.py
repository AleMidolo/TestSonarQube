def get_versions():
    """
    संस्करण जानकारी प्राप्त करें या यदि ऐसा करने में असमर्थ हैं तो डिफ़ॉल्ट मान लौटाएं।
    """
    try:
        import pkg_resources
        versions = {}
        for package in ['numpy', 'pandas', 'scipy']:
            try:
                versions[package] = pkg_resources.get_distribution(package).version
            except pkg_resources.DistributionNotFound:
                versions[package] = 'Not Installed'
        return versions
    except ImportError:
        return {'numpy': '1.0.0', 'pandas': '1.0.0', 'scipy': '1.0.0'}