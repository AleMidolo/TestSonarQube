def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.json")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory not found for version: {version_dir}")
        
        with open(inventory_path, 'r') as f:
            inventory = json.load(f)
        
        # Check for discrepancies in content digests
        root_inventory_path = os.path.join(version_dirs[0], "inventory.json")
        with open(root_inventory_path, 'r') as f:
            root_inventory = json.load(f)
        
        for content_id, digest in inventory.get("contents", {}).items():
            if content_id in root_inventory.get("contents", {}):
                if digest != root_inventory["contents"][content_id]:
                    print(f"Content digest mismatch for {content_id} in version {version_dir}")