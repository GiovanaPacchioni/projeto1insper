import random 
from base_normalizada import dados_normalizados
from Funcoes import haversine
from projeto1insper.Main.Funcoes import sorteia_pais

print ("============================" + ("\n") + "|                            |"+ ("\n") +"| Bem-vindo ao Insper Países |"+ ("\n")+ "|                            |"+ ("\n") + "==== Design de Software ==== "+ ("\n") + ("\n") +"Comandos:" + ("\n") +  "dica       - entra no mercado de dicas"  + ("\n") + "desisto    - desiste da rodada" + ("\n") + "inventario - exibe sua posição"+ ("\n") + ("\n"))
dados= ["Brasil", "México", "Peru"]
sorteado= random.choice(dados_normalizados)
tentativas= 20
lista_distancias_p= []

dic_distancia= {}
dic_dicas= {}
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
            dic_distancia["Distancia"]= str(dist + "-->" + palavra)
        if dist == 0 and palavra == sorteado:
            print ("*** Parabéns! Você acertou após {0} tentativas!".format(20 - tentativas))
    elif palavra == "desisto":
        tem_certeza= input("Tem certeza que deseja desistir? [s/n] ")
        if tem_certeza == "s":
            print (">>>Que deselegante desistir, o país era: {0}".format(sorteado))
            joga_dnv= input("Quer jogar novamente?: ")
            if joga_dnv== "s":
                tentativas=20
            else: 
                break
    elif palavra == "dica":
        tentativas-=1
        print ("Mercado de Dicas" + ("\n") + "----------------------------------------"+ ("\n") + "1. Cor da bandeira  - custa 4 tentativas" + ("\n") + "2. Letra da capital - custa 3 tentativas" + ("\n") + "3. Área             - custa 6 tentativas"  + ("\n") + "4. População        - custa 5 tentativas"+ ("\n") + "5. Continente       - custa 7 tentativas"+ ("\n") + "0. Sem dica"+ ("\n") + "----------------------------------------")
        #WHILE DAS DICAS
        qual_dica= int(input("Escolha sua opção: |0|1|2|3|4|5| "))
        while qual_dica not in [0,1,2,3,4,5]:
            print ("Opção inválida")
        cond=True
        if qual_dica == 1:
            while cond:
                if len(list(dados_normalizados[sorteado]["bandeira"]))>0:
                    tentativas-=4
                    coraleatoria = ([random.randint(0, len(list(dados_normalizados[sorteado]["bandeira"])) - 1)]) #DAR UM NOME NESSA LISTA
                    del list(dados_normalizados[sorteado]["bandeira"])[list(dados_normalizados[sorteado]["bandeira"]).index(coraleatoria)]
                    print(coraleatoria)
                else:
                    cond=False
                    

            
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
    elif palavra == "inventário":

        print(dic_distancia)
        print(dic_dicas)

print ("até a próxima!")     
    
