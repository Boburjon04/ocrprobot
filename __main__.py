from pyrogram import Client
import config

DOWNLOAD_LOCATION = "./Downloads"
BOT_TOKEN = config.BOT_TOKEN

Client(
    "YouTubeDlBot",
    bot_token=BOT_TOKEN,
    workers=100
).run()