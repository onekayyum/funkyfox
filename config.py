from os import getenv
import logging
from logging.handlers import RotatingFileHandler


# ---------------------- ᴄᴏɴғɪɢ ---------------------- #

API_ID = int(getenv("API_ID", "22517234"))
API_HASH = getenv("API_HASH", "a13f39f3effcd7618d2a61481f3c2392")
BOT_TOKEN = getenv("BOT_TOKEN", "6560314978:AAH6mpBnhgyNw-1xs8D1kCgMLpckKRRwav4")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001909805668"))
OWNER_ID = list(map(int, getenv("SUDO_USERS", "6733071568 6867128113").split()))
DB_URI = getenv("DATABASE_URL", "mongodb+srv://raajkundra:Kayamkhani@rajkundra.jsuih8v.mongodb.net/?retryWrites=true&w=majority")
FORCE_SUB_CHANNEL = int(getenv("FORCE_SUB_CHANNEL", "-1001909805668"))
BOT_WORKERS = int(getenv("BOT_WORKERS", "5"))

# --------- ʟɪɴᴋ sʜᴏʀᴛɴᴇʀ ᴄᴏɴᴠᴇʀᴛᴇʀ ---------
URL_SHORTNER_API = getenv("URL_SHORTNER_API", "https://publicearn.com/api?api=ffe90fdeaa90e3518ad52debe75d4d493adb2b90&url=yourdestinationlink.com&alias=CustomAlias")
URL_SHORTNER_API_KEY = getenv("URL_SHORTNER_API_KEY", "ffe90fdeaa90e3518ad52debe75d4d493adb2b90")


default_custom_caption = """
📁 {file_caption}
━━━━━━━━━━━━━━━━━━━━━━━━━━━   
ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴠɪᴅᴇᴏ ᴛʜᴀɴ ᴘʟᴇᴀsᴇ 
ᴀᴅᴅ sᴏᴍᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
CUSTOM_CAPTION = getenv("CUSTOM_CAPTION", default_custom_caption)

# --» sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʀᴇᴠᴇɴᴛ ᴜsᴇʀs ғʀᴏᴍ ғᴏʀᴡᴀʀᴅɪɴɢ ғɪʟᴇs ғʀᴏᴍ ʙᴏᴛ
if getenv("PROTECT_CONTENT", None) == 'True':
    PROTECT_CONTENT = True
else:
    PROTECT_CONTENT = False


# --> sᴇᴛ ᴛʀᴜᴇ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪsᴀʙʟᴇ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛs sʜᴀʀᴇ ʙᴜᴛᴛᴏɴ
if getenv("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False




LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
