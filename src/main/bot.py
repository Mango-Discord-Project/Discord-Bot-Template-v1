import os

from dotenv import load_dotenv
from discord.ext.commands import (
    Bot as _bot
)

from .package import files

load_dotenv()
__TOKEN = os.environ.get("TOKEN")
__all__ = ["Bot", "bot"]
__SETTING_PATH = "./setting.json"

class Bot(_bot):
    def __init__(self):
        setting_obj = files.JSON(__SETTING_PATH)
        self.setting = setting_obj.load()
        super().__init__(command_prefix=self.setting[''])
    
    
bot = Bot()
bot.run(__TOKEN)