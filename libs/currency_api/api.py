from libs.currency_api import settings
from requests import request


class CurrencyRESTAPI(object):
    SUPPORTED_METHODS = ("GET", )

    def __init__(self):
        self._base_url = settings.BASE_URL
        self._access_key = settings.ACCESS_KEY

    def __get_request_url(self, **kwargs):
        url = self._base_url + "?access_key=" + self._access_key + "&"
        params = ["%s=%s" % (key, value) for key, value in kwargs.items()]
        url += "&".join(params)

        return url

    def __request(self, method, **kwargs):
        if method not in self.SUPPORTED_METHODS:
            raise ValueError("Unsupported method %s. Please use one of: %s" %
                             (method, ', '.join(self.SUPPORTED_METHODS)))
        url = self.__get_request_url(**kwargs)
        try:
            response = request(method=method, url=url)
        except Exception as error:
            raise error
        else:
            return response

    @staticmethod
    def __handle_response(response):
        if response.ok:
            resp = response.json()
            if resp["success"]:
                return resp["quotes"]
            else:
                return resp["error"]
        else:
            return response.text

    def get_rates(self, currencies):
        if currencies:
            try:
                data = self.__request(
                    "GET", currencies=",".join(currencies), format=1)
            except Exception as error:
                raise error
            else:
                data = self.__handle_response(data)
                return data
        else:
            raise ValueError("currencies not provided")
