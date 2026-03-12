import os
from dotenv import load_dotenv, dotenv_values

class ENV_Utilities:
    def __init__(self):
        pass
    
    def load_env_variables(self) -> dict[str, str]:
        load_dotenv()
        return {
            "base_url": os.getenv("BASE_URL"),
            "clint_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            "access_token": os.getenv("ACCESS_TOKEN"),
            "refresh_token": os.getenv("REFRESH_TOKEN")
            }


if __name__ == "__main__":
    print(ENV_Utilities().load_env_variables())