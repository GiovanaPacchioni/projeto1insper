import random 
from base_normalizada import dados_normalizados
from Funcoes import *

print ("============================" + ("\n") + "|                            |"+ ("\n") +"| Bem-vindo ao Insper Países |"+ ("\n")+ "|                            |"+ ("\n") + "==== Design de Software ==== "+ ("\n") + ("\n") +"Comandos:" + ("\n") +  "dica       - entra no mercado de dicas"  + ("\n") + "desisto    - desiste da rodada" + ("\n") + "inventario - exibe sua posição"+ ("\n") + ("\n"))
sorteado= sorteia_pais(dados_normalizados)
tentativas= 20
lista_cor= list(dados_normalizados[sorteado]["bandeira"])
lista_cor_nova= []
lista_letra= list(dados_normalizados[sorteado]["capital"])
lista_letra_nova=[]
areas= (dados_normalizados[sorteado]["area"])
lista_distancias_p= []
populacao= (dados_normalizados[sorteado]["populacao"])
continente= (dados_normalizados[sorteado]["continente"])
dic_distancia= {}
dic_mercado_dicas= {
    1: "Cor da bandeira",
    2: "Letra da capital",
    3: "Área",
    4: "População",        
    5: "Continente",       
    0: "Sem dica",
}
raio= 6371 
while tentativas != 0:
    print ("Um país foi escolhido, tente adivinhar!"+ ("\n") + "Você tem {0} tentativa(s)".format(tentativas))
    palavra= input("Qual seu palpite?: ") 
    if palavra not in ["desisto", "dica", "inventario"] and palavra in dados_normalizados:
        tentativas-=1
        dist= haversine(raio, dados_normalizados[sorteado]['geo']['latitude'], dados_normalizados[sorteado]['geo']['longitude'], dados_normalizados[palavra]['geo']['latitude'], dados_normalizados[palavra]['geo']['longitude'] )
        if dist > 0 and dist not in dic_distancia:
            dic_distancia["Distancia"]= str(dist) + "-->" + str(palavra)
        if dist == 0 and palavra == sorteado:
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
        opcoes= "|0|1|2|3|4|5|:"
        qual_dica= int(input("Escolha sua opção: {0}".format(opcoes)))
        while qual_dica not in [0,1,2,3,4,5]:
            print ("Opção inválida")
        if qual_dica == 1:
            cond=True
            while cond:
                if len(lista_cor)>0:
                    tentativas-=4
                    coraleatoria = ([random.randint(0, len(lista_cor) - 1)]) 
                    lista_cor.pop(lista_cor[lista_cor.index(coraleatoria)])
                    lista_cor_nova.append(coraleatoria)
                    print ("Lista de cores: {0}".format(lista_cor_nova))
                else:
                    cond=False
                    del dic_mercado_dicas[qual_dica]
                    opcoes[2]=""
                    opcoes[3]=""
                    print("Acabaram as cores :( ")
            
        elif qual_dica == 2:
            while cond:
                if len(lista_letra)>0:
                    tentativas-=3
                    letra_capital= ([random.randint(0, len(lista_letra) - 1)]) 
                    del lista_letra[lista_letra.index(letra_capital)]
                    lista_letra_nova.append(letra_capital)
                    print ("Lista de letras: {0}".format(lista_letra_nova))
                else:
                    cond=False
                    del dic_mercado_dicas[qual_dica]
                    opcoes[4]=""
                    opcoes[5]=""
                    print("Acabaram as letras")
        elif qual_dica == 3:
            if qual_dica in dic_mercado_dicas:
                print ("A área do país é: {0}".format(areas))
                del dic_mercado_dicas[qual_dica]
                opcoes[6]=""
                opcoes[7]=""
                tentativas-=6
        elif qual_dica == 4:
            if qual_dica in dic_mercado_dicas:
                print ("A população do país é: {0}".format(populacao))
                del dic_mercado_dicas[qual_dica]
                opcoes[8]=""
                opcoes[9]=""
                tentativas-=5
        elif qual_dica == 5:
            if qual_dica in dic_mercado_dicas:
                print("O continente do país é: {0}".format(continente))
                del dic_mercado_dicas[qual_dica]
                opcoes[10]=""
                opcoes[11]=""
                tentativas-=7
    
    elif palavra == "inventário":
            print(dic_distancia)
            print(dic_mercado_dicas)
print ("até a próxima!")     