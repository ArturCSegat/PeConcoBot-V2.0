import discord # importa a biblioteca discord pra usar classes e funções do discord
from discord import client # n lembro mas tem a ver com a linha 1
from discord import message # n  lembro mas tem a ver com a linha 1
from discord.enums import AuditLogAction, RelationshipType #esse eu n faço idea 
from discord.ext import commands # esse permite q possamos criar comandos no caso @bot.command
import random # usado na função rr ou roleta russa para escolher o cara kickado de maneita aleatoria
import top # permite usar variaveis funções e classes do arquivo top.py (ver pata)
import time # usado nas funções votekick e rr para usar funções relacionadas sobre tempo como time.sleep para espear x segundos
import membro_OOP # permite usar as classes de membro_OOP.py (ver pasta)
import requests
import random
import asyncio

intents = discord.Intents.all() # n lembro onde isso é usado mas é importante n remova
intents.presences = True # ver acima
intents.messages = True # ver acima

bot = commands.Bot(command_prefix="!", intents=intents)   # cria a variavel bot usando o modulo commands (ver linha 6)

@bot.event
async def on_ready(): # essa funçao usa async para printar "ready" no log quando o bto esta pronto para receber comandos
    print("ready")

@bot.event
async def on_member_join(member: discord.Member): #função chamada toda vez q alguem entra levando member como argumento representando o memebro que entrou

    guild = bot.get_guild(581158091115200535) # esse numero é o id do pe conco server ou seja é uma variavel para o pe conco server do tipo server(objeto do modulo commands(ver linha 6 e a linha onde bot é definido))


# roles, todos esses sçao os cargos do servidor com seus respectivos ids, no futuro mudar todos como variaveis globais como é o caso do cargo cv q ja foi atualizado
    pleb = guild.get_role(818486529314783263)
    c_master = guild.get_role(832611250348228628)
    chadCargo = guild.get_role(818487902606327878)
    baiano_cargo = guild.get_role(849469082566262839) 
    botRole = guild.get_role(818487365956796456)
    atlantida = guild.get_role(819565407282266112)
    macho_g = guild.get_role(847287306858528828)
    s_tereza = guild.get_role(859066768601645066)
    f_tereza = guild.get_role(856282555703492638)
    chadPreto = guild.get_role(856056567491985419)
    indio = guild.get_role(862672037835178004)
    redk = guild.get_role(860139656796700682)
    pimonte = guild.get_role(862067103061377034)
    f = guild.get_role(862333483732566066)
    cv = guild.get_role(top.CV) # esse cargo é diferente pq ele usa uma variavel importada do modulo top.py(ver linha 8) tecnicamente todos eles podiam ser assim mas eu tenho preguissa
    

# members, cada um desses objetos são os membros do server q tem autotole, a primeira palavra e so identificação normal e n serve pra nada, o segundo é o id deles no discord e a terceira é o cargo deles para o autorole, ver seção de cargos acima
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
    miguel = membro_OOP.Membruh("mjairmingho", 854510245987483668, macho_g)
    gi = membro_OOP.Membruh("gi", 673769040979689472, cv)
    julia_cv = membro_OOP.Membruh("julia_cv", 762057443102425109, cv)
    jofi = membro_OOP.Membruh("JOFI", 323910014190223363, cv)
    isona = membro_OOP.Membruh("Isona", 368897414188236800, cv)
    franco = membro_OOP.Membruh("puflew", 440562108724281344, chadPreto)
    limao = membro_OOP.Membruh("limao", 539137498664665109, s_tereza)
    japa = membro_OOP.Membruh("japa", 413152550242615306, chadPreto)


    members = [vruh2, omni, chad, ernestoChe, baiano, tocomdor, pontos, drealocks, epiclord, MC_lendrinho, miguel, gi, julia_cv, jofi, isona, franco, limao, japa]

#  ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ essa lista é dos membros q tem autorole se for adicionar autorole para alguem adicione ele(ela)  na lista tmb se n n funciona

    members_hash = {m.ident: m for m in members} # cria um hash com todos os membros na lista members e seus respectivos id's no discord
# handles giving out the roles
    if member.id in members_hash: # se o id do membro q entrou estiver no hash execute o abaixo
        await member.add_roles(members_hash[member.id].cargo, reason=None, atomic=True) # da o cargo do membro pra ele, pra pegar o carfo ele olha quem é o membro no hash e verfica a variavel cargo dele ja que ele é um objeto to tipo membruh
# if the user isn't on the list above this section
    else: # se o membro n tiver um autorole definido so de o cargo pleb
        await member.add_roles(pleb, reason=None, atomic=True)
    

@bot.event
async def on_message(message): # isso é executado toda vez q uma msg é enviada em qualquer server q o bot esteja, no momento vazio
    # ctx = await bot.get_context(message) 
    # Essa linha é muito importante n apague ela quebra o bot
    if "teresa" in message.content.lower():
        await message.channel.send("É com z")
    await bot.process_commands(message)
#only commands from here



# Debug commands
@bot.command(pass_context = True)
async def test(ctx, user: discord.User):
    await ctx.send(ctx.message.author.top_role)
    await ctx.send(user.top_role)

@bot.command(pass_context =True)
async def test2(ctx):
    await ctx.send("ok") # ctx.send() é parecido com print() so que ao inves de mandar uma msg no log console manda no canal onde o bot recebeu o comando

@bot.command(pass_context =True)
async def test3(ctx):
    await ctx.send("a")

@bot.command(pass_context =True)
async def testembed(ctx):
    embedVar = discord.Embed(title="Teste de embed", description="Olá, " + ctx.message.author.mention, color=0x00ff00) # eu esqueci tudo o q eu sabi sobre mebd pergunta por vruh2 
    await ctx.send(embed=embedVar)



# Message-related commands
@bot.command(pass_context = True)
async def clear(ctx, number: int): #comando clear levando ctx(contexto(objeto do discord(ver linha 1)) e number sendo o numero q tu coloca quando tu manda o comando(exemplo !clear 30 number = 30))
    if number <= 50: # se o numero q o cara colou for menor ou igual a 50 
        await ctx.message.channel.purge(limit=number) # de purge com o limite sendo o numero colocado(purge é um methodo do disrcod tmb eu n sei como ele funciona pq é closed source mas eu sei q ele delata um numero x de msgs)
        embedVar = discord.Embed(description=f"{ctx.message.author.mention} deletou {number} mensagens", color=0x000000)
        await ctx.send(embed=embedVar)     
        print("clear command used")
    else:
        await ctx.send("Por favor nao")


# Moderation commands
# Rewritten with embed support -- kfh

@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member, is_in_code = 0): #comando de kick levando um argumento user sendo o cara q tu quer kickar e um argumento opcional sendo is_in_code q por defualt é igual a 0 q no momento n faz nada
    commander = ctx.message.author #commander´seria o cara q mandou a msg
    r_dict = top.role_lvl # reliquia de codigo passado, no momento inutil, pode causar errro futuro remover se quiser
    valid_t = top.checkRole(commander.top_role.id, user.top_role.id) # cria a variavel valid_t sendo o resultado da função checkRole(ver top.py) sendo True so o commandder tiver um cargo melhor ou False se ele tiver umc argo pior
    if ctx.message.author.id == 354303193372557313 and user.id == 146956554371989504: #porra estranha do kfh eu n sei oq faz
           await ctx.send("Fake")
           time.sleep(5)
           await ctx.send("Fakíssimo")
    elif valid_t: # se valid_t for True
        embedVar = discord.Embed(title="Membro Kickado", description=f"{user.mention} foi kickado", color=0xded707)
        await ctx.send(embed=embedVar)
        await user.kick() # de kick no cara q foi pedido para kickar
        u = await bot.fetch_user(user.id) # achq ele denovo
        invite_channel = await u.create_dm() # cria uma dm com ele
        await invite_channel.send("Entra de novo ai putelho, https://discord.gg/epk8bFT") # manda o convite classico
    else: #se valid_t  for False
        embedVar = discord.Embed(description="Este usuario tem um cargo melhor que o seu ou o seu cargo não existe", color=0x3289a8)
        await ctx.send(embed=embedVar)

@bot.command(pass_context = True)
async def ban(ctx, user: discord.Member): # e a mesma coisa q o kick mas ao inves de kikcar ele bane e el n mando o invite dps
    commander = ctx.message.author
    r_dict = top.role_lvl
    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if valid_t:
        embedVar = discord.Embed(title="Membro Banido", description=f"{user.mention} foi banido", color=0xa83232)
        await ctx.send(embed=embedVar)
        await user.ban()
    else:
        embedVar = discord.Embed(description="Este usuario tem um cargo melhor que o seu ou o seu cargo não existe", color=0x3289a8)
        await ctx.send(embed=embedVar)

@bot.command(pass_context = True)
async def pogoban(ctx, user: discord.Member): # é a memsa coisa q o ban mas se valid_t for True ele bane os dois mas se valid_t for False ele so kicka o commander
    commander = ctx.message.author
    r_dict = top.role_lvl
    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if ctx.message.author.id == 441986625283686413: #putisse fo vruh2
        await ctx.send("Te fode baiano")
    elif valid_t:
        await user.ban()
        await commander.ban()
        embedVar = discord.Embed(title="Membro suicida!!!", description=f"{commander.mention} ficou sem motivos pra viver, e explodiu {user.mention} junto com ele", color=0xff9100)
        await ctx.send(embed=embedVar)
    else:
        await commander.ban()
        embedVar = discord.Embed(title="Burro do caralho", description=f"{commander.mention} tentou se suicidar e levar junto {user.mention}, mas seu QI era de uma porta (ele morreu sozinho kk)", color=0xff00ff)
        await ctx.send(embed=embedVar)

# Epiclord se você questionar por que tem um comando duplicado, foi o baiano que pediu
@bot.command(pass_context = True)
async def pogokick(ctx, user: discord.Member): #mesma coisa q o @pogoban mas ele kicka e ele tmb n manda invite (next update perhaps?)
    commander = ctx.message.author
    r_dict = top.role_lvl
    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if ctx.message.author.id == 441986625283686413:
        await ctx.send("Te fode baiano")
    elif valid_t:
        await user.kick()
        await commander.kick()
        embedVar = discord.Embed(title="Membro suicida!!!", description=f"{commander.mention} ficou sem motivos pra viver, e explodiu {user.mention} junto com ele", color=0xded707)
        await ctx.send(embed=embedVar)
    else:
        await commander.kick()
        embedVar = discord.Embed(title="Burro (mas não tanto)", description=f"{commander.mention} tentou se suicidar e levar junto {user.mention}, mas seu QI era de uma britadeira (ele morreu sozinho kk)", color=0xff00ff)
        await ctx.send(embed=embedVar)

@bot.command(pass_context = True)
async def superultramegaban(ctx, user :discord.Member): # n vou comentar nesse
    commander = ctx.message.author
    #simple test
    r_dict = top.role_lvl

    valid_t = top.checkRole(commander.top_role.id, user.top_role.id)

    if valid_t:
        await user.ban()
        embedVar = discord.Embed(title="Kapow", description=f"{commander.mention} super ultra mega baniu {user.mention} (ultra morte)", color=0xff9100)
        await ctx.send(embed=embedVar)
    else:
        embedVar = discord.Embed(description="Este usuario tem um cargo melhor que o seu ou o seu cargo não existe", color=0x3289a8)
        await ctx.send(embed=embedVar)

@bot.command(pass_context = True)
async def unban(ctx, user: discord.User): # esse funciona de um jeito um pouco diferent mas é bem parecido com a parte de mandar invite da função kick
    uid = user.id
    u = await bot.fetch_user(uid) #essas duas linhas acham o usuario pra ser desbaido
    
    await ctx.guild.unban(u) #essa linha desbane ele
    embedVar = discord.Embed(title="Membro desbanido", description=f"{user.mention} foi desbanido", color=0x11ff00)
    await ctx.send(embed=embedVar)
    invite_channel = await u.create_dm() #aqui cria a dm com ele 
    await invite_channel.send("Vc foi desbanido, https://discord.gg/epk8bFT") # aqui manda o invite

# theese are funny (Super funny) commands
@bot.command() # P
async def kickall(ctx):# U
    if ctx.message.author.id == 441986625283686413:# T
        await ctx.send(ctx.message.author.mention + ", q falta de consideração sua") # I
    else: # C (funny typo)
        await ctx.send("Kk te fode") # E

@bot.command(pass_context = True)
async def teresa(ctx): # isso seria pra mandar ´"é com z" toda vez q alguem mandasse teresa mas n funciona pq ele so manda se for !teresa pra funcionar teria q ser colocado naquela função destivada na linha 81
    await ctx.send("É com z")
@bot.command(pass_context  = True)
async def dbd(ctx): #comando dbd

    ts = [441986625283686413, 539137498664665109, 578714642843435019] #lista dos ids das pessoas q recebem as msgs

    for t in ts: # executa esse codigo pra todo mundo na lista levando t como o id 
        user = await bot.fetch_user(t) # encontra o alvo
 
        channel = await user.create_dm() #cria a dm

        await channel.send("Alguem usou este comando pois quer jogar dbd contigo") # manda a msg

    await ctx.message.channel.send("Baiano Fellow jitster e Lemon convidados para o dbd (Pallet loop)") #avisa a pessoa q mandou !dbd que as msgs foram enviadas

@bot.command()
async def bogokick(ctx, user: discord.Member): # cara se tu for o vruh2 imagino q tu entenda, se tu for o bruno boa sorte tentado entender

    commander = ctx.message.author # define o autor da msg, vai ser usado pra definir valid_t

    valid_t = top.checkRole(commander.top_role.id, user.top_role.id) # verfica seo  autor da msgtem cargo suficiente

    if valid_t: # se o autor tiver cargo suficiente

        counter = 1 # cria um contador para as tentativas

        nums = [1, 2, 3, 4, 5, 6] # cria a primeira lista com ela ja em ordem por default
        newNums = [] # cria a lista vazia onde vamos tentar colocar a primeira lista em orddem (lista para tentar)
        for num in nums: # loopa por todods os numeros da lista default
            newNums.insert(random.randint(0,5), num) # coloca o numero em um index aleatorio da lista de tentativa
        seql = await ctx.send(newNums) # manda a msg dizendo a primeira tentativa

        await ctx.send(f"Sua morte é iminente, {user.mention}") # msg classica
        
        if newNums == [1,2,3,4,5,6]: # verifica se a primeira tentativa foi um sucesso 
            await user.kick()
            await ctx.send(f"{user.mention} foi kickado de primeira")
            
        else: # se ela n for
            while newNums != [1, 2, 3, 4, 5, 6]:
                newNums.clear() # limpa a lista tentada
                for num in nums: # deixa a lista aleatoria de novo
                    newNums.insert(random.randint(0,5), num) # ver acima
                
                await asyncio.sleep(1) # dorme por um segundo

                e_seql = await seql.channel.fetch_message(seql.id) # pega a msg dizendo a priemria tentativa de novo
                await e_seql.edit(content=newNums) #edita ela com a tentativa atual
                counter = counter + 1 # aumenta o counter

            # print(newNums) Esses prints estão comentados por servir ~funcções de debug e spamar d+ nos logs -EpicLord
            await user.kick() 
            await ctx.send(f"O bot acertou o bogosort e kickou {user.mention} em {counter} tentativas")
    else:
        ctx.send("Este usuario tem um cargo melhor q o seu")
        
        
@bot.command()
async def fox(ctx):

    respose = requests.get('https://randomfox.ca/floof/')

    x = respose.json()

    await ctx.send((x["image"]))

@bot.command(pass_context = True) # cara essa função é purra putisse mas eu vou tentar
async def rr(ctx, m1: discord.User, m2: discord.User, m3: discord.User = "",m4: discord.User = "", m5: discord.User = "", m6: discord.User = ""): #esses são os argumentos da função, o m1 e m2 são obrigatorios(a função n funciona sem eles) mas o resto é opcional e é definido para "" por default
    members_t = [m1, m2, m3, m4, m5, m6] # essa é a lista de todos os argumentos passados
    members = [] #
    participants = []

    for m in members_t: #vefifica se todos os mebros existem, se o membro existir ele vai pra lista members, se ele for "" nada acontece
        if m  != "":
            members.append(m)

    for m in members: # essa parte verifica q n tem duplas ou seja "!rr @EpicLord @vruh2" e "!rr @EpicLord @EpicLord @vruh2" tem a mesma chance de vitoria pros dois lados
        if m.id not in participants:
            participants.append(m.id)

    response = await ctx.send("Reaja para confirmar") # manda a classica mensagem       # Inembedavel, não manda a mensagem caso for um embed (???)
    await response.add_reaction("👍") # reage com a classica mensagem

    await asyncio.sleep(15) # n faz absolutamente nada por 15 segundos

    print(participants) # debug print


    response = await response.channel.fetch_message(response.id) # volta pra msg classica q mandou 15 segundos atras
    
    count = 0 # cria um contador 

    for r in response.reactions: # honestamente, eu n sei, eu acho q ele conta quantas reações tem a msg
        count += r.count

    p_kick = random.choice(members) # escolhe alguem aleatorio da lista members por algum motivo

    if p_kick.id in participants: # verifica se o cara q foi kickado ta em participants (wtf?)
        kicked = p_kick # kicked = p_kick ? p? ?
    
    if count - 1 >= len(participants) and ctx.message.author.id in participants: #verifica se tem reações suficientes e so o cara q andou o comando esta na lista de kickaveis
        print("fire log")
            
        print(participants)
        print(kicked)
        print()
        print(f"counter = {count}")

        await ctx.guild.kick(kicked) # kicka o escolhido
        await ctx.send(f"{kicked.name} foi kickado") # avisa quem foi kickado

    else: # se n tiver reações suficientes ou o car an tiver na msg
        print(participants)
        print(kicked)
        print()
        print(f"counter = {count - 1 }")
        print(f"len = {len(participants)}")
        await ctx.send("Nem todos os participantes concordaram ou voce n esta participando da roleta")


@bot.command(pass_context = True)
async def vote_kick(ctx, user:discord.Member): # o comando esquecido usado tipo 4 vezes
    call =  await ctx.send(f"Vote para kickar {user.mention}") # manda  uma msg disendo quem vai ser kickado 
    await call.add_reaction("🟢")
    await call.add_reaction("🔴") # poe as duas reações na msg


    await asyncio.sleep(20) # morre por 20 sgundos
    
    p = 0 # votos positivos
    n = 0  # votos nigga ativos
    total_v = 0 # votos totais

    votes = await call.channel.fetch_message(call.id) # pega a msg que mandou antes

    for react in votes.reactions: # ve todas as reções ad msg
        if react.emoji == "🟢": # se a reação for verde aumente um ponto p:
            p = react.count -1 
        elif react.emoji == "🔴": # se a reaçõ for vermlho aument um ponto em vermelho
            n = react.count -1

    total_v = p - n # diminui vermelho de verde pra pegar a diferença

    if total_v >= 3: # se tiver uma diferença de 3 ou mais (igual no cs)
        await user.kick() #kicka o cara 
        await ctx.send(f"{user.name} foi kickado pela maioria") #msg
    
    else:
        await ctx.send("N houveram votos suficientes") # : (

    
    print(votes.reactions)
    print(total_v)
    print(user.name)
    print(ctx.message.author.name)

# a weird attempt on music commands

@bot.command(pass_context = True)
async def join(ctx): #comando de join
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(pass_context = True)
async def suicidio(ctx): #pergunta pro quaser foi ele que fez
    commander = ctx.message.author 
    u =  bot.fetch_user(commander.id)
    await commander.kick()
    embedVar = discord.Embed(title="Morte", description=f"{commander.mention} se matou")
    await ctx.send(embed=embedVar)
    invite_channel = await u.create_dm()
    await invite_channel.send("Emo da porra, https://discord.gg/epk8bFT")

# mergency command

# @bot.command(pass_context = True)
# async def close(ctx): #comando !close
#      exit() # esse exit() simplesmente fecha o arquivo, funciona com qualquer arquivo de python

bot.run("NzczOTMzNDUxMDM5NDczNjcy.X6QbsQ.rBCNpShd8tn8DVlhbdHgBAwEnIU") # isso faz o bot ficar online
