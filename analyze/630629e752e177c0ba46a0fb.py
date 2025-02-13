import requests

def send_document(url, data, timeout=10, method="post", *args, **kwargs):
    try:
        if method.lower() == "post":
            response = requests.post(url, data=data, timeout=timeout, *args, **kwargs)
        else:
            raise ValueError("Unsupported method: {}".format(method))
        return response.status_code, None
    except Exception as e:
        return None, e