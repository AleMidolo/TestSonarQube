def identify_request(request: RequestType):
    import json
    import xml.etree.ElementTree as ET

    # Check for JSON events
    try:
        body = request.get_json()
        if 'events' in body:
            return True
    except Exception:
        pass

    # Check for XML Magic_ENV_TAG
    try:
        body = request.get_data(as_text=True)
        root = ET.fromstring(body)
        if root.tag == 'Magic_ENV_TAG':
            return True
    except Exception:
        pass

    return False