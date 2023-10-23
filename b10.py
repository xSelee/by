import discord
import discum
import asyncio
import os
from discum.utils.button import Buttoner
from discord.ext import commands
from keep_alive import keep_alive
from random import choice


token = os.environ["token10"]
channelid = os.environ["id10"]  # replace with channel where bot should send commands
dmid = os.environ[
    "id10"
]  # open a dm channel through the self bot and copy the id of that channel, it should be in the url bar of browser discord.com/@me/dmid, or you can copy it like a normal channel id on phone
bot = commands.Bot(
    command_prefix="s",
    guild_subscription_options=discord.GuildSubscriptionOptions.off(),
    self_bot=True,
)
client = discum.Client(token=token)
bot._skip_check = lambda x, y: False


async def btall():
    while True:
        client.sendMessage(str(channelid), ".give xLoki 10000")  # Command: .bt or .bt all
        await asyncio.sleep(2040)  # interval between each command in seconds


async def ho():
    while True:
        client.sendMessage(str(channelid), ".bt max")  # Command: .bt or .bt all
        await asyncio.sleep(choice([3040])) 

async def cricdrop():
    while True:
        client.sendMessage(str(channelid), ".hourly")  # Command: .bt or .bt all
        await asyncio.sleep(choice([3600]))

async def lo():
    while True:
        client.sendMessage(str(channelid), ".lottery")  # Command: .bt or .bt all
        await asyncio.sleep(choice([680,720,750,780,700,770,850,940,1080])) 


@bot.event
async def on_ready():
    print("Ready!")
    bt_all = asyncio.create_task(btall())
    h_o = asyncio.create_task(ho())
    cric_drop = asyncio.create_task(cricdrop())
    #l_o = asyncio.create_task(lo())
    # rd_bt = asyncio.create_task(rdbt())
    # rd_spawn = asyncio.create_task(rdspawn())

@bot.command()
async def say(ctx, *, content):
    await ctx.send(content)
  

@bot.command()
async def spawn(ctx):
    await ctx.send(".rd spawn i")

@bot.command()
async def j(ctx, arg):
    await ctx.send(f".rd join {arg}")

@bot.command()
async def say_siesta(ctx, arg):
    await ctx.send(f"{arg}")
  
@bot.command()
async def raidleave(ctx):
    await ctx.send(".rd leave")

@bot.command()
async def s(ctx):
    await ctx.send(".rd start")

@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
    if msg.embeds:
        if "Challenging Area" in str(msg.embeds[0].title):
            channelID = str(msg.channel.id)
            messageID = str(msg.id)
            guildId = str(msg.guild.id)
            message = client.getMessage(channelID, messageID)
            data = message.json()[0]
            buts = Buttoner(data["components"])
            client.click(
                data["author"]["id"],
                channelID=data["channel_id"],
                guildID=guildId,
                messageID=data["id"],
                messageFlags=data["flags"],
                data=buts.getButton(emojiName="✅"),
            )
        if "to take on this Raid Boss!" in str(msg.embeds[0].footer.text):
            title = msg.embeds[0].title
            description = msg.embeds[0].description
            footer = msg.embeds[0].footer.text
            image = msg.embeds[0].image.url
            message = f"""```{title}```
```{description}```
```{footer}```
{image}"""
            client.sendMessage(str(dmid), message)
          
        if "Raid Boss Battle" in str(msg.embeds[0].title):
            channelID = str(msg.channel.id)
            messageID = str(msg.id)
            guildId = str(msg.guild.id)
            message = client.getMessage(channelID, messageID)
            data = message.json()[0]
            buts = Buttoner(data["components"])
            client.click(
                data["author"]["id"],
                channelID=data["channel_id"],
                guildID=guildId,
                messageID=data["id"],
                messageFlags=data["flags"],
                data=buts.getButton(emojiName="✅"),
            )
          
        if '''Confirmation''' in str(msg.embeds[0].title):
            channelID = str(msg.channel.id)
            messageID = str(msg.id)
            guildId = str(msg.guild.id)
            message = client.getMessage(channelID, messageID)
            data = message.json()[0]
            buts = Buttoner(data["components"])
            client.click(
                data["author"]["id"],
                channelID=data["channel_id"],
                guildID=guildId,
                messageID=data["id"],
                messageFlags=data["flags"],
                data=buts.getButton(emojiName="✅"),
            )

keep_alive()
bot.run(token, reconnect=True)
