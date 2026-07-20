import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

CHANNELS = [
    os.getenv("CHANNEL_1"),
    os.getenv("CHANNEL_2"),
    os.getenv("CHANNEL_3"),
]
