import os
import hashlib

def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    root_inventory = {}
    for version_dir in version_dirs:
        inventory_path = os.path.join(version_dir, "inventory.txt")
        if not os.path.exists(inventory_path):
            raise FileNotFoundError(f"Inventory file not found in {version_dir}")
        
        with open(inventory_path, 'r') as file:
            for line in file:
                file_path, file_digest = line.strip().split()
                if file_path in root_inventory:
                    if root_inventory[file_path] != file_digest:
                        print(f"Warning: Digest mismatch for {file_path} in {version_dir}")
                else:
                    root_inventory[file_path] = file_digest