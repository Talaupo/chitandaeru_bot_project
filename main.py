import discord
from discord.ext import commands, tasks
from itertools import cycle
from myserver import server_on

TOKEN = "MTEyNTA0NDY2NDg1NzI3MjMzMQ.GhxZNW.6pJL-OZyKZcrZ8TtHz2InjMqvQVZvCAGxYrdVE" # Replace with your bot token

bot = commands.Bot(command_prefix='ce!', intents=discord.Intents.all())
status_list = cycle([
    discord.Activity(type=discord.ActivityType.listening, name="your music"),
    discord.Activity(type=discord.ActivityType.watching, name="bit.ly/tflofficial"),
    discord.Activity(type=discord.ActivityType.playing, name="say eru")
])

aliases = ["kontol", "anjing", "ajg", "bajingan", "babi", "goblok", "tolol", "bodoh", "bebal", "memek", "ngentot"]

@bot.event
async def on_ready():
    change_status.start()
    print('Bot {} has come online'.format(bot.user))

@bot.event
async def on_message(message):
    if any(alias in message.content.lower() for alias in aliases):
        await message.channel.send(f"{message.author.mention}, mulutmu kotor!")
    elif "hallo" in message.content.lower():
        await message.channel.send('Hai {}! Aku Chitanda Eru, Ada yang bisa dibantu?'.format(message.author.mention))
    elif "eru" in message.content.lower():
        await message.channel.send('Manggil aku?')
    elif "talaupo" in message.content.lower():
        await message.channel.send('Kenapa kamu memanggil suamiku?')
    elif "penasaran" in message.content.lower():
        await message.channel.send('Kamu penasaran tentang apa?')
    
    await bot.process_commands(message)

@tasks.loop(seconds=5)
async def change_status():
    activity = next(status_list)
    if activity.name == "your music":
        activity = discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds[0].members)} Member")
    await bot.change_presence(activity=activity)

server_on()
bot.run(TOKEN)
