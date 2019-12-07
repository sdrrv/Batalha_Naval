
Dicionario_Geral=DG={
    "jogadores":{
    #    "jogador1":{
    #        "vitórias":0,
    #        "jogos_jogados":0,
    #    }
    },

    "jogo_em_curso":False,

    "jogadores_em_jogo":[]
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
    for jogador in DG["jogadores_em_jogo"]:
        if jogador==nome:
            return True
    return False
    

def Remover_Jogadores(DG, nome):          #Retira o jogador do dicionário 
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
        DG["jogadores_em_jogo"]=sorted([nome1,nome2])
        DG["jogo_em_curso"]=True
        return(f'Jogo iniciado entre {DG["jogadores_em_jogo"][0]} e {DG["jogadores_em_jogo"][1]}.')
    else:
        return("Jogadores não registados.")
     