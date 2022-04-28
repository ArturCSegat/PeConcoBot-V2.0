import random
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

top_r =  [] # reiquia de codigo antigo
top_r_bans =  [] #reliquia de codigo antigo

# esses são os cargos do servidor, na vdd são os ids deles no futor eu vou mudar umas coisas no autorole(ver linha do cargo cv no peconcohost.py) pra usarem isso mas tmb server pra poder ver a lista de role lvsls melhor
CM = 832611250348228628
CV = 865393494951198740
cs = 856056567491985419
pi = 849469082566262839
HM = 862333483732566066
redk = 860139656796700682
ind = 862672037835178004
c = 818487902606327878
ST = 859066768601645066
FT = 856282555703492638
BOT = 818487365956796456
atl = 819565407282266112
p = 818486529314783263
b = 862067103061377034
MG = 847287306858528828

role_lvl = [b,CM, CV, cs, pi, HM, redk, ind, c, ST, FT, BOT, atl, p,MG]
nd
# essa é a lista de poder dos cargos na visão do bot quanto mais no começo ou mais na esquerda melhor
# isso quer dizer que quanto menor o index do cargo nessa lista melhor ele é de acordo com a  função checkrole(ver abaixo)
#por exemplo baiano tem o menor index no caso 0 pq ele é o primeiro item da lista, logo, para o bot ele é o melhor cargo


def checkRole(id1, id2): # essa é a função leva dois ids de cargo, ela vai olhas os dois cargos na lista e reponder True se o primeiro cargo for o melhor e False so o segundo for melhor, usada nos comandos kick ban pogoban pogo kick e no futuro bogo kick e bogoban imagino
    valid = False # cria a variavel valid como False por defaultl
    if role_lvl.index(id1) < role_lvl.index(id2): # o index do id1 for menor execute o codigo abaixo
        valid = True
        return valid # retorna valid como True
    else:
        return valid # retorna valid como False

def bogoSort(nums): #vou deixar isso aqui pra algum dia hhihi -EpicLord
    newNums = []
    for num in nums:
        newNums.insert(random.randint(0,5), num)
    # print(newNums)
    
    if newNums == [1,2,3,4,5,6]:
        return "yay"
    else:
        while newNums != [1, 2, 3, 4, 5, 6]:
            newNums.clear()
            for num in nums:
                newNums.insert(random.randint(0,5), num)
        #     print(newNums)
        
        # print(newNums) Esses prints estão comentados por servir ~funcções de debug e spamar d+ nos logs -EpicLord
        return "found it"

        # maluco essa função vai ficar aqui parada por um bom tempo pq ela simplesmente n serve pra oq eu quero,
        # n vou apagar mas tmb n vou usar se alguem precisar de um sort use o sort padrão do python como no exemplo abaixo
        # x = [2, 3, 1, 4]
        # x.sort()
        # print(x) 

        # [1, 2, 3, 4]
        # - EpicLord
