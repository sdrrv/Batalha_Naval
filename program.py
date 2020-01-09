import comandos as cm
#----------------------------------------------------------------------------------------------------------
def consola(): #Consola
    orientacoes=["N","S","E","O"]
    DG=cm.Dicionario_Geral()
    #-----------------------------------------------
    while True:
        line=input()
        command=line.split()

        if not line: # Sai do programa se o input for Nulo ou seja inexistente
            exit(0)

        elif command[0]=="RJ":
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
        
        elif command[0] == "print": #DEBUGING COMMAND
            if len(command)!=2:
                print("Instrução inválida.")
            else:
                cm.print_tabuleiro(DG["jogadores_em_jogo"][list ( DG["jogadores_em_jogo"].keys() ) [ int(command[1]) ] ] ["tabuleiro"] )
                print(DG["jogadores_em_jogo"][list ( DG["jogadores_em_jogo"].keys() ) [ int(command[1]) ] ] ["Frota"])
        
        elif command[0] == 'CN':
            if command[2]=="L" and len(command)==5:
                print(cm.Colocar_Navios(DG,command[1],command[2],int(command[3]),command[4]))
            elif len(command)==6:
                print(cm.Colocar_Navios(DG,command[1],command[2],int(command[3]),command[4],command[5]))
            elif not 1 <= int(command[3]) <= 10 or not "A"<=command[4]<="J" or command[5] not in orientacoes:
                print('Instrução inválida.')
        
        elif command[0] == 'RN':
            if len(command)!=4 or not 1 <= int(command[2]) <= 10 or not "A"<=command[3]<="J":
                print('Instrução inválida.')
            elif DG['jogo_em_curso'] == False:
                print('Não existe jogo em curso.')
            elif not cm.existe_jogador_em_jogo(DG,command[1]):
                print('Jogador não participa no jogo em curso.')
            elif DG["jogadores_em_jogo"][command[1]]["tabuleiro"][int(command[2])-1][cm.translator(command [3])] == 0 :
                print('Não existe navio na posição.')
            else:
                cm.Removido(DG,command[1], int(command[2]), command[3] )
                cm.Remover_Navios(DG,command[1], int(command[2]), command[3] )
                print("Navio removido com sucesso.")
        
        elif command[0] == 'D':
            if len(command)!=2 and len(command)!=3:
                print('Instrução inválida.')
            elif DG['jogo_em_curso'] == False:
                print('Não existe jogo em curso.')
            elif not cm.existe_jogador_em_jogo(DG,command[1]):
                print('Jogador não participa no jogo em curso.')
            elif len(command) == 2:
                cm.Desistir(DG,command[1])
                print("Desistência com sucesso. Jogo terminado.")

            elif len(command) == 3:
                cm.Desistir(DG,command[1],command[2])
                print("Desistência com sucesso. Jogo terminado.")

        elif command[0] == 'T':
            if len(command)!=4:
                print('Instrução inválida.')
            elif not DG['jogo_em_curso']:
                print('Não existe jogo em curso.')
            elif not 1 <= int(command[2]) <= 10 or not "A"<=command[3]<="J":
                print("Posição irregular.")
            elif not DG["combate_em_curso"]:
                print("Jogo em curso sem combate iniciado.")
            elif not cm.existe_jogador_em_jogo(DG,command[1]):
                print('Jogador não participa no jogo em curso.')
            elif DG["Ronda"]=="":
                DG["Ronda"]=command[1]
                print(cm.Tiro(DG,command[1],int(command[2]),command[3]))
            else:
                if DG["Ronda"]!= command[1]:
                    DG["Ronda"]=command[1]
                    print(cm.Tiro(DG,command[1],int(command[2]),command[3]))
                else:
                    print("Não é a tua vez.")
 
        elif command[0] == 'IC':
            if len(command) != 1:
                print('Instrução inválida.')
            else: 
                print(cm.Iniciar_combate(DG))

        elif command[0] == 'V':
            if len(command) != 1:
                print('Instrução inválida.')
            elif not DG['jogo_em_curso']:
                print('Não existe jogo em curso.')
            elif not DG["combate_em_curso"]:
                print("Jogo em curso sem combate iniciado.")
            else:
                result=cm.Visualizar_Resultado(DG)
                print(str(result[0]))
                print(str(result[1]))

        elif command[0] == 'G':
            if len(command) != 1:
                print('Instrução inválida.') 
            else:
                print(cm.Gravar(DG))

        elif command[0] == 'L':
            if len(command) != 1:
                print('Instrução inválida') 
            else:
                DG=cm.Ler()
                print("Jogo carregado.")

        else:
            print("Instrução inválida.")
#-----------------------------------------------------------------------
if __name__ == "__main__":
    consola() 