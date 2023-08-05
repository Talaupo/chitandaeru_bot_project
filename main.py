import discord
from discord.ext import commands
from myserver import server_on
import random
import requests

TOKEN = "TOKEN"  # Replace with your bot token

bot = commands.Bot(command_prefix='c!', intents=discord.Intents.all())

aliases = ["kontol", "anjing", "ajg", "bajingan", "babi", "goblok", "tolol", "bodoh", "bebal", "memek", "ngentot"]

@bot.event
async def on_ready():
    activity = discord.Streaming(name="Earthians", url="https://www.youtube.com/watch?v=rUxyKA_-grg")
    await bot.change_presence(activity=activity)
    print('Bot {} has come online'.format(bot.user))

@bot.event
async def on_member_join(member):
    welcome_channel_id = 1131765376326312007  # Replace with the actual channel ID
    welcome_channel = bot.get_channel(welcome_channel_id)
    await welcome_channel.send(f"Selamat datang di Earthians, {member.mention}!")

@bot.event
async def on_member_boost(member):
    thank_you_channel_id = 1132151459065106492  # Replace with the actual channel ID
    thank_you_channel = bot.get_channel(thank_you_channel_id)
    await thank_you_channel.send(f"Terima kasih atas boost server, {member.mention}!")

@bot.event
async def on_message(message):
    if message.author.bot:  # Ignore messages from other bots
        return

    content = message.content.lower()

    if any(alias in content for alias in aliases):
        await message.channel.send(f"{message.author.mention}, sekarang nakal ya?")
    elif "halo" in content:
        await message.channel.send('Hai {}!, ada yang bisa dibantu?'.format(message.author.mention))
    elif "chitanda eru" in content:
        await message.channel.send('Manggil aku?')
    elif "iya" in content:
        await message.channel.send('Iyain aja')
    elif "pagi" in content:
        await message.channel.send('Pagi juga, {}!'.format(message.author.mention))
    elif "siang" in content:
        await message.channel.send('Siang juga, {}!'.format(message.author.mention))
    elif "sore" in content:
        await message.channel.send('Sore juga, {}!'.format(message.author.mention))
    elif "malam" in content:
        await message.channel.send('Malam juga, {}!'.format(message.author.mention))

    await bot.process_commands(message)

@bot.command()
async def rps(ctx, choice):
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)

    if choice not in choices:
        await ctx.send("Please choose either 'rock', 'paper', or 'scissors'.")
        return

    if choice == bot_choice:
        result = "It's a tie!"
    elif (choice == 'rock' and bot_choice == 'scissors') or (choice == 'paper' and bot_choice == 'rock') or (choice == 'scissors' and bot_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    await ctx.send(f"You chose **{choice}**. I chose **{bot_choice}**. {result}")

@bot.command()
async def rolldice(ctx):
    dice_result = random.randint(1, 6)
    await ctx.send(f"You rolled a dice and got **{dice_result}**!")

@bot.command()
async def randomfact(ctx):
    response = requests.get("https://useless-facts.sameerkumar.website/api")
    if response.status_code == 200:
        fact_data = response.json()
        fact = fact_data['data']
        await ctx.send(f"🧠 **Random Fact:** {fact}")
    else:
        await ctx.send("Sorry, I couldn't fetch a random fact at the moment.")

@bot.command()
async def quote(ctx):
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get("content")
        author = quote_data.get("author", "Unknown")
        await ctx.send(f"💡 **Quote of the Day**:\n\n{content}\n\n- {author}")
    else:
        await ctx.send("Sorry, I couldn't fetch a quote at the moment.")

@bot.command()
async def catfact(ctx):
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200:
        fact_data = response.json()
        fact = fact_data['fact']
        await ctx.send(f"🐱 **Cat Fact:** {fact}")
    else:
        await ctx.send("Sorry, I couldn't fetch a cat fact at the moment.")

server_on()
bot.run(TOKEN)
