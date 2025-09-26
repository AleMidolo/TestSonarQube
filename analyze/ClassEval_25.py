import json

class CookiesUtil:
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.cookies = {}

    def get_cookies(self, response):
        self.cookies = self._extract_cookies(response)
        self._save_cookies()

    def load_cookies(self):
        return self._load_cookies_from_file()

    def _save_cookies(self):
        return self._write_cookies_to_file(self.cookies)

    def set_cookies(self, request):
        request['cookies'] = self._format_cookies(self.cookies)

    def _extract_cookies(self, response):
        return response.get('cookies', {})

    def _load_cookies_from_file(self):
        try:
            with open(self.cookies_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _write_cookies_to_file(self, cookies):
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(cookies, file)
            return True
        except Exception:
            return False

    def _format_cookies(self, cookies):
        return '; '.join([f'{key}={value}' for key, value in cookies.items()])