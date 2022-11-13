#Author = "LAUBERGINE"

import discord
from dotenv import load_dotenv
import os
from random import*
from discord.ext import commands
from time import*
from word import* 

load_dotenv()

client = commands.Bot(command_prefix = "!", description = "EggplantBot by LAUBERGINE")
client.remove_command('help')

@client.event
async def on_ready():
    print("Kirua la legende")
    await client.change_presence(activity=discord.Game("laubergine.repl.co | !help"))

@client.command()
async def fr(ctx, ch):
    f = int(ch) 
    mot = wordf(f)
    rep = wordes(f)
    await ctx.send(f"Comment dit-on **{mot}** en espagnol ?")
    
    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    reponse = await client.wait_for("message", check = check)

    if (reponse.content.lower() == rep):        
        await ctx.channel.send("Bravo !")

    elif (reponse.content.lower() != rep):
        await ctx.channel.send(f"Dommage c'était **{rep}**")

@client.command()
async def es(ctx, ch):
    f = int(ch) 
    rep = wordf(f)
    mot = wordes(f)
    await ctx.send(f"Comment dit-on **{mot}** en français ?")
    
    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    reponse = await client.wait_for("message", check = check)

    if (reponse.content.lower() == rep):        
        await ctx.channel.send("Bravo !")

    elif (reponse.content.lower() != rep):
        await ctx.channel.send(f"Dommage c'était **{rep}**")

@client.command()
async def ifr(ctx):
    f = randint(1,62) 
    mot = wordf(f)
    rep = wordes(f)
    await ctx.send(f"Comment dit-on **{mot}** en espagnol ?")
    
    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    reponse = await client.wait_for("message", check = check)

    if (reponse.content.lower() == rep):        
        await ctx.channel.send("Bravo !")

    elif (reponse.content.lower() != rep):
        await ctx.channel.send(f"Dommage c'était **{rep}**")

@client.command()
async def ies(ctx):
    f = randint(1,62) 
    rep = wordf(f)
    mot = wordes(f)
    await ctx.send(f"Comment dit-on **{mot}** en français ?")
    
    def check(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    reponse = await client.wait_for("message", check = check)

    if (reponse.content.lower() == rep):        
        await ctx.channel.send("Bravo !")

    elif (reponse.content.lower() != rep):
        await ctx.channel.send(f"Dommage c'était **{rep}**")

@client.command()
async def tfr(ctx, ch):
    p = 0
    nb = int(ch)
    while nb != 0:
        f = randint(1,62) 
        mot = wordf(f)
        rep = wordes(f)
        await ctx.send(f"Comment dit-on **{mot}** en espagnol ?")
        
        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse = await client.wait_for("message", check = check)

        if (reponse.content.lower() == rep):        
            await ctx.channel.send("Bravo !")
            nb = nb - 1
            p = p + 1
            if nb == 0:
                await ctx.channel.send(f"Tu a eu **{p}/{ch}**")

        elif (reponse.content.lower() != rep):
            await ctx.channel.send(f"Dommage c'était **{rep}**")
            nb = nb -1
            if nb == 0:
                await ctx.channel.send(f"Tu a eu **{p}/{ch}**") 

@client.command()
async def tes(ctx, ch):
    p = 0
    nb = int(ch)
    while nb !=0:
        f = randint(1,62) 
        rep = wordf(f)
        mot = wordes(f)
        await ctx.send(f"Comment dit-on **{mot}** en français ?")
        
        def check(message):
            return message.author == ctx.message.author and ctx.message.channel == message.channel

        reponse = await client.wait_for("message", check = check)

        if (reponse.content.lower() == rep):        
            await ctx.channel.send("Bravo !")
            nb = nb - 1
            p = p + 1
            if nb == 0:
                await ctx.channel.send(f"Tu a eu **{p}/{ch}**")

        elif (reponse.content.lower() != rep):
            await ctx.channel.send(f"Dommage c'était **{rep}**")
            nb = nb - 1
            if nb == 0:
                await ctx.channel.send(f"Tu a eu **{p}/{ch}**") 

@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Colour.purple(), title='Liste des commandes')
    embed.add_field(name="**!fr [numéro]**", value="Donne un mot en **français** à traduire en **espagnol**", inline=False)
    embed.add_field(name="**!es [numéro]**", value="Donne un mot en **espagnol** à traduire en **français**", inline=False)
    embed.add_field(name="**!ifr**", value="Donne un mot en **français** à traduire en **espagnol**", inline=False)
    embed.add_field(name="**!ies**", value="Donne un mot en **espagnol** à traduire en **français**", inline=False)
    embed.add_field(name="**!tfr [numéro]**", value="Te test sur le nombre de mot que tu veux et te donne une note a la fin du test **français** vers **espagnol**", inline=False)
    embed.add_field(name="**!tes [numéro]**", value="Te test sur le nombre de mot que tu veux et te donne une note a la fin du test **espagnol** vers **français**", inline=False)
    await ctx.send(embed=embed)

client.run(os.getenv("TOKEN"))