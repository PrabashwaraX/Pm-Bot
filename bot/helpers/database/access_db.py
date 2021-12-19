import os
from configs import Config
from bot.helpers.database.database import Database

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
