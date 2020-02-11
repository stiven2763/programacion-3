if __name__ == "__main__":
    print("Lista de Supermercado")
    sm = {}
    contador = 0

    archivo = open("super.txt", "r")
    for linea in archivo:
        linea = linea.strip()
        llave = linea.split(',')[0] #Se declara la variable llave para poder crear el diccionario
        valor = int(linea.split(',')[1]) #Se declara el valor que estara afiliado a la llave
                                        # y se esta defininiendo que sera de tipo entero
        sm[llave] = valor   # Se declara que el archivo "super" va a estar compuesto por llave la cual sera de tipo lista
                            #  y que esta va a tener asignado la variable "valor"
        contador += 1     # Se declara la variable para que funcione como un tipo de contador la cual va a contar las lineas que
    archivo.close()

    if contador > 0: #Si la lista no tiene productos, este imprimira lo siguiente.
        print('La lista tiene productos!')
    else:
        print('La lista no tenia productos!')
    for n in range(3):
        articulo = input("Se va a agregar los siguientes item: ")
        cantidad = input("Cantidad de " + articulo + ": ")
        sm[articulo] = cantidad

    print("\tMi Lista")
    num: int = 1
    for k,v in sm.items():
        print(str(num) + ". "+ k + ": " + str(v))
        num += 1

    while True:
        try:
            opc = int(input("\nArt. por Eliminar (n): "))
        except:
            print("Numero invalido")
            opc = len(sm)+1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")
            print("\nEstariamos eliminando " + sm[opc-1])
            sm.pop(opc-1)

        print("\tMi Lista")
        num = 1
        for a in sm:
            print(str(num) + ". " + a)
            num += 1

    while True:
        try:
            opc = int(input("\nArt. por Sustituir (n): "))

        except:
            print("Numero invalido")
            opc = len(sm) + 1
        if opc <= len(sm) and opc > 0:
            break
        else:
            print("Articulo no existe")

            print("\nEstariamos sustituyendo " + sm[opc - 1])
            articulo = input("Nuevo Articulo: ")
            sm[opc - 1] = articulo

    archivo = open("super.txt", "a+")
    for a in sm:
        archivo.write(a)
    archivo.close()