import discord
from discord.ext import commands
from config import DISCORD_TOKEN, CHANNEL_ID

intents = discord.Intents.default()
intents.message_content = True

# Discord Bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('Bot is online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name='hello')
async def hello(ctx: commands.Context):
    await ctx.send('Hello!')
    
async def send_message(message):
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(message)
    else:
        print('Channel not found.')    

def run_bot():
    print('Running Discord Bot...')
    bot.run(DISCORD_TOKEN)
    
def close_bot():
    bot.close()
    print('Bot closed.')