import os
from text import *
from embed import *

TOKEN = os.environ.get('TOKEN', None)

bot.run(TOKEN)
