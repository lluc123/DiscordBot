import discord
import youtube_dl
import asyncio
import os
class Voice_Player:

    def __init__(self, msg):
        self.channel = msg.channel
        self.author = msg.author
        self.content = msg.content
        self.msg = msg
	self.vc = None

    async def join_voice(self):
        try:
            author = self.author
            self.vc = await discord.VoiceChannel.connect(author.voice.channel)
        except Exception as e:
            print(e)

    async def join_leave(self):
        author = self.author
        self.vc = await discord.VoiceChannel.connect(author.voice.channel)
        asyncio.run_coroutine_threadsafe(self.vc.disconnect(), self.vc.loop)

    def voice_disconnect(self):
	if self.vc is not None:
            asyncio.run_coroutine_threadsafe(self.vc.disconnect(), self.vc.loop)
        #await self.vc.disconnect()

    async def file_play(self, file):
	if self.vc is not None:
            vc = self.vc
            vc.play(discord.FFmpegPCMAudio(file))

    async def url_play(self, url):
	if self.vc is None:
            return
        try:
            os.remove('yt.m4a')
            vc = self.vc
            ydl_opts = {
                'outtmpl': 'yt.m4a',
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                vc.play(discord.FFmpegPCMAudio('yt.m4a'),after=lambda e: self.voice_disconnect())
        except Exception as e:
            print(e)
            self.voice_disconnect()
