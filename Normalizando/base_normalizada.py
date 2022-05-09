from matplotlib.cbook import delete_masked_points


def normaliza (DADOS):
    normalizado_dic= {}
    for cont, paises in DADOS.items():
        for pais, info in paises.items():
            info['continente']= cont
            normalizado_dic[pais] = info
    return normalizado_dic