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