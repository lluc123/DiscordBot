from Commands.commands import Commands
from utils import Utils
from Voice_utils import Voice_Player
from ctypes.util import find_library
import discord
from discord import opus


client = discord.Client()
lib = find_library('opus')
opus.load_opus


class play(Commands):
    async def action(self, msg, args):
        output = ''
        for word in args:
            output += word + ' '
        url = 'https://www.youtube.com/watch?v=SpbJ9xyoa18' #Utils.q_google('youtube.com:'+output)
        vp = Voice_Player(msg)
        await vp.join_voice()
        await vp.get_vc()
        await vp.url_play(url)
        await msg.channel.send('Now playing: '+url)

