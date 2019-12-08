import comandos as cm

def consola(): #Consola
    DG=cm.DG
    #-----------------------------------------------

    line=input()
    command=line.split()

    if not line: # Sai do programa se o input for Nulo ou seja inexistente
        exit(0)


    if command[0]=="RJ":
        if len(command)!=2:
            print("Instrução inválida.")
        elif not cm.Existe_Jogador(DG,command[1]):                
            cm.Registar_Jogadores(DG,command[1])
            print("Jogador registado com sucesso.")
        else:
            print("Jogador existente.")
 
    elif command[0] == "EJ":
        if len(command)!=2:
            print("Instrução inválida.")
            
        elif cm.existe_jogador_em_jogo(DG,command[1]):
            print("Jogador participa no jogo em curso.")

        elif  cm.Existe_Jogador(DG,command[1]) and not cm.existe_jogador_em_jogo(DG,command[1]):
            cm.Remover_Jogadores(DG,command[1])
            print('Jogador removido com sucesso.')
        else:
            print('Jogador não existente.')
    
    elif command[0]=="LJ":
        if len(command)!=1:
            print("Instrução inválida.")
        elif cm.sort_jogadores(DG):
            Lista=cm.Listar_Jogadores(DG)
            for jogador in Lista:
                print( jogador, DG["jogadores"][jogador]["Jogos"], DG["jogadores"][jogador]["vitorias"])
        else:
            print("Não existem jogadores registados.")

    elif command[0] == 'IJ':
        if len(command)!=3:
            print("Instrução inválida.")        
        else:
            print(cm.Iniciar_Jogo(DG,command[1],command[2]))
    
    elif command[0] == "print":
        if len(command)!=2:
            print("Instrução invalida.")

        else:
            #cm.print_tabuleiro(cm.DG["jogadores_em_jogo"][list ( cm.DG["jogadores_em_jogo"].keys() ) [ int(command[1]) ] ] ["tabuleiro"] )
            print(cm.DG["jogadores_em_jogo"][list ( cm.DG["jogadores_em_jogo"].keys() ) [ int(command[1]) ] ] ["Frota"])
    
    elif command[0] == 'CN':
        if len(command) != 5:
            print('Instrução inválida')   
            



    else:
        print("Instrução inválida.")
    
    

#-----------------------------------------------------------------------


if __name__ == "__main__":
    while True:
        consola()