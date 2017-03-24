import Codigo_Principal
def salvar_escore(escore):
    nome_de_jogador = input("Digite seu nome de Usuario par salvar seu escore: ")
    arquivo = open("nome.txt", "r")
    x = 0
    for linha in arquivo.readline():
     nomes = linha.split(";")
     if nomes[0] == nome_de_jogador:
      
                    arquivo2 = open("nome.txt","a")
                    arquivo2.write(";")
                    arquivo2.write(escore)
                    arquivo2.close()
                    arquivo.close()

    if x == 0:
               print("Não existe nenhum usuario com esse nome")
               arquivo.close()
               salvar_escore()
    else:
    	Codigo_Principal.Jogo()





