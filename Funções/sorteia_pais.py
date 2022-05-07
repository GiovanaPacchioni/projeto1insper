#Função que inicia o jogo sorteando o país
import random
def sorteia_pais (dic_paises):
    lista_paises= []
    for paises,dados in dic_paises.items():
        lista_paises.append(paises)
    lista_random= random.choice(lista_paises)
    return lista_random