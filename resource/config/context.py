import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(Path(__file__).parent.parent.parent / '.env')
# print(f"Loading .env file from: {env_path}")
load_dotenv(dotenv_path=env_path)

TARGET_URL = os.getenv('URL')
print(f"Target URL from .env: {TARGET_URL}")