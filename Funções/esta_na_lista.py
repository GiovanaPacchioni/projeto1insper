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