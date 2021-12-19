import os
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ForceReply

START_IMG = "https://telegra.ph/file/3a7509ff3fa5232e4408d.png"

ALIVE_TEXT = """
**Heya, I'm Online : ) 🍃**
"""

START_TEXT = """
**Hᴇʟʟᴏ** {} 👋
**I ᴀᴍ [Pʀᴀʙʜᴀꜱᴡᴀʀᴀ'ꜱ](https://t.me/IMPrabaSh) PM Bᴏᴛ 😙🍑**

**Pʟᴇᴀꜱᴇ ɴᴏᴛᴇ ᴛʜᴀᴛ ɪ ᴜꜱᴇ ᴛʜɪꜱ ꜰᴏʀ ᴛʜᴇ ᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ ᴏꜰ ᴍʏ ᴍᴀꜱᴛᴇʀ 💨 Yᴏᴜ ᴄᴀɴ ᴛʏᴘᴇ ᴀɴᴅ ꜱᴇɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ʏᴏᴜ ᴡᴀɴᴛ 📨**

**Uꜱᴇ ᴛʜᴇ ɪɴꜰᴏ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀɴᴅ ᴛʜᴇ ᴛᴏᴏʟ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴛᴏᴏʟꜱ 🧬**
"""

GROUP_START_TEXT = """
**Hᴇʟʟᴏ Tʜᴇʀᴇ 👋**
**I ᴀᴍ[ Pʀᴀʙʜᴀꜱᴡᴀʀᴀ'ꜱ](https://t.me/IMPrabaSh) PM ʙᴏᴛ  : )**

**I ᴀᴍ ᴀ ᴠᴇʀʏ ᴘᴏᴡᴇʀꜰᴜʟ ᴍᴜʟᴛɪᴡᴏʀᴋ ʙᴏᴛ 🛡 ᴘʀɪᴠᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ᴍʏ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ ᴀɴᴅ ʜᴇʟᴘ 🎋🍃**
"""

BOTSTATUS_TEXT = """
**Bᴏᴛ Sᴛᴀᴛᴜꜱ** ```rᴏᴏᴛ : ~ $ bᴀꜱʜ```

```#Independent Developers```

**All Copyright©️ goes to Pʀᴀʙᴀsʜᴡᴀʀᴀ 🇱🇰 #Aғᴋ**
"""

GROUP_HELP_TEXT = """
**Heya : ) 🍃**

**You can learn more about the command** /help  **in private messages with me**
"""

INFO_TEXT = """
**Hᴇʟʟᴏ Tʜᴇʀᴇ 👋

I ᴀᴍ ᴀ [Rɪᴠɪʙɪʙᴜ Pʀᴀʙᴀꜱʜᴡᴀʀᴀ](https://t.me/IMPrabaSh) 😙 Tʜɪꜱ ɪꜱ ᴍʏ PM ʙᴏᴛ 🥴

Aʙᴏᴜᴛ Mᴇ

Aɢᴇ 15 😷
Rᴇꜱɪᴅᴇɴᴄᴇ ɪɴ ɢᴀʟʟᴇ 🏝
Sᴄʜᴏᴏʟɪɴɢ ᴀᴛ ʀɪᴄʜᴍᴏɴᴅ ᴄᴏʟʟᴇɢᴇ 🇫🇷
Nᴏ ᴍᴏʀᴇ ʟɪᴋɪɴɢ ꜰᴏʀ ʀᴇʟᴀᴛɪᴏɴꜱʜɪᴘꜱ 😅

Sᴏᴏɴ . . . 🔜

I ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ ᴀꜱ ᴡᴇʟʟ ᴀꜱ ᴀ ᴡᴇʙꜱɪᴛᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ 😶‍🌫️ ɪ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ᴀ ʟᴏᴛ ᴏꜰ ᴛʜɪɴɢꜱ 😮‍💨

Sᴛɪʟʟ ʟᴇᴀʀɴɪɴɢ . . . 🔛

Fɪɴᴀʟʟʏ ʏᴏᴜ ᴄᴀɴ ᴠɪꜱɪᴛ ᴍʏ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴛᴏ ꜱᴇᴇ ᴍʏ ᴘʀᴏᴊᴇᴄᴛꜱ 🎁

Tʜᴀɴᴋꜱ ꜰᴏʀ ꜱᴛᴀʀᴛɪɴɢ ᴍʏ ʙᴏᴛ ❤️**
"""

HELP_TEXT = """
**Hᴇʟᴘ ⚙️**

**Cʜᴏᴏꜱᴇ ᴛʜᴇ ꜱᴜᴘᴘᴏʀᴛ ꜱᴇʀᴠɪᴄᴇ ʏᴏᴜ ɴᴇᴇᴅ.**
"""

MORE_TOOLS = """
**Wᴇʟᴄᴏᴍᴇ ᴛᴏ Mᴏʀᴇ Tᴏᴏʟ ᴍᴇɴᴜ**

**Sᴇʟᴇᴄᴛ ᴀɴʏ ᴏꜰ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴀɴᴅ ꜱᴘᴏɴꜱᴏʀ ᴍʏ ʙᴏᴛ (Tᴇꜱᴛ ᴀʟʟ ᴏꜰ ᴛʜᴇꜱᴇ ᴛᴏᴏʟꜱ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ)**
"""

HOWTOUSE_TEXT = """
**✘ Iɴꜰᴏ Bᴏᴛ ✘**

**⦁ All Copyright©️ goes to [Pʀᴀʙᴀsʜᴡᴀʀᴀ 🇱🇰 #Aғᴋ](https://t.me/ImPrabashwara)**

**⦁ My first telegram project was #Pm Bot 🔐**

**- Status :** `Online ♻️`
**- Help :** `Damantha Jasinghe 🇱🇰`
**- Language :** `Pyrogram 🔛`
**- Bot Type :** `#Pm`
**- BotID :** `2116113147`
**- Bot Username : @ImPrabashbot**
**- Version :** `1.0`

**Keep Bot Up to date** `...`
"""

MUSIC_TEXT = """
**✘ Mᴜꜱɪᴄ ✘**

**Here is the available help for the Music module:)**

**You can either enter just the song name or both the artist and song name.**

• `/song` **<songname artist(optional)>: uploads the song in it's best quality available.**
• `/video` **<songname artist(optional)>: uploads the video song in it's best quality available.**
"""

QUOTLY_TEXT = """
**✘ Qᴜᴏᴛʟʏ ✘**

**Here is the available help for the Quotly module:)**

**Quotly**

• `/q` **or** `/qbot` **- To quote a message.**
• `/q` **INTEGER or** `/qbot` **INTEGER - To quote more than 1 messages.**
• `/q` **r - to quote a message with it's reply.**
"""

OWNER_TEXT = """
**Pʀᴀʙᴀsʜᴡᴀʀᴀ 🇱🇰 Owner of @ImPrabashbot :)**
"""

COMMANDS = """
**Commands List #️⃣**

**Cᴏᴍᴍᴀɴᴅꜱ ᴀʀᴇ ᴀʟʟ ᴀᴛ ʏᴏᴜʀ ᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ.**

`/alive` **- Aʟɪᴠᴇ Bᴏᴛ**
`/start` **- Sᴛᴀʀᴛ Aɴᴅ Uᴘᴅᴀᴛᴇ Bᴏᴛ**
`/owner` **- Cᴏɴᴛᴀᴄᴛ Tʜᴇ Oᴡɴᴇʀ**
`/stats` **- Cʜᴇᴄᴋ Tʜᴇ Sᴛᴀᴛᴜꜱ**
`/help` **- Hᴇʟᴘ Mᴇɴᴜ**
`/info` **- Iɴꜰᴏ Mᴇɴᴜ**
`/social` **- Sᴏᴄɪᴀʟ Mᴇɴᴜ**
`/cmd` **- Aʟʟ Cᴏᴍᴍᴀɴᴅꜱ**

"""

CMD_GROUP_TEXT = """
**Commands List #️⃣**

**Cᴏᴍᴍᴀɴᴅꜱ ᴀʀᴇ ᴀʟʟ ᴀᴛ ʏᴏᴜʀ ᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ.**

`/alive` **- Aʟɪᴠᴇ Bᴏᴛ**
`/start` **- Sᴛᴀʀᴛ Aɴᴅ Uᴘᴅᴀᴛᴇ Bᴏᴛ**
`/owner` **- Cᴏɴᴛᴀᴄᴛ Tʜᴇ Oᴡɴᴇʀ**
`/stats` **- Cʜᴇᴄᴋ Tʜᴇ Sᴛᴀᴛᴜꜱ**
`/help` **- Hᴇʟᴘ Mᴇɴᴜ**
`/info` **- Iɴꜰᴏ Mᴇɴᴜ**
`/social` **- Sᴏᴄɪᴀʟ Mᴇɴᴜ**
`/cmd` **- Aʟʟ Cᴏᴍᴍᴀɴᴅꜱ**

"""
#----------------------------------------game----------------------------------------------------

GAME_TEXT = """
**✘ Gᴀᴍᴇ ✘**

**Play Game With Emojis:**

• `/dice` **or** `/dice` **1 to 6 any value.**
• `/ball` **or** `/ball` **1 to 5 any value.**
• `/dart` **or** `/dart` **1 to 6 any value.**
• `/football` **or** `/football` **1 to 5 any value.**
• `/slot` **or** `/slot` **1 to 6 any value.**
• `/bowl` **or** `/bowl` **1 to 6 any value.**

**Usage: hahaha just a magic.**
**warning: you would be in trouble if you input any other value than mentioned.**

**🚷 There are some bugs in the Games 🚷**
"""
#-------------------------------endgame--------------------------------------------------------

SOCIAL_TEXT = """
**✘ Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ ✘**

**You can follow me on social media below 😇**
"""

SOCIALN_TEXT = """
**✘ Sᴏᴄɪᴀʟ Mᴇᴅɪᴀ ✘**

**You can follow [Pʀᴀʙᴀsʜᴡᴀʀᴀ 🇱🇰](https://t.me/imprabashwara) on social media below 😇**
"""

BOT_STARTED = """
╭━━╮╱╱╱╭╮╱╭━━━╮╭╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮
┃╭╮┃╱╱╭╯╰╮┃╭━╮┣╯╰╮╱╱╱╭╯╰╮╱╱╱╱┃┃
┃╰╯╰┳━┻╮╭╯┃╰━━╋╮╭╋━━┳┻╮╭╋━━┳━╯┃
┃╭━╮┃╭╮┃┃╱╰━━╮┃┃┃┃╭╮┃╭┫┃┃┃━┫╭╮┃
┃╰━╯┃╰╯┃╰╮┃╰━╯┃┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┃
╰━━━┻━━┻━╯╰━━━╯╰━┻╯╰┻╯╰━┻━━┻━━╯

- #Independent_Developers

- All Copyright©️ goes to Pʀᴀʙᴀsʜᴡᴀʀᴀ 🇱🇰 #Aғᴋ
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Aʙᴏᴜᴛ 👁‍🗨', callback_data="info_"),
        InlineKeyboardButton('Dᴇᴠᴇʟᴏᴘᴇʀ 👨‍💻', url="https://t.me/+D6BpKtujY844ZTRl")
        ],
        [InlineKeyboardButton('Hᴇʟᴘ ⚙️', callback_data='help_')
        ],
        [InlineKeyboardButton('- Mᴏʀᴇ Tᴏᴏʟ -', callback_data='more_')
        ],
        [InlineKeyboardButton('➕ Aᴅᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕', url='http://t.me/ImPrabashbot?startgroup=true')
        ]]
  
)


GROUP_START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ],
        [InlineKeyboardButton('Wᴇʙꜱɪᴛᴇ 🌐', url='https://testdeveloper1234.github.io/Prabashwara.github.io/')
        ]]
)

BOTSTATUS_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ]]
)

GROUP_HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', url='http://t.me/ImPrabashbot?start=help')
        ]]
)

BACK_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ꜱᴏᴄɪᴀʟ 💟', callback_data="social_"),
        InlineKeyboardButton('Lᴏɢ Cʜᴀɴɴᴇʟ 🗄', url='https://t.me/ImPrabashwara')
        ],
        [
        InlineKeyboardButton('Wᴇʙꜱɪᴛᴇ 🌐', url='https://testdeveloper1234.github.io/Prabashwara.github.io/')     
        ],
        [InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='help_back')
        ]]  
)

HELP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Cᴏᴍᴍᴀɴᴅꜱ #️⃣', callback_data="cmds_"),
        InlineKeyboardButton('Sᴜᴘᴘᴏʀᴛ ✨', url='https://t.me/InDeveopeR')
        ],
        [
        InlineKeyboardButton('Sᴏʀᴄᴇ ᴄᴏᴅᴇ 🌏', url='https://github.com/WKRPrabashwara/Prabashwara-PM-Bot'),
        InlineKeyboardButton('Cʀᴇᴅɪᴛ 🚫', url='https://telegra.ph/Credit-of-Pm-Bot-Developers-11-22')
        ],
        [
        InlineKeyboardButton('Iɴꜰᴏ Bᴏᴛ 🔐', callback_data='howtouse_')
        ],
        [
        InlineKeyboardButton('🔙 Back', callback_data='help_back')
        ]]
)

HOWTOUSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='help_')
        ]]
)

MORE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('✘ Mᴜꜱɪᴄ ✘', callback_data='music_'),
        InlineKeyboardButton('✘ Qᴜᴏᴛʟʏ ✘', callback_data='quotly_')
        ],
        [
        InlineKeyboardButton('✘ Gᴀᴍᴇ ✘', callback_data='game_')
        ],
        [
        InlineKeyboardButton("✘ Iɴʟɪɴᴇ ✘", switch_inline_query_current_chat="")
        ],
        [
        InlineKeyboardButton('🔙 Back', callback_data='help_back')
        ]]
  
)

CMD_BACK_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='help_')
        ]]
  
)
        
MUSIC_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='more_')
        ]]
)

QUOTLY_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='more_')
        ]]
)

OWNER_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Lᴏɢ Cʜᴀɴɴᴇʟ 🗄', url='https://t.me/ImPrabashwara')
        ],
        [
        InlineKeyboardButton('Wᴇʙꜱɪᴛᴇ 🌐', url='https://testdeveloper1234.github.io/Prabashwara.github.io/'),
        ]]
)

ALIVE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ]]
)

GAME_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='more_')
        ]]
)

SOCIAL_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('• |   ɪɴꜱᴛᴀɢʀᴀᴍ  | •', url='https://www.instagram.com/invites/contact/?i=fwr277e9109s&utm_content=muwrp81'),
        InlineKeyboardButton('• |   ᴛᴇʟᴇɢʀᴀᴍ   | •', url='https://t.me/ImPrabashwara')
        ],
        [
        InlineKeyboardButton('• |    ᴛᴡɪᴛᴛᴇ    | •', url='https://twitter.com'),
        InlineKeyboardButton('• |    ʏᴏᴜᴛᴜʙᴇ   | •', url='https://www.youtube.com/channel/UC7KV1EAx_BAy1WUMNdD_Vfg')
        ],
        [
        InlineKeyboardButton('• |    ꜰᴀᴄᴇʙᴏᴏᴋ  | •', url='https://www.facebook.com/'),
        InlineKeyboardButton('• |   ᴡʜᴀᴛꜱᴀᴘᴘ   | •', url='https://www.whatsapp.com/')
        ],
        [
        InlineKeyboardButton('• |    ɢɪᴛʜᴜʙ    | •', url='https://github.com/WKRPrabashwara'),
        InlineKeyboardButton('• | ꜱᴛᴀᴄᴋᴏᴠᴇʀꜰʟᴏᴡ | •', url='https://stackoverflow.com/users/17521323/rivibibu-prabashwara?tab=profile')
        ],
        [
        InlineKeyboardButton('• |    ᴇᴍᴀɪʟ     | •', url='https://wkprabashwara@gmail.com'),
        InlineKeyboardButton('• |    ᴡᴇʙꜱɪᴛᴇ   | •', url='https://testdeveloper1234.github.io/Prabashwara.github.io/')
        ],
        [
        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='info_')
        ]]
)

SOCIALN_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('• |   ɪɴꜱᴛᴀɢʀᴀᴍ  | •', url='https://www.instagram.com/invites/contact/?i=fwr277e9109s&utm_content=muwrp81'),
        InlineKeyboardButton('• |   ᴛᴇʟᴇɢʀᴀᴍ   | •', url='https://t.me/ImPrabashwara')
        ],
        [
        InlineKeyboardButton('• |    ᴛᴡɪᴛᴛᴇ    | •', url='https://twitter.com'),
        InlineKeyboardButton('• |    ʏᴏᴜᴛᴜʙᴇ   | •', url='https://www.youtube.com/channel/UC7KV1EAx_BAy1WUMNdD_Vfg')
        ],
        [
        InlineKeyboardButton('• |    ꜰᴀᴄᴇʙᴏᴏᴋ  | •', url='https://www.facebook.com/'),
        InlineKeyboardButton('• |   ᴡʜᴀᴛꜱᴀᴘᴘ   | •', url='https://www.whatsapp.com/')
        ],
        [
        InlineKeyboardButton('• |    ɢɪᴛʜᴜʙ    | •', url='https://github.com/WKRPrabashwara'),
        InlineKeyboardButton('• | ꜱᴛᴀᴄᴋᴏᴠᴇʀꜰʟᴏᴡ | •', url='https://stackoverflow.com/users/17521323/rivibibu-prabashwara?tab=profile')
        ],
        [
        InlineKeyboardButton('• |    ᴇᴍᴀɪʟ     | •', url='https://wkprabashwara@gmail.com'),
        InlineKeyboardButton('• |    ᴡᴇʙꜱɪᴛᴇ   | •', url='https://testdeveloper1234.github.io/Prabashwara.github.io/')
        ]]
)

CMD_GROUP_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Sʏꜱᴛᴇᴍ ꜱᴛᴀᴛᴜꜱ 💻', callback_data='stats_')
        ]]
)
