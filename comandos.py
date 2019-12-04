
jogadores_no_jogo=[]

#-------------------------------------------------------------------------------

jogadores={
#    "jogador1":{
#        "vitórias":0,
#        "jogos_jogados":0,
#    }
}
def Existe_Jogador(nome):
    if nome in jogadores.keys():
        return True
    return False
    

def Registar_Jogadores(nome):        #Adiciona o jogador ao dicionário 
    jogadores[nome]={
        "vitorias":0,
        "Jogos":0,
        }
    pass

def jogador_em_jogo(nome):
    for jogador in jogadores_no_jogo:
        if jogador==nome:
            return True
    return False
    pass

def Remover_Jogadores(nome):          #Retira o jogador do dicionário 
    del jogadores[nome]
    pass

def sort_jogadores():
    return sorted(jogadores.keys())

def Listar_Jogadores():
    if sort_jogadores():
        for i in sort_jogadores():
            print( i, jogadores[i]["Jogos"], jogadores[i]["vitorias"])
    else:
        print("Não existem jogadores registados.")
    pass              

def Iniciar_Jogo(nome1,nome2,jogo_em_curso):
    global jogadores_no_jogo
    if jogo_em_curso==True:
        print("Existe um jogo em curso.")
    elif Existe_Jogador(nome1) and Existe_Jogador(nome2):
        jogadores_no_jogo=sorted([nome1,nome2])
        print(f'Jogo iniciado entre {jogadores_no_jogo[0]} e {jogadores_no_jogo[1]}.')
    else:
        print("Jogadores não registados.")
    pass 