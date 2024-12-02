from Mitsuha.core.bot import Anony
from Mitsuha.core.dir import dirr
from Mitsuha.core.git import git
from Mitsuha.core.userbot import Userbot
from Mitsuha.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
