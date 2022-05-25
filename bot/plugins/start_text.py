from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from bot import (
    AKTIFPERINTAH,
    COMMM_AND_PRE_FIX,
    START_COMMAND,
    START_OTHER_USERS_TEXT,
    INPUT_PHONE_NUMBER,
    CH_EMOJI as emoj,
    OWN_EMOJI as emo,
    GRP_EMOJI as em,
    CREATOR_USERNAME,
    UPDATES_CH,
    CREATOR_MODE,
    UPDATES_MODE,
    SUPPORT_GRP
        
)


@Client.on_message(
    filters.command(START_COMMAND, COMMM_AND_PRE_FIX) &
    filters.private
)
async def num_start_message(_, message: Message):
    AKTIFPERINTAH[message.chat.id] = {}
    status_message = await message.reply_text(
        START_OTHER_USERS_TEXT + "\n" + INPUT_PHONE_NUMBER
    )
    AKTIFPERINTAH[message.chat.id]["START"] = status_message
    raise message.stop_propagation()


@Client.on_message(filters.private & filters.command('start'))
def _start(client, message):
    chatID = message.chat.id
    photoUrl = "https://telegra.ph/file/1014cfb47e131f3bc2bc9.jpg"
    client.send_photo(chatID, photoUrl, 
    parse_mode = "markdown", 
    caption = "**Pyrogram String Session Maker**\nPlease Read : /help", 
    reply_to_message_id = message.message_id, 
    reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton(f"{emo} {CREATOR_MODE}", url=f"t.me/{CREATOR_USERNAME}")],
                    [InlineKeyboardButton(f"{emoj} {UPDATES_MODE}", url=f"t.me/{UPDATES_CH}"),
                     InlineKeyboardButton(f"{em} {SUPPORT_GRP}", url=f"t.me/{SUPPORT_GRP}")],
                    [InlineKeyboardButton("☠️ Repo PyrogramBot ☠️", url="https://github.com/fahrial2310/PyrogramSessionMaker")
                    ]]
                )
            )
