import discord
from discord.ext import commands

TOKEN = "put the bot's token here"
client = discord.Client()
playlists = {}
@client.event
async def on_message(message):
    author = message.author.name
    if message.author == client.user:
        return
    if message.content.startswith('!create'):
        play= (message.content).replace('!create ','')
        playlists.setdefault(author,[])
        playlists[author].append(play)
        await message.channel.send(f'Done! {author} uwu ')
     if message.content.startswith('!playlist'):
        for users in playlists:
            user = ""
            embed = discord.Embed(colour = discord.Colour.red())
            embed.set_author(name=f"{users}'s playlist")
            for playlist in playlists[users]:
                user = user+' \n '+playlist
            embed.add_field(name=f'{user}',value='',inline=False)
            await message.channel.send(embed=embed)
    if message.content.startswith('!clear'):
        play= (message.content).replace('!clear','')
        if len(play) > 0:
            try:
                playlists[author].remove(play)
            except Exception as e:
                print('[-]Failed to remove from play list',e)
            finally:
                await message.channel.send('If the song was in your playlist and you wrote it correct it got removed :)')
        else:
            try:
                del playlists[author]
            except Exception as e:
                print(f"[-]Failed to clear{author}'s playlist",e)
            finally:
                await message.channel.send('Your playlist should be cleared UwU')
    if message.content.startswith('!playme'):
        play= (message.content).replace('!playme','')
        if len(play) > 1:# just in case of sendin space
            for songs in playlists[play]:
                await message.channel.send(f'!play {songs}')
        else:
            for songs in playlists[author]:
                await message.channel.send(f'!play {songs}')
    if message.content.startswith('!playhelp'):
        embed = discord.Embed(
        colour = discord.Colour.green())
        embed.set_author(name='!playhelp : lsit of all the available commands')
        embed.add_field(name='!playme',value ='use it with username to play a user playlist or pass it empty to play yours',inline=False)
        embed.add_field(name='!clear',value ='you can pass a url or words to get it removed from your playlist or if nothing was passed with clear it will clear your whole playlist',inline=False)
        embed.add_field(name='!create',value ='you can pass words or a url to add stuff to your playlist',inline=False)
        embed.add_field(name='!playlist',value ='will return all the users playlist',inline=False)
        await message.channel.send(embed=embed)

@client.event
async def on_ready():
    print(f'logged in as:{client.user.name}:{client.user.id} \n-------------')
client.run(TOKEN)

