import discord
from discord.ext import commands

TOKEN = "put the bot's token here"
help_msg = ("""!create url/words, you can pass words or url to add to your playlist
 \n!clear url/words, you can pass a url or words to remove it from your playlist or if nothing was passed with clear it will clear your whole playlist
 \n!playme user, use it to play a user playlist or pass it alone to play yours
  \n!playlist will send all users songs one by one and it may take time!""")
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
            await message.channel.send(f"{users}'s playlist:")
            for playlist in playlists[users]:
                user = user+' \n '+playlist
            await message.channel.send(f'{user}')
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
        await message.channel.send(help_msg)


@client.event
async def on_ready():
    print(f'logged in as:{client.user.name}:{client.user.id} \n-------------')
client.run(TOKEN)

