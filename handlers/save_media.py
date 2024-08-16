# (c) @AbirHasan2005

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def forward_to_channel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.value > 45:
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("𒊹 𝖡𝖺𝗇 𝖴𝗌𝖾𝗋", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await forward_to_channel(bot, message, editable)


async def save_batch_media_in_channel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await forward_to_channel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("➜ 𝖣𝖾𝗅𝖾𝗍𝖾 𝖡𝖺𝗍𝖼𝗁", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=ItachiUchiha_{str_to_b64(str(SaveMessage.id))}"
        await editable.edit(
            f"**➜ 𝖡𝖺𝗍𝖼𝗁 𝖥𝗂𝗅𝖾𝗌 𝖲𝗍𝗈𝗋𝖾𝖽 𝖨𝗇 𝖬𝗒 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 !**\n\n𝖧𝖾𝗋𝖾 𝖨𝗌 𝖳𝗁𝖾 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄 𝖮𝖿 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 : {share_link} \n\n"
            f"➜ 𝖩𝗎𝗌𝗍 𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖦𝖾𝗍 𝖥𝗂𝗅𝖾𝗌!",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🍁 𝖮𝗉𝖾𝗇 𝖫𝗂𝗇𝗄 🍁", url=share_link)],
                 [InlineKeyboardButton("🌧 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/Infinity_Backup"),
                  InlineKeyboardButton("𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 🌥", url="https://t.me/InfinityRobots")]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) 𝖦𝗈𝗍 𝖡𝖺𝗍𝖼𝗁 𝖫𝗂𝗇𝗄 !",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Open Link", url=share_link)]])
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\n𝖦𝗈𝗍 𝖤𝗋𝗋𝗈𝗋 𝖥𝗋𝗈𝗆 `{str(editable.chat.id)}` !!\n\n**➜ 𝖳𝗋𝖺𝖼𝖾𝖻𝖺𝖼𝗄 :** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("𒊹 𝖡𝖺𝗇 𝖴𝗌𝖾𝗋", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def save_media_in_channel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) 𝖦𝗈𝗍 𝖥𝗂𝗅𝖾 𝖫𝗂𝗇𝗄 !",
            disable_web_page_preview=True)
        share_link = f"https://t.me/{Config.BOT_USERNAME}?start=ItachiUchiha_{str_to_b64(file_er_id)}"
        await editable.edit(
            "**➜ 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 𝖲𝗍𝗈𝗋𝖾𝖽 𝖨𝗇 𝖬𝗒 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 !**\n\n"
            f"𝖧𝖾𝗋𝖾 𝖨𝗌 𝖳𝗁𝖾 𝖯𝖾𝗋𝗆𝖺𝗇𝖾𝗇𝗍 𝖫𝗂𝗇𝗄 𝖮𝖿 𝖸𝗈𝗎𝗋 𝖥𝗂𝗅𝖾𝗌 : {share_link} \n\n"
            "➜ 𝖩𝗎𝗌𝗍 𝖢𝗅𝗂𝖼𝗄 𝖳𝗁𝖾 𝖫𝗂𝗇𝗄 𝖳𝗈 𝖦𝖾𝗍 𝖥𝗂𝗅𝖾𝗌 !",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🍁 𝖮𝗉𝖾𝗇 𝖫𝗂𝗇𝗄 🍁", url=share_link)],
                 [InlineKeyboardButton("🌧 𝖴𝗉𝖽𝖺𝗍𝖾𝗌 𝖢𝗁𝖺𝗇𝗇𝖾𝗅", url="https://t.me/Infinity_Backup"),
                  InlineKeyboardButton("𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 🌥", url="https://t.me/InfinityRobots")]]
            ),
            disable_web_page_preview=True
        )
    except FloodWait as sl:
        if sl.value > 45:
            print(f"𝖲𝗅𝖾𝖾𝗉 𝖮𝖿 {sl.value}s 𝖢𝖺𝗎𝗌𝖾𝖽 𝖡𝗒 𝖥𝗅𝗈𝗈𝖽𝖶𝖺𝗂𝗍....")
            await asyncio.sleep(sl.value)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text="#FloodWait:\n"
                     f"Got FloodWait of `{str(sl.value)}s` from `{str(editable.chat.id)}` !!",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await save_media_in_channel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text="#ERROR_TRACEBACK:\n"
                 f"Got Error from `{str(editable.chat.id)}` !!\n\n"
                 f"**Traceback:** `{err}`",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Ban User", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
