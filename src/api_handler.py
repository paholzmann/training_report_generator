import os
import requests
import time
import datetime
from src.utilities import ENV_Utilities, JSON_Utilities

class API_Handler:
    def __init__(self):
        # ENV SECRETS
        self.env_utils = ENV_Utilities()
        self.env_variables = self.env_utils.load_env_variables()
        self.base_url = self.env_variables["base_url"]
        self.token_url = self.env_variables["token_url"]
        self.client_id = self.env_variables["client_id"]
        self.client_secret = self.env_variables["client_secret"]

        # JSON SECRETS
        self.json_utils = JSON_Utilities()
        self.json_secrets = self.json_utils.load_json_secrets()
        self.access_token = self.json_secrets["access_token"]
        self.refresh_token = self.json_secrets["refresh_token"]
        self.expires_at = self.json_secrets["expires_at"]

        self._validate_secrets()

    def _validate_secrets(self) -> None:
        required = {
        "base_url": self.base_url,
        "token_url": self.token_url,
        "client_id": self.client_id,
        "client_secret": self.client_secret,
        "access_token": self.access_token,
        "refresh_token": self.refresh_token,
        "expires_at": self.expires_at,
        }
        missing = [key for key, value in required.items() if not value]
        if missing:
            raise ValueError(f"Missing secrets: {','.join(missing)}")


    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(
                f"Strava API request failed: {response.status_code} - {response.text}"
            )
        return response.json()
    
class TokenManagement:
    def __init__(self):
        self.api_handler = API_Handler()

    def _get_token(self) -> dict:
        payload = {
            "client_id": self.api_handler.client_id,
            "client_secret": self.api_handler.client_secret,
            "refresh_token": self.api_handler.refresh_token,
            "grant_type": "refresh_token"
        }
        response = requests.post(self.api_handler.token_url, data=payload, timeout=30)
        response.raise_for_status()
        return response.json()
    
    def is_token_expired(self, expires_at: int | float) -> bool:
        return time.time() >= expires_at - 30
    
    def replace_expired_secrets(self, expired: bool) -> None:
        if expired:
            json_secrets = self._get_token()
            self.api_handler.json_utils.insert_json_secrets(json_secrets=json_secrets)
            self.api_handler.access_token = json_secrets["access_token"]
            self.api_handler.expires_at = json_secrets["expires_at"]
            self.api_handler.refresh_token = json_secrets["refresh_token"]



if __name__ == "__main__":
    tm = TokenManagement()
    expired = tm.is_token_expired(expires_at=tm.api_handler.expires_at)
    tm.replace_expired_secrets(expired=expired)