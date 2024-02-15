import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST: str = os.getenv("EMAIL_HOST")
EMAIL_PORT: int = int(os.getenv("EMAIL_PORT"))
EMAIL_USER: str = os.getenv("EMAIL_USER")
FROM_EMAIL: str = os.getenv("FROM_EMAIL")
EMAIL_PASSWORD: str = os.getenv("EMAIL_PASSWORD")
KEYSTROKE_PER_MAIL = int(os.getenv("KEYSTROKE_PER_MAIL"))
