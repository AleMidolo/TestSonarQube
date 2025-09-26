class URLHandler:
    def __init__(self, url):
        self.url = url

    def get_scheme(self):
        scheme_end = self._find_scheme_end()
        if scheme_end != -1:
            return self.url[:scheme_end]
        return None

    def get_host(self):
        scheme_end = self._find_scheme_end()
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = self._find_host_end(url_without_scheme)
            if host_end != -1:
                return url_without_scheme[:host_end]
            return url_without_scheme
        return None

    def get_path(self):
        scheme_end = self._find_scheme_end()
        if scheme_end != -1:
            url_without_scheme = self.url[scheme_end + 3:]
            host_end = self._find_host_end(url_without_scheme)
            if host_end != -1:
                return url_without_scheme[host_end:]
        return None

    def get_query_params(self):
        query_start = self.url.find("?")
        fragment_start = self.url.find("#")
        if query_start != -1:
            query_string = self.url[query_start + 1:fragment_start if fragment_start != -1 else None]
            return self._parse_query_string(query_string)
        return None

    def get_fragment(self):
        fragment_start = self.url.find("#")
        if fragment_start != -1:
            return self.url[fragment_start + 1:]
        return None

    def _find_scheme_end(self):
        return self.url.find("://")

    def _find_host_end(self, url_without_scheme):
        return url_without_scheme.find("/")

    def _parse_query_string(self, query_string):
        params = {}
        if len(query_string) > 0:
            param_pairs = query_string.split("&")
            for pair in param_pairs:
                key_value = pair.split("=")
                if len(key_value) == 2:
                    key, value = key_value
                    params[key] = value
        return params