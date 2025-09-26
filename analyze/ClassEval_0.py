import logging
import datetime


class AccessGatewayFilter:

    START_WITH_PATHS = ["/api", '/login']
    JWT_EXPIRATION_DAYS = 3

    def __init__(self):
        pass

    def filter(self, request):
        request_uri = request['path']
        method = request['method']

        if self.is_start_with(request_uri):
            return True

        try:
            token = self.get_jwt_user(request)
            if token and self.is_user_level_valid(token):
                self.set_current_user_info_and_log(token['user'])
                return True
        except Exception as e:
            logging.error(f"Error in filter: {e}")
            return False

    def is_start_with(self, request_uri):
        return any(request_uri.startswith(s) for s in self.START_WITH_PATHS)

    def get_jwt_user(self, request):
        token = request['headers']['Authorization']
        user = token['user']
        if token['jwt'].startswith(user['name']):
            jwt_str_date = token['jwt'].split(user['name'])[1]
            jwt_date = datetime.datetime.strptime(jwt_str_date, "%Y-%m-%d")
            if self.is_jwt_expired(jwt_date):
                return None
        return token

    def is_jwt_expired(self, jwt_date):
        return datetime.datetime.today() - jwt_date >= datetime.timedelta(days=self.JWT_EXPIRATION_DAYS)

    def is_user_level_valid(self, token):
        return token['user']['level'] > 2

    def set_current_user_info_and_log(self, user):
        host = user['address']
        logging.log(msg=f"{user['name']} {host} {datetime.datetime.now()}", level=1)