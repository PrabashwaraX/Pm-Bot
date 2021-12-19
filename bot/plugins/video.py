from __future__ import unicode_literals
import os
import wget
import requests
from yt_dlp import YoutubeDL
from pyrogram import  filters
from pyrogram.types import  InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch


from bot import bot

@bot.on_message(filters.command(["video"]))
async def vsong(pbot, message):
    ydl_opts = {
        'format':'best',
        'keepvideo':True,
        'prefer_ffmpeg':False,
        'geo_bypass':True,
        'outtmpl':'%(title)s.%(ext)s',
        'quite':True
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"thumb{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]
        views = results[0]["views"]
        results[0]["url_suffix"]
        results[0]["views"]
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
        rby = message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("📥 **downloading video. . .**")
        with YoutubeDL(ydl_opts) as ytdl:
            rep = f'🏷 **Video name**: [{title[:35]}]({link})\n⏱️ **Video Duration**: `{duration}`\n👁‍🗨 **Video Views**: `{views}`\n**🎧 Requested by:** {message.from_user.mention}\n **👑Powerd By: @ImPrabash** '
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"❌**YouTube Download Error !** {str(e)}\n\n **Go support chat @ImPrabash**")
    preview = wget.download(thumbnail)
    await msg.edit("📤 **uploading video. . .**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=rep,
        reply_markup= button)
    try:
        os.remove(file_name)
        msg.delete()
    except Exception as e:
        print(e)
        
