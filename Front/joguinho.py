import random 

print ("============================" + ("\n") + "|                            |"+ ("\n") +"| Bem-vindo ao Insper Países |"+ ("\n")+ "|                            |"+ ("\n") + "==== Design de Software ==== "+ ("\n") + ("\n") +"Comandos:" + ("\n") +  "dica       - entra no mercado de dicas"  + ("\n") + "desisto    - desiste da rodada" + ("\n") + "inventario - exibe sua posição"+ ("\n") + ("\n"))
dados= ["Brasil", "México", "Peru"]
sorteado= random.choice(["Brasil", "México", "Peru"])
tentativas= 20
lista_distancias_p= []

dic_distancia= {}
dic_dicas= {}
dic_mercado_dicas= {}
while tentativas != 0:
    print ("Um país foi escolhido, tente adivinhar!"+ ("\n") + "Você tem {0} tentativa(s)".format(tentativas))
    tentativa= input("Qual seu palpite?: ")  
    if tentativa not in ["desisto", "dica", "inventario"]:
        tentativas-=1
        #harvesine
        dist= 123
        if dist not in dic_distancia:
            dic_distancia["Distancia"]= str(dist + "-->" + tentativa)
        if tentativa == sorteado:
            print ("*** Parabéns! Você acertou após {0} tentativas!".format(20 - tentativas))
    elif tentativa == "desisto":
        tem_certeza= input("Tem certeza que deseja desistir? [s/n] ")
        if tem_certeza == "s":
            print (">>>Que deselegante desistir, o país era: {0}".format(sorteado))
            joga_dnv= input("Quer jogar novamente?: ")
            if joga_dnv== "s":
                tentativas=20
            else: 
                break
    elif tentativa == "dica":
        tentativas-=1
        print ("Mercado de Dicas" + ("\n") + "----------------------------------------"+ ("\n") + "1. Cor da bandeira  - custa 4 tentativas" + ("\n") + "2. Letra da capital - custa 3 tentativas" + ("\n") + "3. Área             - custa 6 tentativas"  + ("\n") + "4. População        - custa 5 tentativas"+ ("\n") + "5. Continente       - custa 7 tentativas"+ ("\n") + "0. Sem dica"+ ("\n") + "----------------------------------------")
        qual_dica= int(input("Escolha sua opção: |0|1|2|3|4|5| "))
        while qual_dica not in [0,1,2,3,4,5]:
            print ("Opção inválida")
        if qual_dica == 1:
            dic_mercado_dicas[1]
            tentativas-=4
            #importar e randomizar cor da bandeira do arquivo com a base normalizada
        elif qual_dica == 2:
            tentativas-=3
            #importar o sortear letra e aplicar na base normalizada
        elif qual_dica == 3:
            tentativas-=5
            #importar área do país com a base normalizada
        elif qual_dica == 4:
            #importar população do país com a base normalizada
        elif qual_dica == 5:
            #importar continente do país com a base normalizada
        else:
    elif tentativa == "inventário":

        print(dic_distancia)
        print(dic_dicas)

print ("até a próxima!")     
    
