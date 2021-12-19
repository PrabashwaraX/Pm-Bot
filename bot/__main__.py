# @Damantha_Jasinghe

from bot.plugins import *
from bot.plugins.privet import *
from bot.plugins.song import *
from pyrogram import idle, filters
from bot import tele, bot
from bot import LOGGER
from configs import Config
from info import BOT_STARTED

bot.start()
tele.start(bot_token=Config.BOT_TOKEN)
LOGGER.info(BOT_STARTED)
idle()
