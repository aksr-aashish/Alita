from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    APP_ID = int(config("APP_ID"))
    API_HASH = config("API_HASH")
    OWNER_ID = int(config("OWNER_ID", default=1198820588))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-1001744920557))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="alita")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="DivideSupport")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="DivideProjects")
    ENABLED_LOCALES = [str(i) for i in config("ENABLED_LOCALES", default="en").split()]
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "5212174041:AAGbPP_gU-Ysb6zpaoQFPKJABLnGNAwIN4g"
    APP_ID = 6  # Your APP_ID from Telegram
    API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"  # Your APP_HASH from Telegram
    OWNER_ID = 5001573230  # Your telegram user id
    MESSAGE_DUMP = -1001744920557  # Your Private Group ID for logs
    DEV_USERS = [5001573230]
    SUDO_USERS = [5001573230]
    WHITELIST_USERS = [5001573230]
    DB_URI = "mongodb+srv://scanner:vexana@cluster0.yrs1w.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "vexu"
    NO_LOAD = []
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "Vexana_Support"
    SUPPORT_CHANNEL = "Vexana_Support"
    ENABLED_LOCALES = ["ENABLED_LOCALES"]
    WORKERS = 8
