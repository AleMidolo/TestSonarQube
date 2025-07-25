def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    # Dictionary to store digests that differ from root inventory
    different_digests = set()
    
    # Get root inventory digest
    root_inventory = self.get_root_inventory()
    if not root_inventory:
        raise ValueError("Root inventory not found")
        
    root_digests = set(root_inventory.get_all_digests())
    
    # Validate each version has inventory and track different digests
    for version in version_dirs:
        inventory_path = os.path.join(version, "inventory.json")
        if not os.path.exists(inventory_path):
            raise ValueError(f"Missing inventory for version {version}")
            
        with open(inventory_path) as f:
            version_inventory = json.load(f)
            
        # Get digests for this version
        version_digests = set(version_inventory.get_all_digests())
        
        # Add any digests not in root inventory to tracking set
        different_digests.update(version_digests - root_digests)
        
    return different_digests