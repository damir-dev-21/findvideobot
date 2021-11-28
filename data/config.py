from environs import load_dotenv
import os

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMINS")
]

aiogram_redis = {
    'host':os.getenv('ip')
}

redis = {
    "address":(os.getenv("ip"),6379),
    "encoding":'utf8',
}
