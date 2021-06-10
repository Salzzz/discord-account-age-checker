import discord
from datetime import datetime, timedelta
from discord.ext import commands

intents = discord.Intents(members=True)
bot = commands.Bot(command_prefix='#', intents=intents)

token = "YOUR_BOT_TOKEN" #  Make sure that you enable the "Server members intent" on your bot page.


@bot.event
async def on_member_join(member):
    days = 14 #  Change this number if you want to change the number of days the account has to be old in order to access the server.
    print(str(member) + " has joined, checking for account age now!")
    print("Account created at: " + str(member.created_at))
    d1 = datetime.today() - timedelta(days=days)
    d2 = member.created_at
    if d2 < d1:
        print("Account is older than " + str(days) + " days! Passed.")
    elif d2 > d1:
        print("Account is younger than " + str(days) + " days! User will be kicked.")
        await member.create_dm()
        await member.dm_channel.send(
            "You have been kicked from the server! Reason: Account age is below " + str(days) + " days.") #  Change this to your server name-
        await member.kick()
    else:
        print("Something went.. wrong")


bot.run(token)
