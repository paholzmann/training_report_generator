import os
import json
from dotenv import load_dotenv, dotenv_values

class ENV_Utilities:
    def __init__(self):
        pass
    
    def load_env_variables(self) -> dict[str, str]:
        load_dotenv()
        return {
            "base_url": os.getenv("BASE_URL"),
            "token_url": os.getenv("TOKEN_URL"),
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            }


class JSON_Utilities:
    def __init__(self):
        pass

    def load_json_secrets(self) -> dict[str, str]:
        with open("configs/tokens.json", "r", encoding="utf-8") as f:
            json_secrets = json.load(f)
        return json_secrets

    def insert_json_secrets(self, json_secrets: dict[str, str]) -> None:
        with open("configs/tokens.json", "w", encoding="utf-8") as f:
            json.dump(json_secrets, f, indent=4)

if __name__ == "__main__":
    print(ENV_Utilities().load_env_variables())