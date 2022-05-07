#utilizar essa função para depois dar "write" no arquivo "base_normalizada"
def normaliza (base_dados):
    normalizado_dic= {}
    for cont, paises in base_dados.items():
        for pais, info in paises.items():
            info['continente']= cont
            normalizado_dic[pais] = info
    return normalizado_dic