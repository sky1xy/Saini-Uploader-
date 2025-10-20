#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29467268"))
API_HASH = environ.get("API_HASH", "314e5ae9ce4f78ef127a5a04a5c97649")
BOT_TOKEN = environ.get("BOT_TOKEN", "8188266739:AAFKXz3lxv4Na5WZWZzy5cUhQeolQVdRv-0")

OWNER = int(environ.get("OWNER", "6579568737"))
CREDIT = environ.get("CREDIT", "ᥫ᭡፝֟፝֟✿𝘼𝙉𝙏𝘼𝙍𝙔𝘼𝙈𝙄 𝘽𝙊𝙏࿐✿")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '6579568737').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '6579568737').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

