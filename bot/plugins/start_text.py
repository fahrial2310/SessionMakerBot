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
    SUPPORT_GRP,
    SUPPORT_MODE      
)
from __init__ import Var, TXT

Bot = Client(
      "SessionMakerBot"
      api_hash=Var.API_HASH, 
      api_id=Var.APP_ID, 
      bot_token=Var.TG_BOT_TOKEN,
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

@Bot.on_callback_query()
async def cdata(c, q):
    chat_id = q.from_user.id 
    data = q.data
    if data == "help":
    await q.answer(wait)
    await q.message.edit_text( text=Tr.START_OTHER_USER_TEXT + "\n" + INPUT_PHONE_NUMBER,  
    disable_web_page_preview=True )

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
                     InlineKeyboardButton(" Help ", callback_data ="help"),
                     InlineKeyboardButton(f"{em} {SUPPORT_MODE}", url=f"t.me/{SUPPORT_GRP}")],
                    [InlineKeyboardButton("☠️ Repo PyrogramBot ☠️", url="https://github.com/fahrial2310/PyrogramSessionMaker")
                    ]]
                )
            )
