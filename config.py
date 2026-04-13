import os
from typing import List

API_ID = os.environ.get("30422005", "")
API_HASH = os.environ.get("5170ded206641d73215baf40175a6924", "")
BOT_TOKEN = os.environ.get("8632689597:AAGY15OjOiRrjuUWQ_ldYKEEgVzUuxYsg90", "")
PICS = (os.environ.get("PICS", "https://litter.catbox.moe/xq8ekr08gqhzp7ik.jpg")).split()
ADMIN = int(os.environ.get("8206476526", ""))
LOG_CHANNEL = int(os.environ.get("-1003710487004", ""))
DB_URI = os.environ.get("mongodb+srv://shnwazx12:q0BzGZZKAANUDJ9l@shnwaz3.zqupsee.mongodb.net/?appName=Shnwaz3", "")
DB_NAME = os.environ.get("shnwazx12E", "")
IS_FSUB = os.environ.get("True", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("-1002946670816", "").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("-1003406785618", "").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
