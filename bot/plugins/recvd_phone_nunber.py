from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    Message
)
from bot import (
    AKTIFPERINTAH,
    ALREADY_REGISTERED_PHONE,
    AVAILABLE_CODE_RECVING_OPTIONS,
    CONFIRM_SENT_VIA,
    RECVD_PHONE_NUMBER_DBP
)
from bot.user import User


@Client.on_message(
    filters.text &
    filters.private,
    group=1
)
async def recvd_ph_no_message(_, message: Message):
    w_s_dict = AKTIFPERINTAH.get(message.chat.id)
    if not w_s_dict:
        return
    status_message = w_s_dict.get("START")
    if not status_message:
        return
    # await w_s_dict.get("START").delete()
    del w_s_dict["START"]
    status_message = await message.reply_text(
        RECVD_PHONE_NUMBER_DBP
    )
    loical_ci = User()
    w_s_dict["PHONE_NUMBER"] = message.text
    await loical_ci.connect()
    w_s_dict["SENT_CODE_R"] = await loical_ci.send_code(
        w_s_dict["PHONE_NUMBER"]
    )
    w_s_dict["USER_CLIENT"] = loical_ci
    status_message = await status_message.edit_text(
        ALREADY_REGISTERED_PHONE + "\n\n" + CONFIRM_SENT_VIA.format(
            AVAILABLE_CODE_RECVING_OPTIONS[w_s_dict["SENT_CODE_R"].type]
        )
    )
    w_s_dict["MESSAGE"] = status_message
    AKTIFPERINTAH[message.chat.id] = w_s_dict
    raise message.stop_propagation()
