# Plugin by @MrItzMe
# Anki Vector Updates <https://t.me/ankivectorUpdates>

import os
import requests
import aiohttp
import yt_dlp
from pytube import YouTube
from bot import bot
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@bot.on_message(filters.command('song'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("**Processing. . . 🚀**")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
#        thumbnail = "AgADBQADE68xG3v76VQGd4rAF9CuHwAUAg"
#        thumb_name = f'thumb{title}.jpg'
#        thumb = (thumbnail)
#        open(thumb_name, 'wb').write(thumb)

        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]
        button = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Watch On Youtube🎬", url=f"{link}")
        ],
        [
            InlineKeyboardButton("Search Here 🔎", switch_inline_query_current_chat="")
        ]
    ]
    
    )
        yt = YouTube(link)
    except Exception as e:
        m.edit(f"**❌ Found Nothing.\n\nTry another keywork or maybe spell it properly.**\n\n`Error is :-\n{e}`")
        return
    m.edit("📥 **downloading Song. . .**")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'**Video name**: [{title[:35]}]({link})\n⏱️ **Video Duration**: `{duration}`\n👁‍🗨 **Video Views**: `{views}`\n**👑Powerd By : @ImPrabash**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, reply_markup= button, parse_mode='md', title=title, duration=dur, performer=str(yt.author))
        m.delete()
    except Exception as e:
        m.edit(
            f"**PM Bots's Client Error...!**\n\n"
            f"**Forward this to @ImPrabash**\n\n"
            f"__--------------------Starting Crash Log--------------------__\n"
            f"{e}`\n__--------------------Finishing Crash Log-------------------__\n"
            f"\nPowerd By: @ImPrabash"
        )

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
