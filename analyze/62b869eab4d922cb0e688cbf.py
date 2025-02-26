def generate_default_observer_schema(app):
    """
    प्रत्येक Kubernetes संसाधन के लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करें जो ``spec.manifest`` में मौजूद है और जिसके लिए कोई कस्टम ऑब्ज़र्वर स्कीमा निर्दिष्ट नहीं किया गया है।

    आर्ग्युमेंट्स:
        app (krake.data.kubernetes.Application): वह एप्लिकेशन जिसके लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करना है।
    """
    default_schema = {}
    for resource in app.spec.manifest:
        if 'custom_observer_schema' not in resource:
            default_schema[resource['kind']] = {
                'apiVersion': resource['apiVersion'],
                'metadata': {
                    'name': resource['metadata']['name'],
                    'namespace': resource['metadata'].get('namespace', 'default')
                },
                'spec': resource.get('spec', {})
            }
    return default_schema