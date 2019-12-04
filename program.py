import comandos as cm

jogo_em_curso=False #global variable

def consola(): #Consola
    line=input()
    command=line.split()

    if not line: # Sai do programa se o input for Nulo ou seja inexistente
        exit(0)


    if command[0]=="RJ":
        if len(command)!=2:
            print("Instrução inválida.")
        elif not cm.Existe_Jogador(command[1]):                
            cm.Registar_Jogadores(command[1])
            print("Jogador registado com sucesso.")
        else:
            print("Jogador existente.")
 
    elif command[0] == "EJ":
        if len(command)!=2:
            print("Instrução inválida.")
        elif cm.jogador_em_jogo(command[1]):
            print("Jogador participa no jogo em curso.")
        elif  cm.Existe_Jogador(command[1]) and not cm.jogador_em_jogo(command[1]):
            cm.Remover_Jogadores(command[1])
            print('Jogador removido com sucesso.')
        else:
            print('Jogador não existente.')
    
    elif command[0]=="LJ":
        if len(command)!=1:
            print("Instrução inválida.")
        else:
            cm.Listar_Jogadores()

    elif command[0] == 'IJ':
        if len(command)!=3:
            print("Instrução inválida.")
        else:
            global jogo_em_curso
            cm.Iniciar_Jogo(command[1],command[2],jogo_em_curso)
            jogo_em_curso=True
        


    
    else:
        print("Instrução inválida.")
        

#-----------------------------------------------------------------------


if __name__ == "__main__":
    while True:
        consola()