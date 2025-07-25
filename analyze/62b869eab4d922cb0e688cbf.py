def generate_default_observer_schema(app):
    """
    प्रत्येक Kubernetes संसाधन के लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करें जो ``spec.manifest`` में मौजूद है और जिसके लिए कोई कस्टम ऑब्ज़र्वर स्कीमा निर्दिष्ट नहीं किया गया है।

    आर्ग्युमेंट्स:
        app (krake.data.kubernetes.Application): वह एप्लिकेशन जिसके लिए डिफ़ॉल्ट ऑब्ज़र्वर स्कीमा उत्पन्न करना है।
    """
    default_schema = {}
    
    if hasattr(app, 'spec') and hasattr(app.spec, 'manifest'):
        manifest = app.spec.manifest
        if isinstance(manifest, dict):
            for resource in manifest.get('resources', []):
                if isinstance(resource, dict) and 'kind' in resource:
                    kind = resource['kind']
                    if kind not in default_schema:
                        default_schema[kind] = {
                            'type': 'object',
                            'properties': {
                                'status': {
                                    'type': 'object',
                                    'properties': {
                                        'conditions': {
                                            'type': 'array',
                                            'items': {
                                                'type': 'object',
                                                'properties': {
                                                    'type': {'type': 'string'},
                                                    'status': {'type': 'string'},
                                                    'lastTransitionTime': {'type': 'string'},
                                                    'reason': {'type': 'string'},
                                                    'message': {'type': 'string'}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
    
    return default_schema