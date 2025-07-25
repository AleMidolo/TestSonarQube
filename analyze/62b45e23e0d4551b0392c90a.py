def validate_version_inventories(self, version_dirs):
    """
    प्रत्येक संस्करण के पास उस बिंदु तक एक इन्वेंटरी होनी चाहिए।

    साथ ही, किसी भी सामग्री डाइजेस्ट का रिकॉर्ड रखें जो रूट इन्वेंटरी में मौजूद डाइजेस्ट से अलग हो,
    ताकि सामग्री को सत्यापित करते समय हम उन्हें भी जांच सकें।

    version_dirs एक संस्करण डायरेक्टरी नामों की सूची है और इसे संस्करण अनुक्रम (1, 2, 3...) में माना जाता है।
    """
    inventory_digests = {}
    discrepancies = []

    for version in version_dirs:
        inventory_path = f"{version}/inventory.json"
        
        try:
            with open(inventory_path, 'r') as file:
                inventory = json.load(file)
                current_digest = inventory.get('digest')
                
                # Check if the current digest is in the root inventory
                if current_digest not in inventory_digests.values():
                    discrepancies.append((version, current_digest))
                
                # Record the digest for the current version
                inventory_digests[version] = current_digest

        except FileNotFoundError:
            raise Exception(f"Inventory file not found for version: {version}")
        except json.JSONDecodeError:
            raise Exception(f"Error decoding JSON for version: {version}")

    return discrepancies