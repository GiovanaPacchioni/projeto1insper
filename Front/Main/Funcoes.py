def adiciona_em_ordem(pais, distancia, listaordenada):
    if len(listaordenada) == 0:
        listaordenada.append([pais, distancia])
    else:
        for i in range(len(listaordenada)):
            if distancia < listaordenada[i][1]:
                listaordenada.insert(i, [pais, distancia])
                break
        else:
            listaordenada.append([pais, distancia])
    return listaordenada

#Confirmar se o país escolhido ta na lista
#Se não estiver na lista printe: "país desconhecido"
def esta_na_lista (pais, lista_p):
    cond= False
    i=0
    for listas in lista_p:
        if pais == listas[0]:
            i+=1
    if i!=0:
        cond=True
    return cond

import math
def haversine(raio, lat1, lon1, lat2, lon2):
    lat1 = lat1 * math.pi / 180
    lon1 = lon1 * math.pi / 180
    lat2 = lat2 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = raio * c
    return d

def normaliza (base_dados):
    normalizado_dic= {}
    for cont, paises in base_dados.items():
        for pais, info in paises.items():
            info['continente']= cont
            normalizado_dic[pais] = info
    return normalizado_dic

#Função para a dica de sortear a letra da capital do país
import random
def sorteia_letra (palavra, restricao):
    letras_sorteadas= ""
    for letras in palavra:
        if letras.lower() not in restricao:
            if letras.upper() not in restricao:
                letras_sorteadas+= letras
    letras_sorteadas=list(letras_sorteadas)
    return random.choice(letras_sorteadas)

#Função que inicia o jogo sorteando o país
import random
def sorteia_pais (dic_paises):
    lista_paises= []
    for paises,dados in dic_paises.items():
        lista_paises.append(paises)
    lista_random= random.choice(lista_paises)
    return lista_random