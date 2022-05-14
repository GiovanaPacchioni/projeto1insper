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
sorteado= sorteia_pais(dados_normalizados) #Linhas para colocar dentro do while
tentativas= 20
dic_tds_cor=(dados_normalizados[sorteado]["bandeira"])#Linhas para colocar dentro do while
lista_cor_possivel=[]
lista_cor_sorteada = []
lista_letra= list(dados_normalizados[sorteado]["capital"])#Linhas para colocar dentro do while
lista_letra_nova= []
areas= (dados_normalizados[sorteado]["area"])#Linhas para colocar dentro do while
populacao= (dados_normalizados[sorteado]["populacao"])#Linhas para colocar dentro do while
continente= (dados_normalizados[sorteado]["continente"])#Linhas para colocar dentro do while
cond = True
#Elementos que aparecem no inventario
inventario = {}
lista_distancia= []
lista_dist_print= []
lista_dicas=[]  
dic_dicas= {}  #substituindo o dicionario pela lista em lista ordenada -> só tirar depois de substituir

pais_utilizado= []

dic_cor= {"- Cores da bandeira": lista_cor_sorteada}
dic_letra= {"- Letras da capital": lista_letra_nova}
dic_area= {"- Área": areas}
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
raio= 6371 

for cor, percentual in dic_tds_cor.items(): 
    if percentual > 0 and cor != "outras": #somente sortear as cores que tem na badeira
        lista_cor_possivel.append(cor)
joga_dnv= "s" #começando com a condição verdade
while joga_dnv == 's':
    while tentativas != 0:
        print ("Um país foi escolhido, tente adivinhar!"+ ("\n") + "Você tem {0} tentativa(s)".format(tentativas))
        palavra= input("Qual seu palpite?: ") 
        if palavra not in ["desisto", "dica", "inventario"] and palavra in dados_normalizados:
            dist = haversine(raio, dados_normalizados[sorteado]['geo']['latitude'], dados_normalizados[sorteado]['geo']['longitude'], dados_normalizados[palavra]['geo']['latitude'], dados_normalizados[palavra]['geo']['longitude'] )
            if esta_na_lista(palavra, pais_utilizado): #Inserindo a função está na lista, se estiver pedir para o joagdor escolher outro
                print ("Você já escolheu esse país, pensa em outra aí")  #Se estiver na lista ele não vai verificar dist e vai rodar o while dnv           
            elif dist > 0: 
                tentativas-=1 
                pais_utilizado.append(palavra)
                #lista das cores das distancias (0> and <1000 = azul  / 1000> and 2000< = amarelo / 2000> and 5000< = vermelho / 5000> and 10000< = rosa/roxo / 10000> = cinza )
                lista_distancia= adiciona_em_ordem(palavra, dist, lista_distancia) #adicione em ordem os países com as dist
                for lista in lista_distancia:
                        #pais = elementos[0]
                        pais = lista_distancia[0][0]
                        distancia= lista_distancia[0][1]
                        lista_dist_print.append("{0} --> {1}".format(pais, distancia))
                        inventario["Distancias"]= [lista_dist_print]
                print(lista_dist_print)
                #não sei se é melhor printar essa lista assim ou formatar a outra
            elif dist == 0 and palavra == sorteado:
                print ("*** Parabéns! Você acertou após {0} tentativas!".format(20 - tentativas))
        elif palavra == "desisto":
            tem_certeza= input("Tem certeza que deseja desistir? [s/n] ")
            if tem_certeza == "s":
                tentativas=0
                print (">>>Que deselegante desistir, o país era: {0}".format(sorteado))
                joga_dnv= input("Quer jogar novamente?: ")
                if joga_dnv== "s":
                    tentativas=20
                else: 
                    break
        elif palavra == "dica":
            print ("Mercado de Dicas" + ("\n") + "----------------------------------------"+ ("\n") + "1. Cor da bandeira  - custa 4 tentativas" + ("\n") + "2. Letra da capital - custa 3 tentativas" + ("\n") + "3. Área             - custa 6 tentativas"  + ("\n") + "4. População        - custa 5 tentativas"+ ("\n") + "5. Continente       - custa 7 tentativas"+ ("\n") + "0. Sem dica"+ ("\n") + "----------------------------------------")
            opcoes= "[0|1|2|3|4|5]: "
            qual_dica= input("Escolha sua opção: {0}".format(opcoes))
            if qual_dica != "1" and qual_dica != "2" and qual_dica != "3" and qual_dica != "4" and qual_dica != "5" and qual_dica != "0":
                print ("Você não escolheu uma opção válida")
            else:
                qual_dica = int(qual_dica)
                if qual_dica == 1:
                    if len(lista_cor_possivel)>0:
                        coraleatoria = random.choice(lista_cor_possivel)
                        print (coraleatoria)
                        lista_cor_sorteada.append(coraleatoria)
                        inventario["Cor da bandeira"] = [coraleatoria]
                        lista_cor_possivel.remove(coraleatoria) 
                        dic_dicas.update({"Dicas: ": dic_cor})
                        print(dic_dicas)
                        tentativas-=4
                    else:
                        print("Acabaram as cores :( ")
                
                elif qual_dica == 2:
                    if cond == True:
                        if len(lista_letra)>0:
                            letra_capital= (random.randint(0, len(lista_letra)-1))
                            lista_letra_nova.append(lista_letra[letra_capital])
                            dic_dicas.update({"Dicas: ": [(lista_letra[letra_capital])]})
                            print ("Lista de letras: {0}".format(lista_letra_nova))
                            inventario["Letras da capital"] = [lista_letra_nova]
                            del lista_letra[letra_capital]
                            tentativas-=3
                        elif len(lista_letra)<=0:
                            cond=False
                            print("Acabaram as letras :( ")
                elif qual_dica == 3:
                    if qual_dica in dic_mercado_dicas:
                        dic_dicas.update({"Dicas: ": dic_area})
                        print (dic_dicas)
                        del dic_mercado_dicas[qual_dica]
                        inventario["Area do país"] = [dic_area]
                        tentativas-=6
                    else:
                        print("Você já sabe a area do país")
                elif qual_dica == 4:
                    if qual_dica in dic_mercado_dicas:
                        print ("A população do país é: {0}".format(populacao))
                        del dic_mercado_dicas[qual_dica]
                        dic_dicas.update({"Dicas: ": dic_populacao})
                        inventario["População"] = [dic_populacao]
                        tentativas-=5
                    else:
                        print("Você já sabe a população do país")
                elif qual_dica == 5:
                    if qual_dica in dic_mercado_dicas:
                        print("O continente do país é: {0}".format(continente))
                        del dic_mercado_dicas[qual_dica]
                        dic_dicas.update({"Dicas: ": dic_continente})
                        inventario["Continente"] = [dic_continente]
                        tentativas-=7
                    else:
                        print("Você já sabe o continente do país")
        elif palavra == "inventario":
            print("Inventário: {0}".format(inventario))
        else:
            print ("Você não escolheu uma opção válida")
    if joga_dnv!= "s":
        break
    else: #tentando criar a condição pra ele sair do jogo desistindo ou perdendo
        print (">>> Você perdeu, o país era: {0}".format(sorteado))
        joga_dnv= input("Quer jogar novamente?: ")
        tentativas=20