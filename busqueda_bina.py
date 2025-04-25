def busquedabinaria(list,buscar):
    izquierda,derecha=0,len(list)-1
    while izquierda<=derecha:
        medio=izquierda+(derecha-izquierda)//2
        if list[medio]==buscar:
            return medio
        elif list[medio]<buscar:
            izquierda=medio+1
        else:
            derecha=medio-1
    return -1

list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,17,19,20,110,18,]
buscar=18

resultado=busquedabinaria(list,buscar)
if resultado != -1:
    print("objetivo encontrado en el indice: " , resultado)
else:
    print("el  numero no se encuentra en la lista ")