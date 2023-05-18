import discord
from discord.ext import commands
import random
import requests

INTENTS = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=INTENTS)

@bot.command()
async def dc(ctx):
    is_valid = False
    while not is_valid:
        gift_code = generate_gift_code()
        is_valid = validate_gift_code(gift_code)

    await ctx.author.send(f'https://discord.gift/{gift_code}')

def generate_gift_code():
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy0123456789', k=16))

def validate_gift_code(code):
    url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}"
    proxy_list = [
        'http://176.113.73.104:3128/', # This is how this list of proxies should look like, paste a lot of your proxies so that they don't crash constantly due to limited rate
        'http://176.113.73.99:3128/',
        'http://167.172.109.12:39533/'
    ]
    headers = {"Authorization": "YOUR_BOT_TOKEN"}  # replace YOUR_BOT_TOKEN with your bot's token

    for proxy in proxy_list:
        try:
            response = requests.get(
                f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}",
                headers=headers,
                proxies={'http': proxy, 'https': proxy}
            )
            if response.status_code == 200:
                return True
        except requests.exceptions.RequestException:

            pass

    return False

bot.run('YOUR_BOT_TOKEN') # replace YOUR_BOT_TOKEN with your bot's token