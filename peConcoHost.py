
import discord
from discord import client
from discord import message
from discord.enums import AuditLogAction, RelationshipType
from discord.ext import commands
import random
import top
import time
import membro_OOP

# ╔═══╗───────────────────╔╗────╔╗
# ║╔═╗║───────────────────║║───╔╝╚╗
# ║╚═╝╠══╗╔══╦══╦═╗╔══╦══╗║╚═╦═╩╗╔╝
# ║╔══╣║═╣║╔═╣╔╗║╔╗╣╔═╣╔╗║║╔╗║╔╗║║
# ║║──║║═╣║╚═╣╚╝║║║║╚═╣╚╝║║╚╝║╚╝║╚╗
# ╚╝──╚══╝╚══╩══╩╝╚╩══╩══╝╚══╩══╩═╝

intents = discord.Intents.all()
intents.presences = True
intents.messages = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("ready")

@bot.event
async def on_member_join(member: discord.Member):
    canal = await bot.get_channel(760586755672899634)
    guild = bot.get_guild(581158091115200535)
    # Como que ele vai mencionar o membro que entrou sendo que ele não foi definido? discord.Member?
    await canal.send("Teste")


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
    chadPreto = guild.get_role(856056567491985419)
    indio = guild.get_role(862672037835178004)
    redk = guild.get_role(860139656796700682)
    pimonte = guild.get_role(862067103061377034)
    f = guild.get_role(862333483732566066)
    cv = guild.get_role(top.CV)
    

# members
    vruh2 = membro_OOP.Membruh("kfh", 146956554371989504, c_master)
    omni = membro_OOP.Membruh("omni", 225051659221467137, chadPreto)
    chad = membro_OOP.Membruh("faxina", 584776317321609238, chadCargo)
    ernestoChe = membro_OOP.Membruh("ernesto", 691069156400824372, indio)
    baiano = membro_OOP.Membruh("breno", 441986625283686413, baiano_cargo)
    tocomdor = membro_OOP.Membruh("dudz", 358985083329314816, redk)
    pontos = membro_OOP.Membruh("...", 578714642843435019, macho_g)
    drealocks = membro_OOP.Membruh("Drealocks", 354303193372557313, baiano_cargo)
    epiclord = membro_OOP.Membruh("Epic", 423503073479098368, chadPreto)
    MC_lendrinho = membro_OOP.Membruh("loldrinho", 423596836578918444, f)
    miguel = membro_OOP.Membruh("mjairmingho", 854510245987483668, pleb)
    gi = membro_OOP.Membruh("gi", 673769040979689472, cv)
    julia_cv = membro_OOP.Membruh("julia_cv", 762057443102425109, cv)
    jofi = membro_OOP.Membruh("JOFI", 323910014190223363, cv)
    isona = membro_OOP.Membruh("Isona", 368897414188236800, cv)
    franco = membro_OOP.Membruh("puflew", 440562108724281344, chadPreto)



    members = [vruh2, omni, chad, ernestoChe, baiano, tocomdor, pontos, drealocks, epiclord, MC_lendrinho, miguel, gi, julia_cv, jofi, isona, franco]

    members_hash = {m.ident: m for m in members}
# handles giving out the roles
    if member.id in members_hash:
        await member.add_roles(members_hash[member.id].cargo, reason=None, atomic=True)
# if the user isn't on the list above this section
    else:
        await member.add_roles(pleb, reason=None, atomic=True)
    

@bot.event
async def on_message(message):
    ctx = await bot.get_context(message)
    await bot.process_commands(message)


#only commands from here

# this section is exclusively for debugging and testing purposes

# obsoleted
#@bot.command(pass_context =True)
#async def test(ctx, user: discord.User):
#    if user.top_role.name == "Membros":
#        await ctx.send("O seu maior cargo é Membros")

@bot.command(pass_context = True)
async def test(ctx, user: discord.User):
    await ctx.send(ctx.message.author.top_role)
    await ctx.send(user.top_role)

@bot.command(pass_context =True)
async def test2(ctx):
    await ctx.send("ok")

@bot.command(pass_context =True)
async def test3(ctx):
    await ctx.send("a")

@bot.command(pass_context =True)
async def testembed(ctx):
    embedVar = discord.Embed(title="Teste de embed", description="Olá, " + ctx.message.author.mention, color=0x00ff00)
    await ctx.send(embed=embedVar)

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

    
    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)


    if valid_t:

        await ctx.send(f"{user.mention} foi kickado")
        await user.kick()
        u = await bot.fetch_user(user.id)

        invite_channel = await u.create_dm()

        await invite_channel.send("discord.gg/epk8bFT")

    else:
        await ctx.send("Este usuario tem um cargo melhor que o seu ou o seu cargo não existe")

@bot.command(pass_context = True)
async def ban(ctx, user: discord.Member):
    commander = ctx.message.author

    r_dict = top.role_lvl

    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if valid_t:
        await ctx.send(f"{user.mention} foi banido")
        await user.ban()
    else:
        await ctx.send("Este usuario tem um cargo melhor que o seu ou o seu cargo não existe")
@bot.command(pass_context = True)
async def pogoban(ctx, user: discord.Member):
    commander = ctx.message.author

    r_dict = top.role_lvl

    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if valid_t:
        await user.ban()
        await commander.ban()
        await ctx.send(f"{user.mention}{commander.mention} foram banidos")
    else:
        await commander.ban()
        await ctx.send(f"{commander.mention} tinha um cargo menor e foi banido por ser burrinho")

@bot.command(pass_context = True)
async def superultramegaban(ctx, user :discord.Member):
    commander = ctx.message.author
    #simple test
    r_dict = top.role_lvl

    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if valid_t:
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
@bot.command()
async def kickall(ctx):
    if ctx.message.author.id == 441986625283686413:
        await ctx.send("Baiano q falta de consideração sua")
    else:
        await ctx.send("Kk te fode")
 
@bot.command(pass_context  = True)
async def dbd(ctx):

    ts = [146956554371989504, 441986625283686413, 539137498664665109, 578714642843435019]

    for t in ts:
        user = await bot.fetch_user(t)

        channel = await user.create_dm()

        await channel.send("Alguem usou este comando pois quer jogar dbd contigo")

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
