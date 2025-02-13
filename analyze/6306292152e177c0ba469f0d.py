def identify_request(request: RequestType) -> bool:
    try:
        body = request.json()
        return 'events' in body
    except (ValueError, AttributeError):
        return False