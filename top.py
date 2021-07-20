#variables for roles to have better redablilty or however you wirte this

top_r =  []
top_r_bans =  []

CM = 832611250348228628
CV = 865393494951198740
chads = 856056567491985419
pimonte = 849469082566262839
HM = 862333483732566066
Redklauss = 860139656796700682
Indio = 862672037835178004
chad = 818487902606327878
ST = 859066768601645066
FT = 856282555703492638
BOT = 818487365956796456
atlantida = 819565407282266112
pleb = 818486529314783263
baiano = 862067103061377034
MG = 847287306858528828

role_lvl = [CM, CV, chads, pimonte, HM, Redklauss, Indio, chad, ST, FT, BOT, atlantida, pleb, baiano, MG]


def checkRole(id1, id2):
    valid = false
    if role_lvl.index(id1) < role_lvl.index(id2):
        valid = True
        return valid
    else:
        return valid