def __init__(self, url):
    self.url = url
    self.parsed_url = urllib.parse.urlparse(url)