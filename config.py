# (©)Codexbotz
# Recode by @mrismanaziz
# t.me/SharingUserbot & t.me/Lunatic0de

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6260157665:AAHN-KjExhNyjsSDPx-tfANdxMDEpVHI6Ig")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "9774346"))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "a92aed7d74654a563af4b07efbcd88e9")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001875828537"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Eror_404_NF")

# Heroku Credentials for updater.
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)

# Database
DB_URI = os.environ.get("DATABASE_URL", "postgres://xmexatur:LSosh0AXDENMdukjfgLBoM1OXJEaVp7U@berry.db.elephantsql.com/xmexatur")

# Protect Content
PROTECT_CONTENT = strtobool(os.environ.get("PROTECT_CONTENT", "True"))

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Zoids_Robot")
GROUP = os.environ.get("GROUP", "Zoidssupport")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "-1001622555655"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "-1001812330560"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))
FORCE_SUB_5 = int(os.environ.get("FORCE_SUB_5", "0"))
FORCE_SUB_6 = int(os.environ.get("FORCE_SUB_6", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>👩‍💻 𝑯𝒂𝒍𝒍𝒐 {first}</b>\n\n<b>✨ 𝑼𝒏𝒕𝒖𝒌 𝑴𝒆𝒏𝒅𝒂𝒑𝒂𝒕𝒌𝒂𝒏 𝑨𝒔𝒖𝒑𝒂𝒏 𝑮𝒓𝒂𝒕𝒊𝒔 𝑨𝒏𝒅𝒂 𝑯𝒂𝒓𝒖𝒔 𝑱𝒐𝒊𝒏 𝑻𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝑫𝒂𝒉𝒖𝒍𝒖\n✨ 𝑻𝒆𝒕𝒂𝒑 𝑺𝒕𝒂𝒚 𝑨𝒈𝒂𝒓 𝒃𝒊𝒔𝒂 𝑻𝒆𝒓𝒖𝒔 𝒅𝒂𝒑𝒂𝒕 𝑨𝒌𝒔𝒆𝒔 𝑽𝒊𝒅𝒆𝒐 𝑻𝒆𝒓𝒖𝒑𝒅𝒂𝒕𝒆\n\n👩‍💻 𝑱𝒊𝒌𝒂 𝑩𝒐𝒕 𝑴𝒂𝒕𝒊 𝒂𝒕𝒂𝒘 𝑩𝒆𝒓𝒌𝒆𝒏𝒅𝒂𝒍𝒂 𝑳𝒂𝒑𝒐𝒓 𝒌𝒆 @Eror_404_NF.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "5751992673 6519126726").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>👩‍💻 𝑯𝒂𝒍𝒍𝒐 {first}</b>\n\n<b>✨ 𝑼𝒏𝒕𝒖𝒌 𝑴𝒆𝒏𝒅𝒂𝒑𝒂𝒕𝒌𝒂𝒏 𝑨𝒔𝒖𝒑𝒂𝒏 𝑮𝒓𝒂𝒕𝒊𝒔 𝑨𝒏𝒅𝒂 𝑯𝒂𝒓𝒖𝒔 𝑱𝒐𝒊𝒏 𝑻𝒆𝒓𝒍𝒆𝒃𝒊𝒉 𝑫𝒂𝒉𝒖𝒍𝒖\n✨ 𝑻𝒆𝒕𝒂𝒑 𝑺𝒕𝒂𝒚 𝑨𝒈𝒂𝒓 𝒃𝒊𝒔𝒂 𝑻𝒆𝒓𝒖𝒔 𝒅𝒂𝒑𝒂𝒕 𝑨𝒌𝒔𝒆𝒔 𝑽𝒊𝒅𝒆𝒐 𝑻𝒆𝒓𝒖𝒑𝒅𝒂𝒕𝒆\n\n👩‍💻 𝑱𝒊𝒌𝒂 𝑩𝒐𝒕 𝑴𝒂𝒕𝒊 𝒂𝒕𝒂𝒘 𝑩𝒆𝒓𝒌𝒆𝒏𝒅𝒂𝒍𝒂 𝑳𝒂𝒑𝒐𝒓 𝒌𝒆 @Eror_404_NF.</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.extend(())


LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
