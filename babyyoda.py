import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    onedirection_quotes = [
        (
            'Why did the mushroom go to the party? '
            'Because hes a fungi!' ),
        'And id marry you harry because it rhymes',
        'psychiatry isnt a word, you made that one up',
        'HOLEH MOLEH',
        'WHAT DID YOU BRING LIAM? NO HAI!',
        'Bye Donuts',
        ]
    if message.content == '!1d':
        response = random.choice(onedirection_quotes)
        await message.channel.send(response)


    babyyoda_gifs = [
        'https://media1.tenor.com/images/a80b0bb71ac88114d5d6c704ccb9df94/tenor.gif?itemid=16072547',
        'https://media.giphy.com/media/Lk0DMQSpLypMDBkbe7/giphy.gif',
        'https://filmdaily.co/wp-content/uploads/2020/11/babyyoda-02.gif',
        'https://i.imgur.com/NlEy4cg.gif',
        'https://media1.tenor.com/images/0bd53bc439762d0ac07975721780117d/tenor.gif?itemid=19101147',
        'https://pyxis.nymag.com/v1/imgs/e2d/2b8/9bc93b0e62b2d8be5105cfd99e2f5afed3-baby-yoda-no-eating-eggs.2x.w710.gif',
        ]
    if message.content == 'baby yoda':
        response = random.choice(babyyoda_gifs)
        await message.channel.send(response)


client.run('Nzk3NTAxNzgxNTYzMTQ2Mjcy.X_nZaQ.vUe3wMa4iKnZcaKmFW_qU0BdwGo')
