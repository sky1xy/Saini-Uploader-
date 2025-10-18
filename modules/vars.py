#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27813525"))
API_HASH = environ.get("API_HASH", "4c422dcd8b5d472bfe99f6f66953b96c")
BOT_TOKEN = environ.get("BOT_TOKEN", "8230564085:AAE54WewrkWR8r57FtI4RusMfmPMhKZz7ko")

OWNER = int(environ.get("OWNER", "7565361272"))
CREDIT = environ.get("CREDIT", "ᥫ᭡፝֟፝֟✿𝘼𝙉𝙏𝘼𝙍𝙔𝘼𝙈𝙄 𝘽𝙊𝙏࿐✿")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7565361272').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7565361272').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
