import os
import requests

from src.utilities import ENV_Utilities

class API_Handler:
    def __init__(self):
        self.env_utils = ENV_Utilities()
        self.env_variables = self.env_utils.load_env_variables()
        self.url = self.env_variables["base_url"]
        self.client_id = self.env_variables["client_id"]
        self.client_secret = self.env_variables["client_secret"]
        self.access_token = self.env_variables["access_token"]
        self.refresh_token = self.env_variables["refresh_token"]

    def _get(self, endpoint: str, params: dict | None = None) -> dict:
        url = f"{self.env_variables["base_url"]}{endpoint}"
        access_token = self.env_variables["access_token"]
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(
                f"Strava API request failed: {response.status_code} - {response.text}"
            )
        return response.json()
    

if __name__ == "__main__":
    print(API_Handler()._get("/athlete"))