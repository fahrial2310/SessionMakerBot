from pyrogram import (
    Client,
    __version__
)
from bot import (
    API_HASH,
    APP_ID,
    LOGGER,
    TG_BOT_WORKERS
)


class User(Client):
    """ modded client for SessionMakerUser """

    def __init__(self):
        super().__init__(
            ":memory:",
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=TG_BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} based on Pyrogram v{__version__} "
        )
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
