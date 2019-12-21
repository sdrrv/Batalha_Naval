#----------------------------------Imports---------------------------------------
import pickle
#--------------------------------------------------------------------------------
def Dicionario_Geral():
    return {
    "jogadores":{
    #    "jogador1":{
    #        "vitorias":0,
    #        "Jogos":0,
    #    }
    },

    "jogo_em_curso":False,
    "combate_em_curso":False,
    "Ronda":"",
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
        },

        "S":{
            "nome":"Submarino",
            "tamanho": 2,
        },

        "F":{
            "nome":"Fragata",
            "tamanho":3,
        },

        "C":{
            "nome":"Cruzador",
            "tamanho": 4,
        },
        
        "P":{
            "codigo":"Porta Avioes",
            "tamanho": 5,
        }

    }
}
#--------------------------------------------------------------------------------

def Existe_Jogador(DG,nome):            #Função que verifica se existe um jogador
    if nome in DG["jogadores"].keys():
        return True
    return False
    

def Registar_Jogadores(DG,nome):        #Adiciona o jogador ao dicionário 
    DG["jogadores"][nome]={
        "vitorias":0,
        "Jogos":0,
        }
    return DG


def existe_jogador_em_jogo(DG, nome):              # Função que verifica se existe um jogador em jogo 
    for jogador in DG["jogadores_em_jogo"].keys():
        if jogador==nome:
            return True
    return False
    

def Remover_Jogadores(DG, nome):          #Retira o jogador do dicionário.
    del DG["jogadores"][nome]
    

def sort_jogadores(DG):                     # Ordena os jogadores por ordem alfabética
    return sorted(DG["jogadores"].keys())

def Listar_Jogadores(DG):                    #Lista os jogadores que foram introduizods pelo comando "IJ" por ordem alfabética
    Lista=[]
    for i in sort_jogadores(DG):
        Lista.append(i)
    return Lista
                  

def Iniciar_Jogo(DG,nome1,nome2):             #Inicia o jogo com os dois jogadores introduzidos. Criamos também um tabuleiro, classificação e frota para cada jogador.
    if DG["jogo_em_curso"]==True:
        return("Existe um jogo em curso.")

    elif Existe_Jogador(DG, nome1) and Existe_Jogador(DG, nome2):
        lista_sort=sorted([nome1,nome2])
        DG["jogo_em_curso"]=True
        for jogador in lista_sort:
            #----------------------Criar Tabuleiros-------------------------------------------------------
            DG["jogadores_em_jogo"][jogador]={"tabuleiro":[[0 for _ in range(0,10)] for _ in range(0,10)]}
            #----------------------Criar Classificaçao----------------------------------------------------
            DG["jogadores_em_jogo"][jogador]["Tiros"]=0
            DG["jogadores_em_jogo"][jogador]["Tiros_em_navios"]=[]
            DG["jogadores_em_jogo"][jogador]["Navios_afundados"]=0
            #-------------------------Criar Frota------------------
            DG["jogadores_em_jogo"][jogador]["Frota"]={
                "L":{
                    "quantidade":4,
                    "navios_em_jogo":4,
                    "contador":0,
                    "Frota_em_jogo":{ # Frota deum tipo especifico que se encontra em jogo. cada barco tem um id único proveniente do contador, que aumenta 1 apos cada colocação.
                        #"L1":1,
                        #"L2":1,
                        #"L3":1,
                        #"L4":1
                    }
                },

                "S":{
                    'quantidade':3,
                    "navios_em_jogo":3,
                    "contador":0,
                    "Frota_em_jogo":{
                        
                    }
                },

                "F":{
                    "quantidade":2,
                    "navios_em_jogo":2,
                    "contador":0,
                    "Frota_em_jogo":{
                        
                    }
                },

                "C":{
                    'quantidade':1,
                    "navios_em_jogo":1,
                    "contador":0,
                    "Frota_em_jogo":{

                    }

                },
        
                "P":{
                    'quantidade':1,
                    "navios_em_jogo":1,
                    "contador":0,
                    "Frota_em_jogo": {
                        
                    }
                }
            }    
        return(f'Jogo iniciado entre {lista_sort[0]} e {lista_sort[1]}.')
    else:
        return("Jogadores não registados.")

def print_tabuleiro(tabuleiro): #Para DEBUG! Não para avaliar. Sabemos que contem prints. :P
    Letras=["   A","B","C","D","E","F","G","H","I","J"]
    for letra in range(0,len(Letras)):
        print(f"{Letras[letra]:<3}\t", end="")
    print()
    for linha in range(0, len(tabuleiro)):
        print(f"{(linha+1):<2}", end=" ")
        for coluna in range(0,len(tabuleiro)):
            print(f"{tabuleiro[linha][coluna]}\t", end="")
        print()

def translator(letra):                      #Traduz uma letra para uma posição index da lista.
    return ord(letra)-65

def bloco(DG,nome,linha,coluna): #verifica se o jogador pode ou não colocar o navio no espaco de jogo, já delimitado pela funçao verificar_posiçao_em_tabuleiro
    a=[[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,-1],[1,1],[-1,1]]
    permite=True
    result=[]
    tabuleiro=DG["jogadores_em_jogo"][nome]["tabuleiro"]
    posiçao=[linha,coluna]
    for i in a:
        if not posiçao[0]+i[0]<0 and not posiçao[0]+i[0]>9 and not posiçao[1]+i[1]<0 and not posiçao[1]+i[1]>9:
            if tabuleiro[posiçao[0]+i[0]] [posiçao[1]+i[1]]!=0:
                permite=False
                result.append([posiçao[0]+i[0],posiçao[1]+i[1]])
    result.insert(0,permite)
    return result

def verificar_posiçao_em_tabuleiro(DG,tipo,linha,coluna,orientacao,nome): #Verifica se o navio esta colocado dentro do campo de jogo.
    tamanho=DG["Frota"][tipo]["tamanho"]
    permite=True
    posiçao=[linha-1,translator(coluna)]

    for i in range(0,tamanho):               #Delimita o espaço de jogo.
        if orientacao=="O" or orientacao=="não_tem":
            if posiçao[1]-i <0 or not bloco(DG,nome,posiçao[0],posiçao[1]-i)[0]:
                permite=False
        elif orientacao=="E":
            if posiçao[1]+i >9 or not bloco(DG,nome,posiçao[0],posiçao[1]+i)[0]:
                permite=False
        elif orientacao=="S":
            if posiçao[0]+i >9 or not bloco(DG,nome,posiçao[0]+i,posiçao[1])[0]:
                permite=False
        elif orientacao=="N":
            if posiçao[0]-i <0 or not bloco(DG,nome,posiçao[0]-i,posiçao[1])[0]:
                permite=False

    return permite

def Colocar_Navios(DG,nome,tipo,linha,coluna,orientaçao="não_tem"): #Coloca navios no tabuleiro do jogador indicado
    if not DG["jogo_em_curso"]:
        return("Não existe um jogo em curso.")
    elif tipo!="L" and orientaçao=="não_tem":
        return('Instrução inválida')
    elif existe_jogador_em_jogo(DG,nome):
        tabuleiro=DG["jogadores_em_jogo"][nome]["tabuleiro"]
        tamanho=DG["Frota"][tipo]["tamanho"]
        posiçao=[linha-1,translator(coluna)]
        if verificar_posiçao_em_tabuleiro(DG,tipo,linha,coluna,orientaçao,nome):
            if DG["jogadores_em_jogo"][nome]["Frota"][tipo]["quantidade"]>0:
                DG["jogadores_em_jogo"][nome]["Frota"][tipo]["quantidade"]-=1
                contador=DG["jogadores_em_jogo"][nome]["Frota"][tipo]["contador"] # o contador permite criar um barco com um id unico, sempre que se o coloca.
                DG["jogadores_em_jogo"][nome]["Frota"][tipo]["Frota_em_jogo"][f"{tipo}{contador}"]=tamanho #Adicina o numero de navios ao tipo
                for i in range(0,tamanho): #Coloca os navios.
                    if orientaçao=="O" or orientaçao=="não_tem":
                        tabuleiro[posiçao[0]] [posiçao[1]-i]=(f"{tipo}{contador}")
                    elif orientaçao=="E":
                        tabuleiro[posiçao[0]] [posiçao[1]+i]=(f"{tipo}{contador}")
                    elif orientaçao=="S":
                        tabuleiro[posiçao[0]+i] [posiçao[1]]=(f"{tipo}{contador}")
                    elif orientaçao=="N":
                        tabuleiro[posiçao[0]-i] [posiçao[1]]=(f"{tipo}{contador}")
                DG["jogadores_em_jogo"][nome]["Frota"][tipo]["contador"]+=1
                return("Navio colocado com sucesso.")
            else:
                return('Não tem mais navios dessa tipologia disponíveis.')
        else:
            return ("Posição irregular.")
    else:
        return("Jogador não participa no jogo em curso.")

def Remover_Navios(DG,nome,linha,coluna): #Remove os navios por recurção 
    posiçao=[linha-1,translator(coluna)]
    tabuleiro=DG["jogadores_em_jogo"][nome]["tabuleiro"]
    result=(bloco(DG,nome,posiçao[0],posiçao[1])) # Retorna falso, e a posiçao dos navios em questão
    tabuleiro [posiçao[0]] [posiçao[1]] = 0
    if not result[0]:
        del(result[0]) #deleta o estatudo True or False
        for i in result:
            Remover_Navios(DG,nome,i[0]+1,chr(i[1]+65))
    
def Removido(DG,nome,linha,coluna): # Subtrai e adiciona dos dicinarios a quantidade e caracteristicas dos navios. (Quando Removidos)
    posiçao=[linha-1,translator(coluna)]
    tabuleiro=DG["jogadores_em_jogo"][nome]["tabuleiro"]
    result=(bloco(DG,nome,posiçao[0],posiçao[1]))
    tipo=tabuleiro [posiçao[0]] [posiçao[1]]
    tipo_base=(list(tipo))[0]
    DG["jogadores_em_jogo"][nome]["Frota"][tipo_base]["quantidade"]+=1
    del(DG["jogadores_em_jogo"][nome]["Frota"][tipo_base]["Frota_em_jogo"][tipo])

def Desistir(DG,nome1,nome2="não_tem"):           #FF aos 15    
    if nome2 != "não_tem":
        for jogador in DG["jogadores_em_jogo"].keys():
            DG["jogadores"][jogador]["Jogos"]+=1
    else:                                                   
        DG["jogadores"][nome1]["Jogos"]+=1
        for jogador in DG["jogadores_em_jogo"].keys():
            if jogador!= nome1:
                DG["jogadores"][jogador]["Jogos"]+=1                            
                DG["jogadores"][jogador]["vitorias"]+=1
    #-------------------Reset-do-tabuleiro-------------------------------            
    DG["jogadores_em_jogo"].clear()
    DG["jogo_em_curso"]=False
    DG["combate_em_curso"]=False
    DG["Ronda"]=""

def Iniciar_combate(DG):                                    #Inicia o combate quanto todos os navios tiverem colocados 
    if DG["jogo_em_curso"]==False:
        return("Não existe jogo em curso.")
    else:
        for jogador in DG["jogadores_em_jogo"]:
            for tipo in DG["jogadores_em_jogo"][jogador]["Frota"]:
                    if DG["jogadores_em_jogo"][jogador]["Frota"][tipo]["quantidade"]!=0:
                        return("Navios não colocados.")
    DG["combate_em_curso"]=True
    return("Combate iniciado.")

def Tiro(DG,nome,linha,coluna): #Dá tiros no tabuleiro do adversario do jogador indicado.
    posiçao=[linha-1,translator(coluna)]
    DG["jogadores_em_jogo"][nome]["Tiros"]+=1

    for jogador in DG["jogadores_em_jogo"]:
        if jogador != nome:
            nome_adversario=jogador
    tabuleiro=DG["jogadores_em_jogo"][nome_adversario]["tabuleiro"]
    #---------------------------------Se-Falhar------------------------------------
    if tabuleiro[posiçao[0]][posiçao[1]] == 0:
        return "Tiro na água."
    #---------------------------------Se-Acertar------------------------------------
    else:
        tipo=tabuleiro [posiçao[0]] [posiçao[1]]
        tipo_base=(list(tipo))[0]
        if posiçao in DG["jogadores_em_jogo"][nome]["Tiros_em_navios"]:
            if DG["jogadores_em_jogo"][nome_adversario]["Frota"][tipo_base]["Frota_em_jogo"][tipo]==0:
                return(f"Navio {tipo_base} afundado.")
            else:
                return("Tiro em navio.")
        else:
            DG["jogadores_em_jogo"][nome_adversario]["Frota"][tipo_base]["Frota_em_jogo"][tipo]-=1
            DG["jogadores_em_jogo"][nome]["Tiros_em_navios"].append(posiçao)
            if DG["jogadores_em_jogo"][nome_adversario]["Frota"][tipo_base]["Frota_em_jogo"][tipo]==0:
                DG["jogadores_em_jogo"][nome_adversario]["Frota"][tipo_base]["navios_em_jogo"]-=1
                DG["jogadores_em_jogo"][nome]["Navios_afundados"]+=1
                contador=0
                for tipo_bases in DG["jogadores_em_jogo"][nome_adversario]["Frota"]:
                    if DG["jogadores_em_jogo"][nome_adversario]["Frota"][tipo_bases]["navios_em_jogo"]==0:
                        contador+=1
                if contador!=5:
                    return(f"Navio {tipo_base} afundado.")
                else:
                    Desistir(DG,nome_adversario)
                    return(f"Navio {tipo_base} afundado. Jogo terminado.")
            return("Tiro em navio.")

def Visualizar_Resultado(DG):   
    result=[]
    jogo=DG["jogadores_em_jogo"]
    for jogador_em_jogo in DG["jogadores_em_jogo"]:
        i=str(jogador_em_jogo)+" "+str(jogo[jogador_em_jogo]["Tiros"])+" "+str(len(jogo[jogador_em_jogo]["Tiros_em_navios"]))+" "+str(jogo[jogador_em_jogo]["Navios_afundados"])
        result.append(i)
    return result

def Gravar(DG):
    with open ('save.txt', 'wb') as f: 
        pickle.dump(DG,f)
    return ("Jogo gravado.")

def Ler():
    DG=None
    with open ('save.txt', 'rb') as f:
        DG = pickle.load(f)
    return DG