# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
from os import environ, getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class Config(object):
    # Bot Information 
    TECH_VJ_BOT_TOKEN = os.environ.get("TECH_VJ_BOT_TOKEN", "7423930218:AAFlSE73_9wjbB2wLdFfOC399XCUwdr9Csw")
    TECH_VJ_BOT_USERNAME = os.environ.get("TECH_VJ_BOT_USERNAME", "nightfilesbot_bot") # Bot username without @.
    
    # The Telegram API things
    TECH_VJ_API_ID = int(os.environ.get("TECH_VJ_API_ID", "28573516"))
    TECH_VJ_API_HASH = os.environ.get("TECH_VJ_API_HASH", "60bd65955d8b9c63943688f7d3972958")
    
    # the download location, where the HTTP Server runs
    TECH_VJ_DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Telegram maximum file upload size
    TECH_VJ_MAX_FILE_SIZE = 50000000
    TECH_VJ_TG_MAX_FILE_SIZE = 4194304000 #2097152000
    TECH_VJ_FREE_USER_MAX_FILE_SIZE = 50000000
    
    # chunk size that should be used with requests
    TECH_VJ_CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    TECH_VJ_HTTP_PROXY = ""
    
    # maximum message length in Telegram
    TECH_VJ_MAX_MESSAGE_LENGTH = 4096
    
    # set timeout for subprocess
    TECH_VJ_PROCESS_MAX_TIMEOUT = 3600
    
    # your telegram account id
    TECH_VJ_OWNER_ID = int(os.environ.get("TECH_VJ_OWNER_ID", "5628866621")) 
    TECH_VJ_SESSION_NAME = "VJ-URL-UPLOADER-BOT"
    
    # database uri (mongodb)
    TECH_VJ_DATABASE_URL = os.environ.get("TECH_VJ_DATABASE_URL", "mongodb+srv://sandeepsah86405:Fl1hEVo8oMeztCQp@cluster0.tsmqg0t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    TECH_VJ_MAX_RESULTS = "50"

    # channel information
    TECH_VJ_LOG_CHANNEL = int(os.environ.get("TECH_VJ_LOG_CHANNEL", "5628866621")) # your log channel id and make bot admin in log channel with full right 
    
    # if you want force subscribe then give your channel id below else leave blank
    tech_vj_update_channel = environ.get('TECH_VJ_UPDATES_CHANNEL', '') # your update channel id and make bot admin in update channel with full right
    TECH_VJ_UPDATES_CHANNEL = int(tech_vj_update_channel) if tech_vj_update_channel and id_pattern.search(tech_vj_update_channel) else None  
    
    # Url Shortner Information 
    TECH_VJ = bool(environ.get('TECH_VJ', True)) # Set False If you want shortlink off else True
    TECH_VJ_URL = environ.get('TECH_VJ_URL', 'modijiurl.com') # your shortlink url domain or url without https://
    TECH_VJ_API = environ.get('TECH_VJ_API', 'afd663d79c4436a8ba24996834697a3af5f3fb85') # your url shortner api
    TECH_VJ_TUTORIAL = os.environ.get("TECH_VJ_TUTORIAL", "https://web.telegram.org/k/#@howtobottyfiles_bot")

Use this token to access the HTTP API:
6656250991:AAFr6foCSLxINjuCZiKHaKfCCUStvjDJ_Kw
Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api")


# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
