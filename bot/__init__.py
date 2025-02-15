import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler
from bot.get_config import get_config

# apparently, no error appears even if the path does not exists
load_dotenv("config.env")

class Var(object):
# The Telegram API things
# Get these values from my.telegram.org or Telegram: @useTGxBot
API_HASH = get_config("API_HASH", should_prompt=True)
APP_ID = get_config("APP_ID", should_prompt=True)
# get a token from @BotFather
TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", should_prompt=True)
CH_EMOJI = get_config("CH_EMOJI", "🔔")
GRP_EMOJI =get_config("GRP_EMOJI", "📣")
OWN_EMOJI = get_config("OWN_EMOJI", "☠️")
CREATOR_USERNAME = get_config("CREATOR_USERNAME", "Alvin_Junior")
UPDATES_CH = get_config("UPDATES_CH", "Alvin_Image_Editor")
SUPPORT_GRP = get_config("SUPPORT_GRP", "Alvin_Image_Editor_Group")
SUPPORT_MODE = get_config("SUPPORT_MODE", "Support")
UPDATES_MODE = get_config("UPDATES_MODE", "Updates")
CREATOR_MODE = get_config("CREATOR_MODE", "Creator")

# Number of update workers to use.
# 4 is the recommended (and default) amount,
# but your experience may vary.
# Note that going crazy with more workers
# wont necessarily speed up your bot,
# given the amount of sql data accesses,
# and the way python asynchronous calls work.
TG_BOT_WORKERS = int(get_config("TG_BOT_WORKERS", "4"))
#
COMMM_AND_PRE_FIX = get_config("COMMM_AND_PRE_FIX", "/")
# start command
START_COMMAND = get_config("START_COMMAND", "help")
# path to store LOG files
LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "SessionMakerBot.log")


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    """ get a Logger object """
    return logging.getLogger(name)


# a dictionary to store the currently running processes
AKTIFPERINTAH = {}
# a dictionary to store the human frinedly names
# of different sent_code types
AVAILABLE_CODE_RECVING_OPTIONS = {
    "app": "Telegram app",
    "sms": "SMS",
    "call": "Phone Call",
    "flash_call": "Phone Flash Call"
}
class TXT(object):
# /start message when other users start your bot
START_OTHER_USERS_TEXT = get_config(
    "START_OTHER_USERS_TEXT",
    (
        "Subscribe @Alvin_Image_Editor If You Support This Bot\n\n"
    )
)
INPUT_PHONE_NUMBER = get_config("INPUT_PHONE_NUMBER", (
    "☠️ Enter The Phone Number That You Want To Make Session."
))
RECVD_PHONE_NUMBER_DBP = get_config("RECVD_PHONE_NUMBER_DBP", (
    "☠️ Checking Received Phone Number \n\n"
    "☠️ The Process Takes a Long Time,\n"
    "☠️ Please Be Patient,\n\n"
    "<b>Never Submit Again</b> \n"
    "<b><i><u>It'll Ruin The System</u></i></b>"
))
ALREADY_REGISTERED_PHONE = get_config("ALREADY_REGISTERED_PHONE", (
    "☠️ This Number Is Registered On Telegram. "
    "Please Input The Verification Code That You Receive "
    "From <a href='tg://user?id=777000'>Telegram</a> "
    "Seperated By Space, \n\n <b>🤫 Example :</b> ✅ 1 7 0 2 9 - ❌ 17029\n\n"
    "Else A <b>PhoneCodeInvalidError</b> Would Be Raised."
))
CONFIRM_SENT_VIA = get_config("CONFIRM_SENT_VIA", (
    "✅ The Confirmation Code Has Been Sent Via {}"
))
RECVD_PHONE_CODE = get_config("RECVD_PHONE_CODE", (
    "☠️ Checking Received Phone Code \n\n"
    "☠️ The Process Takes a Long Time,\n"
    "☠️ Please Be Patient,\n\n"
    "<b>Never Submit Again</b> \n"
    "<b><i><u>It'll Ruin The System</u></i></b>"
))
NOT_REGISTERED_PHONE = get_config("NOT_REGISTERED_PHONE", (
    "❌ This Number Is Not Registered On Telegram. "
))
PHONE_CODE_IN_VALID_ERR_TEXT = get_config(
    "PHONE_CODE_IN_VALID_ERR_TEXT",
    "☠️ Invalid Code Received. Please Re /help"
)
TFA_CODE_IN_VALID_ERR_TEXT = get_config(
    "TFA_CODE_IN_VALID_ERR_TEXT",
    "Invalid Two Factor Code Received. Please Re /help"
)
ACC_PROK_WITH_TFA = get_config("ACC_PROK_WITH_TFA", (
    "The entered Telegram Number is protected with 2FA. "
    "Please enter your second factor authentication code.\n\n"
    "<i>This message will only be used for generating your "
    "string session, and will never be used for any other purposes "
    "than for which it is asked.</i>\n\n"
    "☠️ : @Alvin_Image_Editor"
))
SESSION_GENERATED_USING = get_config("SESSION_GENERATED_USING", (
    "👆 String Session Successfully Generated\n\n"
    "☠️ : @Alvin_Image_Editor \n☠️ Thank You For Using Me "
))
