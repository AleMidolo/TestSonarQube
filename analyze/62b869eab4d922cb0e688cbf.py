def generate_default_observer_schema(app):
    """
    प्रत्येक Kubernetes संसाधन के लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करें जो ``spec.manifest`` में मौजूद है और जिसके लिए कोई कस्टम ऑब्ज़र्वर स्कीमा निर्दिष्ट नहीं किया गया है।

    आर्ग्युमेंट्स:
        app (krake.data.kubernetes.Application): वह एप्लिकेशन जिसके लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करना है।
    """
    default_schema = {
        "apiVersion": "krake.eclabs.io/v1alpha1",
        "kind": "ObserverSchema",
        "metadata": {
            "name": f"{app.metadata.name}-default-observer-schema",
            "namespace": app.metadata.namespace
        },
        "spec": {
            "resources": []
        }
    }

    if hasattr(app, 'spec') and hasattr(app.spec, 'manifest'):
        for resource in app.spec.manifest:
            resource_schema = {
                "group": resource.get("group", ""),
                "version": resource.get("version", ""),
                "kind": resource.get("kind", ""),
                "observer": {
                    "type": "Kubernetes",
                    "config": {
                        "apiVersion": resource.get("apiVersion", ""),
                        "kind": resource.get("kind", "")
                    }
                }
            }
            default_schema["spec"]["resources"].append(resource_schema)

    return default_schema