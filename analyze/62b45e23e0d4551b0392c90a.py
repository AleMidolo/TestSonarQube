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
                
                # Validate the inventory for the current version
                if not self.validate_inventory(inventory):
                    raise ValueError(f"Invalid inventory in {version}")

                # Record the digests
                current_digests = set(item['digest'] for item in inventory.get('items', []))
                root_digests = set(inventory_digests.get('root', []))

                # Check for discrepancies
                discrepancies.extend(current_digests - root_digests)

                # Update the inventory digests
                inventory_digests[version] = current_digests

        except FileNotFoundError:
            raise FileNotFoundError(f"Inventory file not found for version: {version}")
        except json.JSONDecodeError:
            raise ValueError(f"Error decoding JSON for inventory in version: {version}")

    return discrepancies