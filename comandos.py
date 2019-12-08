
Dicionario_Geral=DG={
    "jogadores":{
    #    "jogador1":{
    #        "vitórias":0,
    #        "jogos_jogados":0,
    #    }
    },

    "jogo_em_curso":False,

    "jogadores_em_jogo":{
        #"jogador1":{
            #"tabuleiro":[],
            #"Frota":{}
        # }
    },

    "Frota":{
        
        "L":{
            "nome":"Lancha",
            "tamanho":1,
            "quantidade":4,
            "navios_colocados":4
        },

        "S":{
            "nome":"Submarino",
            "tamanho": 2,
            'quantidade':3,
            "navios_colocados":3
        },

        "F":{
            "nome":"Fragata",
            "tamanho":3,
            "quantidade":2,
            "navios_colocados":2
        },

        "C":{
            "nome":"Cruzador",
            "tamanho": 4,
            'quantidade':1,
            "navios_colocados":1
        },
        
        "P":{
            "codigo":"Porta Avioes",
            "tamanho": 5,
            'quantidade':1,
            "navios_colocados":1
        }

    }
}
#--------------------------------------------------------------------------------

def Existe_Jogador(DG,nome):
    if nome in DG["jogadores"].keys():
        return True
    return False
    

def Registar_Jogadores(DG,nome):        #Adiciona o jogador ao dicionário 
    DG["jogadores"][nome]={
        "vitorias":0,
        "Jogos":0,
        }
    return DG


def existe_jogador_em_jogo(DG, nome):
    for jogador in DG["jogadores_em_jogo"].keys():
        if jogador==nome:
            return True
    return False
    

def Remover_Jogadores(DG, nome):          #Retira o jogador do dicionário.
    del DG["jogadores"][nome]
    

def sort_jogadores(DG):
    return sorted(DG["jogadores"].keys())

def Listar_Jogadores(DG):
    Lista=[]
    for i in sort_jogadores(DG):
        Lista.append(i)
    return Lista
                  

def Iniciar_Jogo(DG,nome1,nome2):
    if DG["jogo_em_curso"]==True:
        return("Existe um jogo em curso.")

    elif Existe_Jogador(DG, nome1) and Existe_Jogador(DG, nome2):
        lista_sort=sorted([nome1,nome2])

        #----------------------criar tabuleiros------------------
        DG["jogadores_em_jogo"][lista_sort[0]]={"tabuleiro":[[0 for _ in range(0,10)] for _ in range(0,10)]}

        DG["jogadores_em_jogo"][lista_sort[1]]={"tabuleiro":[[0 for _ in range(0,10)] for _ in range(0,10)]}
        #-------------------------Criar Frota--------------------
        DG["jogadores_em_jogo"][lista_sort[0]]["Frota"]=DG["Frota"]

        DG["jogadores_em_jogo"][lista_sort[1]]["Frota"]=DG["Frota"]
        #--------------------------------------------------------

        DG["jogo_em_curso"]=True
        return(f'Jogo iniciado entre {lista_sort[0]} e {lista_sort[1]}.')
    else:
        return("Jogadores não registados.")

def print_tabuleiro(tabuleiro):
    Letras=["","A","B","C","D","E","F","G","H","I","J"]
    for letra in range(0,len(Letras)):
        print(f"{Letras[letra]:<3}", end="")
    print()
    for linha in range(0, len(tabuleiro)):
        print(f"{(linha+1):<2}", end="")
        for coluna in range(0,len(tabuleiro)):
            print(f"[{tabuleiro[linha][coluna]}]", end="")
        print()

def translator(letra):                      #Traduz uma letra para uma posição index da lista.
    return ord(letra)-65

def bloco(DG,nome,linha,coluna,tipo,orientacao): #Cria blocos á volta da posição pretendida, impedindo assim a colocação de navios nas redondesas desse navio
    a=[[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
    tabuleiro=DG["jogadores_em_jogo"][nome]["tabuleiro"]
    posiçao=[linha,coluna]
    tabuleiro[posiçao[0]] [posiçao[1]]=tipo
    for i in a:
        if not posiçao[0]+i[0]<0 and not posiçao[0]+i[0]>9  and not posiçao[1]+i[1]<0 and  not posiçao[1]+i[1]>9:
            if tabuleiro[posiçao[0]+i[0]] [posiçao[1]+i[1]]==0:
                tabuleiro[posiçao[0]+i[0]] [posiçao[1]+i[1]]="x"


def verificar_posiçao_em_tabuleiro(DG,tipo,linha,coluna,orientacao):
    tamanho=DG["Frota"][tipo]["tamanho"]
    permite=True
    posiçao=[linha,coluna]

    for i in range(0,tamanho):               #Delimita o espaço de jogo.
        if orientacao=="O":
            if posiçao[1]-i <0:
                permite=False
        if orientacao=="E":
            if posiçao[1]+i >9:
                permite=False
        if orientacao=="S":
            if posiçao[0]+i >9:
                permite=False
        if orientacao=="N":
            if posiçao[0]-i <0:
                permite=False

    return permite



def Colocar_Navios(DG,nome,tipo,linha,coluna,orientaçao):
    if DG["jogo_em_curso"]==False:
        return("Não existe um jogo em curso.")
    if existe_jogador_em_jogo(DG,nome):
        tamanho=DG["Frota"][tipo]["tamanho"]
        posiçao=[linha-1,translator(coluna)]
        for i in range(0,tamanho):
            if orientaçao=="O":
                bloco(DG,nome,posiçao[0],posiçao[1]-i,tipo,orientaçao)
            if orientaçao=="E":
                bloco(DG,nome,posiçao[0],posiçao[1]+i,tipo,orientaçao)
            if orientaçao=="S":
                bloco(DG,nome,posiçao[0]+i,posiçao[1],tipo,orientaçao)
            if orientaçao=="N":
                bloco(DG,nome,posiçao[0]-i,posiçao[1],tipo,orientaçao)
        return("Navio colocado com sucesso.")

    else:
        print("Jogador não participa no jogo em curso.")
