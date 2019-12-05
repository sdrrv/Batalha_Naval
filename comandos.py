#-------------------------------------------------------------------------------
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


def Existe_Jogador(nome):
    if nome in DG["jogadores"].keys():
        return True
    return False
    

def Registar_Jogadores(nome):        #Adiciona o jogador ao dicionário 
    DG["jogadores"][nome]={
        "vitorias":0,
        "Jogos":0,
        }
    pass

def existe_jogador_em_jogo(nome):
    for jogador in DG["jogadores_em_jogo"]:
        if jogador==nome:
            return True
    return False
    pass

def Remover_Jogadores(nome):          #Retira o jogador do dicionário 
    del DG["jogadores"][nome]
    pass

def sort_jogadores():
    return sorted(DG["jogadores"].keys())

def Listar_Jogadores():
    if sort_jogadores():
        for i in sort_jogadores():
            print( i, DG["jogadores"][i]["Jogos"], DG["jogadores"][i]["vitorias"])
    else:
        print("Não existem jogadores registados.")
    pass              

def Iniciar_Jogo(nome1,nome2):
    if DG["jogo_em_curso"]==True:
        print("Existe um jogo em curso.")

    elif Existe_Jogador(nome1) and Existe_Jogador(nome2):
        DG["jogadores_em_jogo"]=sorted([nome1,nome2])
        print(f'Jogo iniciado entre {DG["jogadores_em_jogo"][0]} e {DG["jogadores_em_jogo"][1]}.')
        DG["jogo_em_curso"]=True
    else:
        print("Jogadores não registados.")
    pass 