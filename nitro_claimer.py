from discord.ext import commands
import discord
import re, requests
from colorama import Fore, init
init()


### hunchos ###
token = input("Token: ") ### Możesz też to zastąpić poprostu tokenem jak nie chcesz za każdym razem wpisywać
while 1:
    try:
        bot = commands.Bot(command_prefix=".", self_bot=True)
 
        @bot.event
        async def on_ready():
            print("[+] bot gotowy")
 
        @bot.event
        async def on_message(ctx):
            if 'discord.gift' in ctx.content:
                code = re.search("discord.gift/(.*)", ctx.content).group(1)
                if len(code) != 16:
                    print("[=] Fejkowy kod : "+code)
                else:
                    print(Fore.LIGHTGREEN_EX+"[-] Zajebano kod : "+code+" z "+ctx.author.name+"#"+ctx.author.discriminator)
                    r = requests
                    result = r.post('https://discordapp.com/api/v6/entitlements/gift-codes/'+code+'/redeem', json={"channel_id":str(ctx.channel.id)}, headers={'authorization':token}).text
                    if 'This gift has been redeemed already.' in result:
                        print(Fore.YELLOW+"[-] Ktoś już go wziął : "+code+Fore.RESET)
                    elif 'nitro' in result:
                        print(Fore.GREEN+"[+] Kod poprawny : "+code+Fore.RESET)
                    elif 'Unknown Gift Code' in result:
                        print(Fore.RED+"[-] Zły kodzik : "+code+Fore.RESET)
 
        bot.run(token, bot=False)
    except KeyError:
        pass
