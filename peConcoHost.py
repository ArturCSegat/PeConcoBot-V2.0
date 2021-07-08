from operator import truediv
import discord
from discord import client
from discord import message
from discord.enums import AuditLogAction, RelationshipType
from discord.ext import commands
import random
import top
import time
import membro_OOP


intents = discord.Intents.all()
intents.presences = True
intents.messages = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_member_join(member: discord.Member):

    guild = bot.get_guild(581158091115200535)

# roles
    pleb = guild.get_role(818486529314783263)
    c_master = guild.get_role(832611250348228628)
    chadCargo = guild.get_role(818487902606327878)
    baiano_cargo = guild.get_role(849469082566262839)
    botRole = guild.get_role(818487365956796456)
    cringeNaoAdm = guild.get_role(826785809474125872)
    atlantida = guild.get_role(819565407282266112)
    macho_g = guild.get_role(847287306858528828)
    grand_rob = guild.get_role(854518898220990466)
    s_tereza = guild.get_role(859066768601645066)
    f_tereza = guild.get_role(856282555703492638)
    omega = guild.get_role(862704974429159455)
    indio = guild.get_role(862672037835178004)
    redk = guild.get_role(860139656796700682)
    pimonte = guild.get_role(862067103061377034)
    f = guild.get_role(862333483732566066)
    

# members
    vruh2 = membro_OOP.Membruh("kfh", 146956554371989504, c_master)
    omni = membro_OOP.Membruh("omni", 225051659221467137, omega)
    chad = membro_OOP.Membruh("faxina", 584776317321609238, chadCargo)
    ernestoChe = membro_OOP.Membruh("ernesto", 691069156400824372, indio)
    baiano = membro_OOP.Membruh("breno", 441986625283686413, baiano_cargo)
    tocomdor = membro_OOP.Membruh("dudz", 358985083329314816, redk)
    pontos = membro_OOP.Membruh("...", 578714642843435019, macho_g)
    drealocks = membro_OOP.Membruh("Drealocks", 354303193372557313, pimonte)
    epiclord = membro_OOP.Membruh("Epic", 423503073479098368, omega)
    MC_lendrinho = membro_OOP.Membruh("loldrinho", 423596836578918444, f)



    members = [vruh2, omni, chad, ernestoChe, baiano, tocomdor, pontos, drealocks, epiclord, MC_lendrinho]

    members_hash = {m.ident: m for m in members}

    if member.id in members_hash:
        await member.add_roles(members_hash[member.id].cargo, reason=None, atomic=True)

    else:
        await member.add_roles(pleb, reason=None, atomic=True)
    

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    await bot.process_commands(message)


#only commands from here

# this section is exclusivly for debugging and testing purposes

@bot.command(pass_context =True)
async def test(ctx, user: discord.User):
    if user.top_role.name == "Plebeus":
        await ctx.send("ok")

@bot.command(pass_context = True)
async def test2(ctx, user: discord.User):
    await ctx.send(ctx.message.author.top_role)
    await ctx.send(user.top_role)

@bot.command(pass_context =True)
async def test3(ctx):
    await ctx.send("ok")

@bot.command(pass_context =True)
async def test4(ctx):
    await ctx.send("a")

# message managing commands
@bot.command(pass_context = True)
async def clear(ctx, number: int):
    if number < 51:
        await ctx.message.channel.purge(limit=number + 1)
        await ctx.send(f"{number} mensagens deletadas por {ctx.message.author.name}" )
        print("clear command used")


# this section is for user managing commands
@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member, is_in_code = 0):
    commander = ctx.message.author

    r_dict = top.role_lvl

    if r_dict[commander.top_role.id] > r_dict[user.top_role.id]:
        
        await user.kick()
        await ctx.send(f"{user.mention} foi kickado")
        u = await bot.fetch_user(user.id)

        invite_channel = await u.create_dm()

        await invite_channel.send("discord.gg/epk8bFT")
    else:
        await ctx.send("Este usuario tem um cargo melhor que o seu ou o seu cargo não existe")

@bot.command(pass_context = True)
async def ban(ctx, user: discord.Member):
    commander = ctx.message.author

    r_dict = top.role_lvl

    if r_dict[commander.top_role.id] > r_dict[user.top_role.id]:
        await ctx.send(f"{user.mention} foi banido")
        await user.ban()
    else:
            await ctx.send("Este usuario tem um cargo melhor que o seu ou o seu cargo não existe")




@bot.command(pass_context = True)
async def superultramegaban(ctx, user :discord.Member):
    commander = ctx.message.author
    #simple test
    r_dict = top.role_lvl

    if r_dict[commander.top_role.id] > r_dict[user.top_role.id]:
        await user.ban()
        await ctx.send(f"{user.mention} foi super ultra mega banido")
    else:
            await ctx.send("Este usuario tem um cargo melhor que o seu ou o seu cargo não existe")

@bot.command(pass_context = True)
async def unban(ctx, user: discord.User):
    uid = user.id
    u = await bot.fetch_user(uid)
    
    await ctx.guild.unban(u)

    await ctx.send(f"{user.mention}foi desbanido")

    invite_channel = await u.create_dm()

    await invite_channel.send("discord.gg/epk8bFT")

# theese are funny (Super funny) commands
@bot.command(pass_context  = True)
async def dbd(ctx):
    vruh2 = await bot.fetch_user(146956554371989504)
    fj = await bot.fetch_user(578714642843435019)
    lp = await bot.fetch_user(539137498664665109)
    b = await bot.fetch_user(441986625283686413)
    Channel_b = await b.create_dm()
    Channel_v = await vruh2.create_dm()
    Channel_f = await fj.create_dm()
    Channel_l = await lp.create_dm()

    try:
        await Channel_b.send("Alguem usou este comando pois quer jogar dbd contigo")
        print("b check")
    except:
        print("b fail")
    try:
        await Channel_f.send("Alguem usou este comando pois quer jogar dbd contigo")
        print("f check")
    except:
        print("f fail")
    try:
        await Channel_v.send("Alguem usou este comando pois quer jogar dbd contigo")
        print("v check")
    except:
        print("v fail")
    try:    
        await Channel_l.send("Alguem usou este comando pois quer jogar dbd contigo")
        print("l check")
    except:
        print("l fail")
    await ctx.message.channel.send("Baiano Vruh 2 Fellow jitster e Lemon convidados para o dbd (Pallet loop)")

@bot.command(pass_context = True)
async def rr(ctx, m1: discord.User, m2: discord.User, m3: discord.User = "",m4: discord.User = "", m5: discord.User = "", m6: discord.User = ""):
    members_t = [m1, m2, m3, m4, m5, m6]
    members = []
    participants = []

    for m in members_t:
        if m  != "":
            members.append(m)

    for m in members:
        if m.id not in participants:
            participants.append(m.id)

    response = await ctx.send("Reaja para confirmar")
    await response.add_reaction("👍")

    time.sleep(15)

    print(participants)


    response = await response.channel.fetch_message(response.id)
    
    count = 0

    for r in response.reactions:
        count += r.count

    p_kick = random.choice(members)

    if p_kick.id in participants:
        kicked = p_kick
    
    if count - 1 >= len(participants) and ctx.message.author.id in participants:
        print("fire log")
            
        print(participants)
        print(kicked)
        print()
        print(f"counter = {count}")

        await ctx.guild.kick(kicked)
        await ctx.send(f"{kicked.name} foi kickado")

    else:
        print(participants)
        print(kicked)
        print()
        print(f"counter = {count - 1 }")
        print(f"len = {len(participants)}")
        await ctx.send("Nem todos os participantes concordaram ou voce n esta participando da roleta")



@bot.command(pass_context = True)
async def vote_kick(ctx, user:discord.Member):
    call =  await ctx.send(f"Vote para kickar {user.mention}")
    await call.add_reaction("🟢")
    await call.add_reaction("🔴")

    time.sleep(20)

    p = 0
    n = 0 
    total_v = 0

    votes = await call.channel.fetch_message(call.id)

    for react in votes.reactions:
        if react.emoji == "🟢":
            p = react.count -1
        elif react.emoji == "🔴":
            n = react.count -1

    total_v = p - n

    if total_v >= 3:
        await user.kick()
        await ctx.send(f"{user.name} foi kickado pela maioria")
    
    else:
        await ctx.send("N houveram votos suficientes")

    
    print(votes.reactions)
    print(total_v)
    print(user.name)
    print(ctx.message.author.name)

# a weird attempt on music commands

@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

# mergency command

@bot.command(pass_context = True)
async def close(ctx):
     exit()

bot.run("NzczOTMzNDUxMDM5NDczNjcy.X6QbsQ.rBCNpShd8tn8DVlhbdHgBAwEnIU")