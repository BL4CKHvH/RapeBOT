import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
    print('Bot is Online.')
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):

    guild = ctx.guild

    for role in guild.roles:
        if role.name =="Muted":
            await member.add_roles(role)
            await ctx.send("{} has been muted" .format(member.mention,ctx.author.mention))
            return

            overwrite = discord.PermissionOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole,overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} has been muted" .format(member.mention,ctx.author.mention))
    

    
@client.command()
@commands.has_permissions(ban_members=True)
async def kill(ctx, member : discord.Member, *, reason=None):
    await ctx.send(f'Banned {member.mention} for {reason}')
    await member.ban(reason=reason)

   

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@commands.has_permissions(manage_roles=True)
async def unmute(self, ctx, member: discord.Member):
    role = discord.utils.get(member.guild.roles, name="Muted")
    await member.remove_roles(role)

		

@client.command()
async def Revive(ctx, *, member):
    banned_users = await ctx.guild.unban()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f' Unbanned {user.mention}')
            return

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(kick_members=True)
async def rape(ctx, member : discord.Member, *, reason=None):
      await member.kick(reason=reason)
      await ctx.send(f'Raped {member.mention}')

@client.command(aliases=['porn'])
async def _porn(ctx):
    responses = ["(WIP)"]
    await ctx.send(f'{random.choice(responses)}')
@client.command(aliases=['cat'])
async def _cat(ctx):
    responses = ["https://imgur.com/gallery/VWjRf",
    "https://imgur.com/gallery/KWvtdg0",
    "https://imgur.com/gallery/9ay6J",
    "https://i.imgur.com/8PDnHK2.jpg",
    "https://i.imgur.com/lTYTyD8.jpg",
    "https://i.imgur.com/sTvv7k9.jpg",
    "https://i.imgur.com/viwpmPe.jpg",
    "https://i.imgur.com/ynDYXnJ.jpg",
    "https://i.imgur.com/l0stuyN.jpg",
    "https://i.imgur.com/hYJ64VY.jpg",
    "https://i.imgur.com/rnFDEuR.jpg",
    "https://i.imgur.com/HvHGZI1.jpg",
    "https://i.imgur.com/SqGWyWu.jpg",
    "https://i.imgur.com/U1vVDGk.jpg",
    "https://i.imgur.com/0iy3vvI.jpg",
    "https://i.imgur.com/eA42vyk.jpg"]
    await ctx.send(f'{random.choice(responses)}')
    


@client.command(aliases=['hentai'])

async def _hentai(ctx):
    responses = ["https://fi1.ypncdn.com/201904/07/15275869/original/5/hentai-group-sex-bondage-domination-part-1-5(m=eaAaaEPbaaaa).jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQs8FwByBVQrPEQxuKzCiyFQMY_m0_nWTpi7w&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRtXfd1bNjC33MQgtFgJUJad05L0MuzrSf-RQ&usqp=CAU",
                "https://static-ca-cdn.eporner.com/thumbs/static4/1/14/142/1427378/5_360.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRKOAZV7q1PAc-5LzIJk28p62hFpenWKP0q_g&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTjNERXFVV6avmsvSwqOmaI4H1VgOHawh-PcA&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQTXCRboZzp1zxVfmEfQlxcrX4o9evq57C53Q&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTkStnjfUDTzpVpHri7R_h5B4rZU2c--_U7Kg&usqp=CAU",
                "https://hentaibar.com/contents/videos_screenshots/0/497/preview.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRQP7zGuBvLUr-vYMxBoQy9_IVKMJZHiIHAOg&usqp=CAU"]
    
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['kitten'])
async def _kitten(ctx):
    responses = ["https://imgur.com/r/kittens/GFxHTHC",
                "https://imgur.com/r/kittens/B3zuvJL",
                "https://imgur.com/r/kittens/QWdjVFM",
                "https://imgur.com/r/kittens/fG2k8eC",
                "https://imgur.com/r/kittens/pQJftyj",
                "https://imgur.com/r/kittens/0Bxiciq",
                "https://imgur.com/r/kittens/QD1WDRi",
                "https://imgur.com/r/kittens/K9V1OR2",
                "https://imgur.com/r/kittens/JBZ2WRU",
                "https://imgur.com/r/kittens/PcRRpUd"]
    
    await ctx.send(f'{random.choice(responses)}')
@client.command(aliases=['darling'])
async def _infodarling(ctx):
    responses = ["https://en.wikipedia.org/wiki/Darling_in_the_Franxx"]
               
    
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['Youtube'])
async def _youtube(ctx):
    responses = ["https://en.wikipedia.org/wiki/YouTube"]
    await ctx.send(f'{random.choice(responses)}')

               
    


@client.command(aliases=['csgo'])
async def _csgo(ctx):
    responses = ["https://en.wikipedia.org/wiki/Counter-Strike:_Global_Offensive"]
               
    
    await ctx.send(f'{random.choice(responses)}')




     
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('NzI2NTA0ODg0NjMwODQ3NTE4.XveRdg.JoOV7h5lzGcSmKfkc-3tIgjNdKQ')
