import os
import time
import shutil
import psutil
import pyrogram
import subprocess

from sys import version as pyver
from pyrogram import Client, filters, idle
from pyrogram.types import Message, User
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from configs import Config
from bot import LOGGER
from bot import bot
from bot.helpers.humanbytes import humanbytes
from bot.helpers.database.access_db import db
from bot.helpers.broadcast import broadcast_handler
from bot.helpers.stats import bot_sys_stats
from bot.helpers.database.add_user import AddUserToDatabase
from info import START_IMG, START_TEXT, OWNER_TEXT, GROUP_HELP_TEXT, CMD_GROUP_TEXT, CMD_GROUP_BUTTON, BOTSTATUS_TEXT, SOCIALN_TEXT, SOCIALN_BUTTON, SOCIAL_TEXT, SOCIAL_BUTTON, BOTSTATUS_BUTTON, GROUP_HELP_BUTTON, ALIVE_TEXT, GAME_TEXT, GAME_BUTTON, ALIVE_BUTTON, OWNER_BUTTON, START_BUTTON, BOT_STARTED, INFO_TEXT, HOWTOUSE_TEXT, HOWTOUSE_BUTTON, BACK_BUTTON, HELP_TEXT, MORE_TOOLS, HELP_BUTTON, MORE_BUTTON, COMMANDS, CMD_BACK_BUTTON, GROUP_START_TEXT, GROUP_START_BUTTON, MUSIC_TEXT, QUOTLY_TEXT, MUSIC_BUTTON, QUOTLY_BUTTON


IF_TEXT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"
IF_CONTENT = "<b>Message from:</b> {} \n<b>Name:</b> {}"

@bot.on_message(filters.private & filters.incoming & filters.command(["start"]))
async def start(bot, update):
    await AddUserToDatabase(bot, update)    
    await update.reply_photo(START_IMG)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.private & filters.incoming & filters.command(["alive"]))
async def alive(bot, update):
    await update.reply_text(
        text=ALIVE_TEXT,
        reply_markup=ALIVE_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("alive") & ~filters.private & ~filters.channel)
async def alive(bot, update):
    await update.reply_text(
        text=ALIVE_TEXT,
        reply_markup=ALIVE_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.private & filters.incoming & filters.command(["status"]))
async def status(bot, update):
    await update.reply_text(
        text=BOTSTATUS_TEXT,
        reply_markup=BOTSTATUS_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("status") & ~filters.private & ~filters.channel)
async def status(bot, update):
    await update.reply_text(
        text=BOTSTATUS_TEXT,
        reply_markup=BOTSTATUS_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def group_start(bot, update):
    await update.reply_text(
        text=GROUP_START_TEXT,
        reply_markup=GROUP_START_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def group_help(bot, update):
    await update.reply_text(
        text=GROUP_HELP_TEXT,
        reply_markup=GROUP_HELP_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command(["help"]))
async def help(bot, update):
    await AddUserToDatabase(bot, update)    
    await update.reply_photo(
        START_IMG,
        caption=HELP_TEXT.format(update.from_user.mention),
        reply_markup=HELP_BUTTON
    )        

@bot.on_message(filters.private & filters.incoming & filters.command(["info"]))
async def info(bot, update):
    await update.reply_text(
        text=INFO_TEXT,
        reply_markup=BACK_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("owner") & ~filters.private & ~filters.channel)
async def owner(bot, update):
    await update.reply_text(
        text=OWNER_TEXT,
        reply_markup=OWNER_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.private & filters.incoming & filters.command(["owner"]))
async def owner(bot, update):
    await update.reply_text(
        text=OWNER_TEXT,
        reply_markup=OWNER_BUTTON,
        disable_web_page_preview=True
    )

@bot.on_message(filters.command("social") & ~filters.private & ~filters.channel)
async def socialn(bot, update):
    await update.reply_text(
        text=SOCIALN_TEXT,
        reply_markup=SOCIALN_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.private & filters.incoming & filters.command(["cmd"]))
async def cmd(bot, update):
    await update.reply_text(
        text=CMD_GROUP_TEXT,
        reply_markup=CMD_GROUP_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.command("cmd") & ~filters.private & ~filters.channel)
async def cmd(bot, update):
    await update.reply_text(
        text=CMD_GROUP_TEXT,
        reply_markup=CMD_GROUP_BUTTON,
        disable_web_page_preview=True
    )
    
@bot.on_message(filters.private & filters.incoming & filters.command(["football"]))
async def ball(bot, update):
    await update.reply_text("⚽️")
    
@bot.on_message(filters.private & filters.incoming & filters.command(["dice"]))
async def dice(bot, update):
    await update.reply_text(
        text="🎲",
        disable_web_page_preview=True
    )
@bot.on_message(filters.private & filters.incoming & filters.command(["dart"]))
async def dart(bot, update):
    await update.reply_text(
        text="🎯",
        disable_web_page_preview=True
    ) 
@bot.on_message(filters.private & filters.incoming & filters.command(["slot"]))
async def slot(bot, update):
    await update.reply_text(
        text="🎰",
        disable_web_page_preview=True
    ) 
@bot.on_message(filters.private & filters.incoming & filters.command(["bowl"]))
async def bowl(bot, update):
    await update.reply_text(
        text="🎳",
        disable_web_page_preview=True
    )
@bot.on_message(filters.private & filters.incoming & filters.command(["ball"]))
async def ball(bot, update):
    await update.reply_text(
        text="🏀",
        disable_web_page_preview=True
    ) 
    
@bot.on_message(filters.private & filters.command("broadcast") & filters.user(Config.OWNER) & filters.reply)
async def _broadcast(_, bot: Message):
    await broadcast_handler(bot)    
    
@bot.on_message(filters.private & filters.command("stats") & filters.user(Config.OWNER))
async def show_status_count(_, bot: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await bot.reply_text(
        text=f"**💽 Tᴏᴛᴇʟ Dɪꜱᴋ Sᴘᴀᴄᴇ:** {total} \n**💿 Uꜱᴇᴅ Sᴘᴀᴄᴇ:** `{used}({disk_usage}%)` \n**📊 Fʀᴇᴇ Sᴘᴀᴄᴇ:** `{free}` \n**Cᴘᴜ Uꜱᴀɢᴇ:** `{cpu_usage}%` \n**Rᴀᴍ Uꜱᴀɢᴇ:** `{ram_usage}%` \n\n**Tᴏᴛᴀʟ Uꜱᴇʀꜱ 👀:** `{total_users}`\n\n**@IᴍPʀᴀʙᴀꜱʜBᴏᴛ 🛡**",
        parse_mode="Markdown",
        quote=True
    )      
    
@bot.on_callback_query(filters.regex("stats_"))
async def stats_callbacc(_, CallbackQuery):
    text = await bot_sys_stats()
    await bot.answer_callback_query(CallbackQuery.id, text, show_alert=True)  
    
# ============== callback ==============
    
@bot.on_callback_query()
async def cb_data(bot, update):  
    if update.data == "info_":
        await update.message.edit_text(
            text=INFO_TEXT,
            reply_markup=BACK_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "help_back":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=START_BUTTON,
            disable_web_page_preview=True
        )  
    elif update.data == "help_":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=HELP_BUTTON,
            disable_web_page_preview=True
        )          
    elif update.data == "dev_":
        await update.message.edit_text(
            text=DEV_TEXT,
            reply_markup=DEV_BUTTON,
            disable_web_page_preview=True
        )    
    elif update.data == "more_":
        await update.message.edit_text(
            text=MORE_TOOLS,
            reply_markup=MORE_BUTTON,
            disable_web_page_preview=True
        ) 
    elif update.data == "cmds_":
        await update.message.edit_text(
            text=COMMANDS,
            reply_markup=CMD_BACK_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "music_":
       await update.message.edit_text(
           text=MUSIC_TEXT,
           reply_markup=MUSIC_BUTTON,
           disable_web_page_preview=True
        )
    elif update.data == "quotly_":
       await update.message.edit_text(
           text=QUOTLY_TEXT,
           reply_markup=QUOTLY_BUTTON,
           disable_web_page_preview=True
        )
    elif update.data == "howtouse_":
       await update.message.edit_text(
           text=HOWTOUSE_TEXT,
           reply_markup=HOWTOUSE_BUTTON,
           disable_web_page_preview=True
        )
    
    elif update.data == "game_":
       await update.message.edit_text(
           text=GAME_TEXT,
           reply_markup=GAME_BUTTON,
           disable_web_page_preview=True
        )
    
    elif update.data == "social_":
       await update.message.edit_text(
           text=SOCIAL_TEXT,
           reply_markup=SOCIAL_BUTTON,
           disable_web_page_preview=True
        )

@bot.on_message(filters.private & filters.text)
async def pm_text(bot, message):
    if message.from_user.id == Config.BOT_OWNER:
        await reply_text(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.send_message(
        chat_id=Config.BOT_OWNER,
        text=IF_TEXT.format(reference_id, info.first_name, message.text),
        parse_mode="html"
    )

@bot.on_message(filters.private & filters.media)
async def pm_media(bot, message):
    if message.from_user.id == Config.BOT_OWNER:
        await replay_media(bot, message)
        return
    info = await bot.get_users(user_ids=message.from_user.id)
    reference_id = int(message.chat.id)
    await bot.copy_message(
        chat_id=Config.BOT_OWNER,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        caption=IF_CONTENT.format(reference_id, info.first_name),
        parse_mode="html"
    )

@bot.on_message(filters.user(Config.BOT_OWNER) & filters.text & filters.private)
async def reply_text(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.send_message(
            text=message.text,
            chat_id=int(reference_id)
        )    


@bot.on_message(filters.user(Config.BOT_OWNER) & filters.media & filters.private)
async def replay_media(bot, message):
    reference_id = True
    if message.reply_to_message is not None:
        file = message.reply_to_message
        try:
            reference_id = file.text.split()[2]
        except Exception:
            pass
        try:
            reference_id = file.caption.split()[2]
        except Exception:
            pass
        await bot.copy_message(
            chat_id=int(reference_id),
            from_chat_id=message.chat.id,
            message_id=message.message_id,
            parse_mode="html"
        )                 
       
# ======================= main cmd ==================================================== #

@bot.on_message(filters.command('ball') & filters.private)
def command1(bot, on_message):
    bot.send_message(message.chat.id, "bool")
