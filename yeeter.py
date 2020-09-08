



# bot.py
import os
import discord

TOKEN = "NzUyNjcyNzY1OTk1MTIyNzk4.X1bDIw.DTorjXzS8XP5WeQH5HMobmgcOh0"
GUILD = "bot_testing"



client = discord.Client()

@client.event
async def on_message(message):
    if 'epic' in message.content.lower():
        await message.channel.send('And the Lord spake, saying, First shalt thou take out the Holy Pin. Then shalt thou count to three, no more, no less. Three shall be the number thou shalt count, and the number of the counting shall be three. Four shalt thou not count, neither count thou two, excepting that thou then proceed to three. Five is right out. Once the number three, being the third number, be reached, then lobbest thou thy Holy Hand Grenade of Antioch towards thy foe, who, being naughty in My sight, shall snuff it.')
    if 'unexpected' in message.content.lower():
        await message.channel.send('And now for something completely different.')
    if 'england' in message.content.lower():
        await message.channel.send('You don’t frighten us, English pig dogs. Go and boil your bottoms, you sons of a silly person. I blow my nose at you, so-called ‘Arthur King,’ you and all your silly English K-nig-hts.')
    if 'establishment' in message.content.lower():
        await message.channel.send('Strange women lying in ponds, distributing swords, is no basis for a system of government!')
    if 'vegan' in message.content.lower():
        await message.channel.send('We serve no meat of any kind. We’re not only proud of that, we’re smug about it.')






client.run(TOKEN)
