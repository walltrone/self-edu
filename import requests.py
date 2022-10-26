from typing import List
from urllib.parse import urlparse, urlencode

import requests
from pydantic import BaseModel

TOKEN = ''
APP_ID = 51438494


class DisplayTypes(BaseModel):
    page = 'page'
    popup = 'popup'


class ScopeTypes(BaseModel):
    FRIENDS = 'friends'
    WALL = 'wall'


class VKClient:
    URL_AUTH = 'https://oauth.vk.com/authorize'
    URL_REDIRECT = 'https://oauth.vk.com/blank.html'
    SCOPE_LIST = [FRIENDS, WALL]
    SCOPE = ','.join(SCOPE_LIST)
    PROTOCOL_V: str = '5.194'

    def __init__(self, token: str, user_id: str):
        self.token = token
        self.user_id = user_id

    def get_token(self):
        param = {
            'client_id': APP_ID,
            'redirect_url': self.URL_REDIRECT,
            'display': DisplayTypes.page,
            'scope': ScopeTypes.scope,
            'response_type': 'token'
        }
        print('Press ==>', ''.join((self.URL_AUTH, urlencode(param))))

    client = VKClient(TOKEN, '1')
    client.get_token()
