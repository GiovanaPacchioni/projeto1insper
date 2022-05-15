#Guia das cores para as faixas de distancias (usar if para categorizar)
from sqlalchemy import true
from termcolor import colored #Lembrar que as cores estão nos países com dist e nas tentativas
#Exemplo
print(colored('Error Test!!!', 'red'))
print(colored('Warning Test!!!', 'yellow'))
print(colored('Success Test!!!', 'green'))

import random 
from base_normalizada import dados_normalizados
from Funcoes import *

print ("============================" + ("\n") + "|                            |"+ ("\n") +"| Bem-vindo ao Insper Países |"+ ("\n")+ "|                            |"+ ("\n") + "==== Design de Software ==== "+ ("\n") + ("\n") +"Comandos:" + ("\n") +  "dica       - entra no mercado de dicas"  + ("\n") + "desisto    - desiste da rodada" + ("\n") + "inventario - exibe sua posição"+ ("\n") + ("\n"))

sorteado= ''
tentativas= 20
lista_cor_possivel=[]
lista_cor_sorteada = []
lista_letra_nova= []
cond = True
lista_distancia= []
lista_dist_print= []
lista_dicas=[]   
lista_d_formatada= ""
pais_utilizado= []
raio= 6371 
cond2= True
joga_dnv= "s" #começando com a condição verdade

while joga_dnv == 's': #Loop de jogar o jogo 
    sorteado= sorteia_pais(dados_normalizados)
    dic_tds_cor=(dados_normalizados[sorteado]["bandeira"])
    lista_letra= list(dados_normalizados[sorteado]["capital"])
    areas= (dados_normalizados[sorteado]["area"])
    populacao= (dados_normalizados[sorteado]["populacao"])
    continente= (dados_normalizados[sorteado]["continente"])
    dica1= "1. Cor da bandeira  - custa 4 tentativas \n"
    dica2= "2. Letra da capital - custa 3 tentativas\n"
    dica3= "3. Área do país     - custa 6 tentativas\n"
    dica4= "4. População do país - custa 5 tentativa\n"
    dica5= "5. Continente do país - custa 7 tentativa\n"
    dica0= "0. Sem dica"
    dic_cor= {"- Cores da bandeira": lista_cor_sorteada}
    dic_letra= {"- Letras da capital": lista_letra_nova}
    dic_area= {"- Área do país": areas}
    dic_populacao= {"- População": populacao}
    dic_continente= {"- Continente": continente}
    dic_mercado_dicas= {
    1: "Cor da bandeira",
    2: "Letra da capital",
    3: "Área",
    4: "População",        
    5: "Continente",       
    0: "Sem dica",
    }
    dic_dicas= {} 
    dicas_for_real= str(dic_dicas)
    lista_dicas= [] 
    zero="[0"
    um="|1"
    dois="|2"
    tres="|3"
    quatro="|4"
    cinco="|5"
    chavef= "]"
    for cor, percentual in dic_tds_cor.items(): 
        if percentual > 0 and cor != "outras": #somente sortear as cores que tem na badeira
            lista_cor_possivel.append(cor)  
    while tentativas > 0:
        print ("Um país foi escolhido, tente adivinhar!"+ ("\n") + "Você tem {0} tentativa(s)".format(tentativas))
        palavra= input("Qual seu palpite?: ") 
        if palavra not in ["desisto", "dica", "inventario"] and palavra in dados_normalizados:
            dist = haversine(raio, dados_normalizados[sorteado]['geo']['latitude'], dados_normalizados[sorteado]['geo']['longitude'], dados_normalizados[palavra]['geo']['latitude'], dados_normalizados[palavra]['geo']['longitude'] )
            if esta_na_lista(palavra, pais_utilizado): #Inserindo a função está na lista, se estiver pedir para o joagdor escolher outro
                print ("Você já escolheu esse país, pensa em outra aí")  #Se estiver na lista ele não vai verificar dist e vai rodar o while dnv           
            elif dist > 0: 
                if palavra not in pais_utilizado:
                    pais_utilizado.append(palavra)
                    #lista_distancia.append([palavra, dist])
                    #lista das cores das distancias (0> and <1000 = azul  / 1000> and 2000< = amarelo / 2000> and 5000< = vermelho / 5000> and 10000< = rosa/roxo / 10000> = cinza )
                    lista_dist_print= adiciona_em_ordem(palavra, dist, lista_distancia) #adicione em ordem os países com as distâncias
                    tentativas-=1 #diminuindo a quantidade de tentativas
                    lista_d_formatada=formatando(lista_dist_print)
                    print(lista_d_formatada)
            elif dist == 0 and palavra == sorteado:
                print ("*** Parabéns! Você acertou após {0} tentativas!".format(20 - tentativas))
        elif palavra == "desisto":
            tem_certeza= input("Tem certeza que deseja desistir? [s/n] ")
            while tem_certeza not in ["s", "n"]:
                print ("Você não escolheu uma opção válida")
                tem_certeza= input("Tem certeza que deseja desistir? [s/n] ")
            if tem_certeza == "s":
                tentativas=0
                print (">>>Que deselegante desistir, o país era: {0}".format(sorteado))
                joga_dnv= input("Quer jogar novamente?: ")
                while joga_dnv not in ["s", "n"]:
                    print ("Você não escolheu uma opção válida")
                    joga_dnv= input("Quer jogar novamente?: [s/n] ")
                if joga_dnv== "s":
                    del dados_normalizados[sorteado]
                    sorteado= sorteia_pais(dados_normalizados)
                    tentativas=20
                    lista_d_formatada= ""
                    lista_distancia= []
                    lista_dist_print= []
                    lista_dicas=[]  
                    lista_letra_nova= []
                    lista_cor_possivel=[]
                    lista_cor_sorteada = []
                    pais_utilizado= []
                    joga_dnv= "s"
                else: 
                    tentativas=0
                    joga_dnv= "n"
        elif palavra == "dica":
            print ("Mercado de Dicas" + ("\n") + "---------------------------------------- \n{0}{1}{2}{3}{4}{5}\n ----------------------------------------".format(dica1 ,dica2, dica3, dica4, dica5, dica0))
            opcoes= zero + um + dois + tres + quatro + cinco + chavef
            qual_dica= input("Escolha sua opção: {0}".format(opcoes))
            print("Dicas: ")
            opcoes_validas= opcoes.replace("[", "") 
            opcoes_validas2= opcoes_validas.split("|") #usando replace e split para tornar opçoes uma lista com as variaveis/numero de dicas disponível
            while qual_dica not in opcoes_validas2:
                print ("Você não escolheu uma opção válida")
                qual_dica= input("Escolha sua opção: {0}".format(opcoes))
            else:
                qual_dica = int(qual_dica) #tornando a str que o usuário digitou em número inteiro para saber em qual if entrar
                if tentativas >= 4:
                    if qual_dica == 1:
                        if len(lista_cor_possivel)>0:
                            coraleatoria = random.choice(lista_cor_possivel)
                            lista_cor_sorteada.append(coraleatoria)
                            lista_cor_possivel.remove(coraleatoria) 
                            dic_dicas.update(dic_cor)
                            tentativas-=4
                        else:
                            dica1= ""
                            um= ""
                            print("Acabaram as cores :( ")
                            break
                else:
                    dica1= ""
                    um= ""
                if tentativas >= 3:
                    if qual_dica == 2:
                        if cond == True:
                            if len(lista_letra)>0 and qual_dica in dic_mercado_dicas:
                                letra_capital= (random.randint(0, len(lista_letra)-1))
                                lista_letra_nova.append(lista_letra[letra_capital])
                                del lista_letra[letra_capital]
                                dic_dicas.update(dic_letra)
                                tentativas-=3
                            elif len(lista_letra)<=0:
                                del dic_mercado_dicas[qual_dica]
                                dica2= ""
                                dois= ""
                                cond=False
                                print("Acabaram as letras :( ")
                else:
                    dica2= ""
                    dois= ""
                if tentativas >= 6:
                    if qual_dica == 3:
                        if qual_dica in dic_mercado_dicas:
                            dic_dicas.update(dic_area)
                            del dic_mercado_dicas[qual_dica]
                            dica3= ""
                            tres= ""
                            tentativas-=6
                        else:
                            print("Você já sabe a area do país")
                else:
                    dica3= ""
                    tres= ""
                if tentativas >= 5:
                    if qual_dica == 4:
                        if qual_dica in dic_mercado_dicas:
                            del dic_mercado_dicas[qual_dica]
                            dica4= ""
                            quatro= ""
                            dic_dicas.update(dic_populacao)   
                            tentativas-=5
                        else:
                            print("Você já sabe a população do país")
                else:
                    dica4= ""
                    quatro= ""
                if tentativas >= 6:
                    if qual_dica == 5:
                        if qual_dica in dic_mercado_dicas:
                            del dic_mercado_dicas[qual_dica]
                            dica5= ""
                            dic_dicas.update(dic_continente)
                            tentativas-=7
                            cinco= ""
                        else:
                            print("Você já sabe o continente do país")
                else:
                    dica5= ""
                    cinco= ""
                for dicas, descricao in dic_dicas.items():
                    dicas_for_real= str("{0}: {1}").format(dicas, descricao)
                    print(dicas_for_real)
        elif palavra == "inventario":
            print("\nInventário: \n {0} \n {1}\n".format(lista_d_formatada, dic_dicas))
        else:
            print ("Você não escolheu uma opção válida")
    else: #tentando criar a condição pra ele sair do jogo desistindo ou perdendo
        print (">>> Você perdeu, o país era: {0}".format(sorteado))
        joga_dnv= input("Quer jogar novamente?: [s/n] ")
        while joga_dnv not in ["s", "n"]:
            print ("Você não escolheu uma opção válida")
            joga_dnv= input("Quer jogar novamente?: [s/n] ")
        if joga_dnv == "s":
            del dados_normalizados[sorteado]
            sorteado= sorteia_pais(dados_normalizados)
            lista_d_formatada= ""
            lista_distancia= []
            lista_dist_print= []
            lista_dicas=[]  
            lista_letra_nova= []
            lista_cor_possivel=[]
            lista_cor_sorteada = []
            pais_utilizado= [] 
            tentativas=20
            cond= True
        elif joga_dnv == "n":
            tentativas=0
            joga_dnv= "n"