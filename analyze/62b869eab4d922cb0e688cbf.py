def generate_default_observer_schema(app):
    """
    प्रत्येक Kubernetes संसाधन के लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करें जो ``spec.manifest`` में मौजूद है और जिसके लिए कोई कस्टम ऑब्ज़र्वर स्कीमा निर्दिष्ट नहीं किया गया है।

    आर्ग्युमेंट्स:
        app (krake.data.kubernetes.Application): वह एप्लिकेशन जिसके लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करना है।
    """
    default_schema = {
        "type": "object",
        "properties": {
            "status": {
                "type": "object",
                "properties": {
                    "conditions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {"type": "string"},
                                "status": {"type": "string"},
                                "lastTransitionTime": {"type": "string", "format": "date-time"},
                                "reason": {"type": "string"},
                                "message": {"type": "string"}
                            },
                            "required": ["type", "status"]
                        }
                    }
                },
                "required": ["conditions"]
            }
        },
        "required": ["status"]
    }

    # Check if the app has a manifest and if it contains any resources
    if hasattr(app.spec, 'manifest') and app.spec.manifest:
        for resource in app.spec.manifest:
            if not hasattr(resource, 'observer_schema'):
                resource.observer_schema = default_schema

    return app