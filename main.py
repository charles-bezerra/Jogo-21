import random
import ale
import sys
import time
def login():  # Função login
    j = 0
    while j == 0:
        pergun = input("Você já possui conta: ")  # aqui receber o valor se vc já possui cadastro
        if pergun == "sim" or pergun == "s" or pergun == "Sim" or pergun == "S":  # se sim vc entra na funçao que verifica se sua conta existe
            j = 1
            def entrar():
                print("""___________________________________________________________________
                        """)
                nome = input("Digite seu nome de usuario: ")
                senha = input("Digite sua senha: ")
                print("___________________________________________________________________")
                arquivo_nome = open("nome.txt",
                                    "r")  # estou abrindo o arquivo que estão quardados os dados dos cadastros
                permicao_nome = 0
                permicao_senha = 0
                i = 0
                for i in arquivo_nome.readlines():  # esse for verifica o arquivo e i recebe os valores de linha a linha
                    dados = i.split(
                        ";")  # a funçao split transforma i linha em um vetor, nesse caso com duas posições que ';' vai ser o ponto que separa os elementos apos ele em outro indice               if nome == dados[0].rstrip() and senha == dados[1].rstrip():
                    if dados[0].rstrip() == nome and dados[1].rstrip() == senha:
                        permicao_nome = 1
                        permicao_senha = 1
                        break
                arquivo_nome.close()
                if permicao_nome == 1 and permicao_senha == 1:
                    Jogo()
                else:
                    try:
                        print("Esqueceu sua senha?!")
                        print("")
                        print("")
                        print("")

                        resp = input("Deseja sair(sair) ou continuar(continuar)? ")
                        if resp == "continuar" or resp == "Continuar" or resp == "cont" or resp == "Cont":

                            x = login()

                        elif resp == "sair" or resp == "Sair":
                            print("Fechou")
                    except ValueError:
                        print(
                            """ Algum dado que você inseriu ocasionou gerou um error, reiniciaremos o procedimento!""")
                        login()
                    except TypeError:
                        print(
                            """ Algum dado que você inseriu ocasionou gerou um error, reiniciaremos o procedimento!""")
                        login()
                    except:
                        print(
                            """ Algum dado que você inseriu ocasionou gerou um error, reiniciaremos o procedimento!""")
                        login()

            x = entrar()
        elif pergun == "nao" or pergun == "não" or pergun == "n" or pergun == "N" or pergun == "Nao":
            j = 1
            def cadastra():
                print("___________________________")
                nome = input("Digite seu nome de usuario: ")
                senha = input("Digite para ser sua senha: ")
                senha_confirmacao = input("Confirme sua senha: ")
                print("___________________________")
                nome_usurio_existentes = open("nome.txt", "r")
                verificaçao_de_existencia = 0
                for i in nome_usurio_existentes.readlines():
                    dados = i.split(";")
                    if nome == dados[0].rstrip():
                        verificaçao_de_existencia = 1
                nome_usurio_existentes.close()
                if verificaçao_de_existencia != 1:
                    if senha == senha_confirmacao:
                        arquivo_nome = open("nome.txt", "a")
                        arquivo_nome.write(nome)
                        arquivo_nome.write(";")
                        arquivo_nome.write(senha)
                        arquivo_nome.write("\n")

                        arquivo_nome.close()
                        print("Cadastrado com sucesso!!")

                        Jogo()
                    else:
                        print("")
                        print("!!!Algo deu errado faça novamente!!!")
                        x = cadastra()

                elif verificaçao_de_existencia == 1:
                    print("Esse nome de usuario já existe, tente novamente com outro nome.")
                    x = cadastra()

            x = cadastra()
        else:
            print("Esse comando não existe, responda com sim ou nao")
            j = 0
def menu():
    print("")
    print("")
    print("")
    print("""
                                     Menu:
                                    
   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
   $                                                                        $
   $        __              1 - Iniciar jogo                  ______        $
   $       (__)                                              (______)       $
   $      (____)            2 - Instrucoes                   (______)       $ 
   $    (________)                                        (____________)    $ 
   $   (__________)         3 - Ranking                    (__________)     $
   $  (____________)                                        (________)      $
   $     (______)           4 - Tabela De Conversao           (____)        $
   $     (______)                                              (__)         $
   $                        5 - Sair                                        $
   $                                                                        $
   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
""")
    op = int(input("Digite sua opção: "))
    return op

def Instrucoes ():
    print("")
    print("")
    print("")
    print("")
    print(chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),"Regras",chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226))
    print("""
______________________________________________________
|                                                    |
|    * BlackJack ou 21: e um jogo de cartas em       |
|      que o objetivo e jogar contra a mesa ou       |
|      Tambem Chamado Dealer as regras são           |
|      muito simples:                                |
|                                                    |
|   * No comeco do Jogo o Dealer vai puxar as        |
|      cartas ate que estejam o mais proximas        |
|      possiveis de 21                               |
|                                                    |
|   * Depois disso o Jogador que vai jogar tentara   |
|      ultrapassar o numero do Dealer porem sem      |
|      passar de 21 pois caso isso aconteca e        |
|      derrota automatica                            |
|                                                    |
|   * Caso o Jogador consiga ultrapassar o Dealer    |
|      sem passar de 21 ele ganha mas caso ele não   |
|      passe o Dealer ou caso ele ultrapasse os      |
|      21 ele perde                                  |
|                                                    |
|                                                    |
|   $$$$$$$$$$$$$$$$  Controles  $$$$$$$$$$$$$$$$$$$ |
|    ______________________________________________  |
|   |                                              | |
|   | 1. Todas as perguntas (Exeto o seu nome)     | |
|   | podem e devem ser respondidas com sim, nao   | |
|   | e seus derivados                             | |
|   |                                              | |
|   | 2. Para perguntas de multipla escolha        | |
|   | responde sempre com numeros                  | |
|   |______________________________________________| |
|                                                    |
|   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ |
|____________________________________________________|
""")
    print( chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),chr(7226),)
    
def Tabela():
    print("")
    print("")
    print("")
    print(chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898))
    print(chr(2898),"A (as)      -------------- 1 ",chr(2898))
    print(chr(2898),"2 (Dois)    -------------- 2 ",chr(2898))
    print(chr(2898),"3 (Tres)    -------------- 3 ",chr(2898))
    print(chr(2898),"4 (Quatro)  -------------- 4 ",chr(2898))
    print(chr(2898),"5 (Cinco)   -------------- 5 ",chr(2898))
    print(chr(2898),"6 (Seis)    -------------- 6 ",chr(2898))
    print(chr(2898),"7 (Sete)    -------------- 7 ",chr(2898))
    print(chr(2898),"8 (Oito)    -------------- 8 ",chr(2898))
    print(chr(2898),"9 (Nove)    -------------- 9 ",chr(2898))
    print(chr(2898),"10(Dez)     -------------- 10",chr(2898))
    print(chr(2898),"J (Valete)  -------------- 11",chr(2898))
    print(chr(2898),"Q (Dama)    -------------- 12",chr(2898))
    print(chr(2898),"K (Rei)     -------------- 13",chr(2898))
    print(chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898),chr(2898))
#Funcao Para Imprimir
def imprimir (x , y):

    for i in range(13):

        for j in range(8):

            if(x[i][j] == 1):
                print(chr(7226),end =" ")
            elif(x[i][j] == 2):
                print(chr(y),end =" ")
            else:
                print(" ",end=" ")
        print("")
###
#limpar tela
def limpar():
    print("\n" * 130)
def Dealer ():
    Banca = [0,0]
    vez = 0
    for i in range (15):
        x = random.choice("A234567890JQK")
        vez = vez + 1
        carta1 = 0
        if (x == "2"):
            x = 2
        if (x == "3"):
            x = 3
        if (x == "4"):
            x = 4        
        if (x == "5"):
            x = 5
        if (x == "6"):
            x = 6
        if (x == "7"):
            x = 7
        if (x == "8"):
            x = 8        
        if (x == "9"):
            x = 9
        if (x == "0"):
            x = 10
        if (x == "A"):
            x = 1
        if (x == "J"):
            x = 11
        if (x == "Q"):
            x = 12        
        if (x == "K"):
            x = 13           
        Banca[0] = Banca[0] + x
        if(i == 0):
            if(x == 1):
                Banca[1] = "A"
            elif(x == 11):
                Banca[1] = "J"
            elif(x == 12):
                Banca[1] = "Q"
            elif(x == 13):
                Banca[1] = "K"
            else:
                Banca[1] = x
        if(Banca[0] > 17):
            return Banca
            break
def fim_de_jogo():
                    print("""
____________________________________________________________________________________________________________________________________________


                      |||||||    |||||   ||||      ||||  ||||||||            |||||||   |||         |||  ||||||||  ||||||||
                      |||      |||   ||| ||| ||  || |||  |||               |||     |||  |||       |||   |||       |||   |||             
                      |||      |||   ||| |||  ||||  |||  |||               |||     |||   |||     |||    |||       |||   |||
                      |||      ||||||||| |||   ||   |||  ||||||||          |||     |||    |||   |||     ||||||||  ||||||||           
                      ||| |||  |||   ||| |||        |||  |||               |||     |||     ||| |||      |||       |||  |||
                      |||  ||  |||   ||| |||        |||  |||               |||     |||      |||||       |||       |||   |||
                      |||||||  |||   ||| |||        |||  ||||||||            |||||||         |||        ||||||||  |||    |||


____________________________________________________________________________________________________________________________________________

""")
                    x = 0
                    while x != 1:
                
                                resposta = input("Você deseja voltar ao menu principal? ")
                                if resposta == "sim" or resposta == "s" or resposta == "Sim":                     
                                    Jogo()
                                    x = 1
                                elif resposta == "nao" or resposta == "Nao" or resposta == "n" or resposta == "N":
                                    print("Fechou")
                                    x = 1
                                else:
                                    print("Error, digite novamente")
                                    print("")
def inf(i=0, cont=1):
    while True:
        yield i
        i+=cont
def Jogo ():
    opçao = menu()
    escore = 0
    if opçao != 5:
        if opçao == 2:
            Instrucoes()
            print("""
                """)
            resp = input ("Deseja Voltar Para o Menu?: ")
            for i in range (60):
                if(resp == "sim" or resp == "s"):
                    Jogo()
                    break
                elif(resp == "nao" or resp == "n" or resp == "não"):
                    break
                else:
                    print("""


                        """)
                    resp = input("Responda Com sim,s ou nao(não),n: ")


        elif opçao == 4:
            Tabela()
            print("""



                """)
            resp = input("Deseja Voltar Para o Menu?: ")
            
            for i in range (60):
                if(resp == "sim" or resp == "s"):
                    Jogo()
                    break
                elif(resp == "nao" or resp == "n" or resp == "não"):
                    break
                else:
                    print("")
                    print("")
                    print("")
                    resp = input("Responda Com sim,s ou nao(não),n: ")
        elif opçao == 3:

            print("....................Ranking....................")

            arquivo = open("nome.txt", "r")
            print("_______________________Ranking_______________________")
          
            
            resp = input("Deseja Voltar Para o Menu?: ")
            for i in range (60):
                if(resp == "sim" or resp == "s"):
                    Jogo()
                    break
                elif(resp == "nao" or resp == "n" or resp == "não"):
                    break
                else:
                    resp = input("Responda Com sim,s ou nao(não),n: ")

        elif opçao == 1:

                print("""
  ______________________________________________________________
 
                          INICIANDO JOGO
  ______________________________________________________________




                    """)
                escore = 0
                def jogando(escore):

                          carta = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                          pontos = 0
                          posicao = -1                                                                                  
                          x = [1,2,3,4,5,6,7,8,9,10,11,12,13]

                          x[0]=                                  [[1,1,1,1,1,1,1,1],
                                                                  [1,0,0,0,0,0,2,1],
                                                                  [1,0,0,1,1,0,0,1],
                                                                  [1,0,1,0,0,1,0,1],
                                                                  [1,0,1,0,0,1,0,1],
                                                                  [1,0,1,1,1,1,0,1],
                                                                  [1,0,1,0,0,1,0,1],
                                                                  [1,0,1,0,0,1,0,1],
                                                                  [1,0,0,0,0,0,0,1],
                                                                  [1,0,0,0,0,0,0,1],
                                                                  [1,0,2,0,0,0,0,1],
                                                                  [1,0,0,0,0,0,0,1],
                                                                  [1,1,1,1,1,1,1,1]]
                          
                          x[1]=                                      [[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,0,0,1],
                                                                      [1,0,1,0,0,0,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[2]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[3]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[4]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,0,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[5]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,0,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[6]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[7]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[8]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[9]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,1,1,1,0,1,0,1],
                                                                      [1,0,1,1,0,1,0,1],
                                                                      [1,0,1,1,0,1,0,1],
                                                                      [1,0,1,1,0,1,0,1],
                                                                      [1,1,1,1,1,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[10]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,1,0,0,1],
                                                                      [1,0,0,0,1,0,0,1],
                                                                      [1,0,0,0,1,0,0,1],
                                                                      [1,0,1,0,1,0,0,1],
                                                                      [1,0,1,1,1,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[11]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,1,1,0,1],
                                                                      [1,0,1,1,1,1,0,1],
                                                                      [1,0,0,0,1,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]
                          x[12]=[[1,1,1,1,1,1,1,1],
                                                                      [1,0,0,0,0,0,2,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,1,0,1,0,0,1],
                                                                      [1,0,1,1,0,0,0,1],
                                                                      [1,0,1,1,0,0,0,1],
                                                                      [1,0,1,0,1,0,0,1],
                                                                      [1,0,1,0,0,1,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,0,2,0,0,0,0,1],
                                                                      [1,0,0,0,0,0,0,1],
                                                                      [1,1,1,1,1,1,1,1]]

                          banca = Dealer()
                          print("A Primeira Carta Do Dealer Foi:",banca[1])
                          for i in inf():
                              resposta = input("Mais Uma Carta?: ")
                              print("")
                              print("")
                              if (resposta == "sim" or resposta == "s"):
                                   n = ale.begin()
                                   for i in range(13):
                                        if(n[0] == x[i]):
                                             posicao = posicao +1
                                             carta[posicao] = i+1
                                   imprimir(n[0],n[1])

                              elif(resposta == "não" or resposta == "n" or resposta == "nao"):
                                  for j in range(12):
                                      if(j == 0):
                                          pontos = carta[j]
                                      else:
                                          pontos = pontos + carta[j]
                                  if(pontos > 21 and banca[0] > 21):
                                      print("A soma dos pontos É:",pontos,"Voçê Perdeu!!")
                                      fim_de_jogo()
                                                        
                                                      
                                  elif (pontos < 21 and banca[0] < 21 and pontos == banca[0]):
                                      print("A soma dos pontos É:",pontos,"E a Banca Tambem É:",banca[0],"Empatou!!!")
                                      break
                                                      
                                  elif(pontos < 21 and pontos < banca[0] and banca[0] <= 21):
                                      print("A soma dos pontos É:",pontos,"Mas a Banca É:",banca[0],"Voçê Perdeu!!")
                                      fim_de_jogo()
                                      break
                                                      
                                  elif(pontos <= 21 and pontos > banca[0]):
                                      print("A soma dos pontos É:",pontos,"E Banca É:",banca[0],"Voçê Ganhou!!")
                                      escore = int(escore + 10)
                                      print("""
                                                                  
                                                                 
                                                                  ||  |||
                                                          ||     ||| || ||
                                                        ||||||    || || ||
                                                          ||      || || ||
                                                                  ||  |||



                                                   """)
                                      cont = 0
                                      perg = ''
                                      while cont == 0:
                                            perg = input("Voce deseja voltar ao Menu(menu), ou continuar (cont)")
                                            if perg == "menu" or perg == "m" or perg == "Menu" or perg == "MENU" or perg == "cont" or perg == "c" or perg == "CONT":
                                                cont = 1
                                            else:
                                                print("Digite novamente!!")
                                                    
                                      if perg == "menu" or perg == "m" or perg == "Menu" or perg == "MENU":
                                                  menu()
                                                  
                                      elif perg == "cont" or perg == "c" or perg == "CONT":
                                                  jogando(escore)

                                  elif(pontos <= 21 and banca[0] > 21):
                                      print("A soma dos pontos É:",pontos,"E Banca É:",banca[0],"Voçê Ganhou!!")
                                      escore = escore + 10
                                      print("""
                                                                  
                                                                 
                                                                  ||  |||
                                                          ||     ||| || ||
                                                        ||||||    || || ||
                                                          ||      || || ||
                                                                  ||  |||



                                                   """)
                                      cont = 0
                                      perg = ''
                                      while cont == 0:
                                            perg = input("Voce deseja voltar ao Menu(menu), ou continuar (cont)")
                                            if perg == "menu" or perg == "m" or perg == "Menu" or perg == "MENU" or perg == "cont" or perg == "c" or perg == "CONT":
                                                cont = 1
                                            else:
                                                print("Digite novamente!!")
                                      if perg == "menu" or perg == "m" or perg == "Menu" or perg == "MENU":
                                                  menu()
                                      elif perg == "cont" or perg == "c" or perg == "CONT":
                                                  jogando(escore)
                                  else:
                                      Game_over()
                                      break
                              else:
                                   print("Invalido - Por Favor Responda Com sim,s ou nao(não),n")
                jogando(escore)
    else:
           print("¨%Fechou%")
if __name__ == '__main__':
    x = login()