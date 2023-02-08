import discord
import os
import requests
import json
import random
from keep_alive import keep_alive
from discord.ext import commands
import image

# client = discord.Client(intents=discord.Intents.default())
client = commands.Bot(command_prefix=')')

bye_statements = ["bye", "Bye", "cya", "Cya"]

hello_statements = ["hello", "Hello", "wsp", "sup", 'Hi', "Sup"]

sad_words = [
    "sad", "depressed", "unhappy", "angry", "miserable", "depressing",
    "depression"
]

starter_encouragements = [
    "It's ok man relax and just watch some hent** lol im joking",
    "Cheer up man!!", "Time will pass dont worry", "Never give up",
    "Go and watch some anime that will cheer you up :)",
    "Haha keep crying like a girl"
]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("joke"):
        joke = image.get_joke()
        await message.channel.send(joke)

    if any(word in message.content for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

    if any(word in message.content for word in (hello_statements)):
        await message.channel.send('Hey there,I hope you are doing well :)')

    if message.content.startswith("hi"):
        await message.channel.send("Hey there,I hope you are doing well :)")

    if message.content.startswith("!list"):
        await message.channel.send(starter_encouragements)

    if message.content.startswith('sus'):
        await message.channel.send('sussy baka')

    if any(word in message.content for word in bye_statements):
        await message.channel.send("Bye, see you later!")

    if message.content.startswith("lol"):
        await message.channel.send("lol")

    if message.content.startswith("stfu"):
        await message.channel.send("no")
    if message.content.startswith("dog"):
        get_dog = image.dog()
        await message.channel.send(get_dog)

    if message.content.startswith("wyr"):
        get_wyr = image.wyr()
        await message.channel.send(get_wyr)

    if message.content.startswith("truth"):
        get_truth = image.Truth()
        await message.channel.send(get_truth)

    if message.content.startswith("cat"):
        get_cat = image.Cat()
        await message.channel.send(get_cat)
        
    if message.content.startswith("avatar"):
        get_avatar = avatar()
        await message.channel.send(get_avatar)



keep_alive()
client.run(os.environ['token'])
