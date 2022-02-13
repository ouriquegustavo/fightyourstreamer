import json
import time
import string
import random
import requests
import webbrowser
from pywitch import validate_token

valid_char = string.ascii_letters + string.digits


def random_string(length):
    return ''.join([random.choice(valid_char) for i in range(length)])


class Auth:
    def __init__(self, game):
        self.game = game
        try:
            with open('token.json', 'r') as cfg_file:
                self.token = json.load(cfg_file)['token']
        except:
            self.token = None
        self.auth_server = 'https://pywitch-auth.herokuapp.com'
        self.auth_client_id = '9lzu5wqst0swbinmvqpqu80failj3l'
        self.auth_scopes = ['user:read:email']

        self.start()

    def get_auth_url(self, auth_endpoint='authenticate'):
        self.auth_endpoint = auth_endpoint
        self.auth_state_length = 128
        self.auth_state = random_string(self.auth_state_length)
        self.auth_scopes_str = '%20'.join(self.auth_scopes)

        self.auth_url = (
            'https://id.twitch.tv/oauth2/authorize'
            '?response_type=code'
            f'&client_id={self.auth_client_id}'
            f'&redirect_uri={self.auth_server}/{self.auth_endpoint}'
            f'&scope={self.auth_scopes_str}'
            f'&state={self.auth_state}'
        )
        return self.auth_url, self.auth_state

    def get_token(self, state, state_endpoint='state'):
        self.auth_state = state
        self.state_endpoint = state_endpoint
        url = f'{self.auth_server}/{self.state_endpoint}'
        params = {'state': self.auth_state}
        response = requests.get(url, params=params)
        data = response.json()
        token = data.get('access_token')
        return token

    def validate(self, token):
        try:
            self.validation, self.helix_headers = validate_token(
                token, verbose=False
            )
        except Exception as e:
            self.validation = {}
        return self.validation

    def start(self):
        validation = self.validate(self.token)
        if not validation:
            url, state = self.get_auth_url()
            webbrowser.open(url)
            time.sleep(3)
            self.token = self.get_token(state)
            with open('token.json', 'w') as cfg_file:
                cfg_file.write(json.dumps({'token': self.token}))
