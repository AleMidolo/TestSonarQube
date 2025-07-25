def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    # Track all unique content digests seen
    all_digests = set()
    
    # Get root inventory digests
    root_inventory = self.get_root_inventory()
    root_digests = set(root_inventory.get_all_digests())
    
    # Validate each version has inventory
    for version in version_dirs:
        inventory_path = os.path.join(version, 'inventory.json')
        if not os.path.exists(inventory_path):
            raise ValidationError(f"Missing inventory file for version {version}")
            
        # Load inventory and get digests
        with open(inventory_path) as f:
            inventory = json.load(f)
            version_digests = set(inventory.get_all_digests())
            
        # Add any new digests not in root inventory
        diff_digests = version_digests - root_digests
        all_digests.update(diff_digests)
        
    return all_digests