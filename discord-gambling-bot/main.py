# ToDo's
# - Set up discord bot
# - Add gambling mechanics to functions
# - Add gambling commands
# - Add Aron's special messages


# Imports

import discord
from discord.ext import commands

import random

from dotenv import load_dotenv
import os

# Token
load_dotenv()
token = os.getenv('TOKEN')

# Bot

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Events

@bot.event
async def on_ready():
    print("Gambling Bot is ready!")

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return
    
    from functions.play import play as Gamble
    from functions.balance import balance as checkBalance
    from functions.reset import reset as resetCoins

    motivation = ["90% of Gambling Addicts Quit Right Before They're About to Hit It Big", "You can win 1000% of your money but only lose 100%.", "Now is a good moment! Go all in!", "You can't win if you don't play!"]

    id = message.author.id
    
    gamblers = [609371127566827521, 949009367070560276]

    if message.channel.id == 1108789026992959610:
        if id in gamblers:
            if random.random() < 0.3:
                await message.reply(random.choice(motivation))
        if random.random() < 0.3:
            await message.reply("You should be gambling right now!")

    await bot.process_commands(message)
    

@bot.command()
async def play(ctx, bet=None):
    if bet is None:
        embed = discord.Embed(title="Gambling", description="You need to specify a bet!", color=0xff0000)
        await ctx.message.reply("You need to specify a bet!")
        return
    from functions.play import play as Gamble
    status = Gamble(ctx.author.id, int(bet))
    embed = discord.Embed(title="Gambling", description=status, color=0x04ff00)
    await ctx.message.reply(embed=embed)

@bot.command()
async def balance(ctx):
    from functions.balance import balance as checkBalance
    balance = checkBalance(ctx.author.id)
    embed = discord.Embed(title="Gambling", description=balance, color=0x04ff00)
    await ctx.message.reply(embed=embed)

@bot.command()
async def reset(ctx):
    from functions.reset import reset as resetCoins
    status = resetCoins(ctx.author.id)
    embed = discord.Embed(title="Gambling", description=status, color=0x04ff00)
    await ctx.message.reply(embed=embed)

@bot.command()
async def motivation(ctx):
    motivation = ["90% of Gambling Addicts Quit Right Before They're About to Hit It Big", "You can win 1000% of your money but only lose 100%.", "Now is a good moment! Go all in!", "You can't win if you don't play!"]
    embed = discord.Embed(title="Motivation", description=random.choice(motivation), color=0x04ff00)
    await ctx.message.reply(embed=embed)

# Run bot

bot.run(token)