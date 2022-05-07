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
