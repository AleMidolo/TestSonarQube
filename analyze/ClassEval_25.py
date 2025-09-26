import json

class CookiesUtil:
    def __init__(self, cookies_file):
        self.cookies_file = cookies_file
        self.cookies = None

    def get_cookies(self, response):
        self.cookies = response['cookies']
        self._save_cookies()

    def load_cookies(self):
        return self._load_cookies_from_file()

    def _load_cookies_from_file(self):
        try:
            with open(self.cookies_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_cookies(self):
        try:
            with open(self.cookies_file, 'w') as file:
                json.dump(self.cookies, file)
            return True
        except Exception:
            return False

    def set_cookies(self, request):
        request['cookies'] = self._format_cookies()

    def _format_cookies(self):
        return '; '.join([f'{key}={value}' for key, value in self.cookies.items()])