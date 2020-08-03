import os

import discord
from dotenv import load_dotenv

TOKEN = "NzM5NjgyMzU5MTQxNzI4MzQ3.XyeA4Q.Rgnj-WMO-G86fIlgm8qpgNW9T8Y"
GUILD = "Festival de Frios de Garanhuns"

client = discord.Client()

@client.event
async def on_ready():
	guild = discord.utils.get(client.guilds, name=GUILD)
	print(f"{guild.name}(id: {guild.id}")

@client.event
async def on_message(message):
	if "miguel" in message.author.name:
		await message.channel.send("NENEKATCHANNNNNNNN")
	if "yeso" in message.author.name:
		await message.channel.send("NAMISWANNNNNNNNNNNNNN")
	if "ozzy" in message.author.name:
		await message.channel.send("oi ozzy me desculpe :c")

client.run(TOKEN)
