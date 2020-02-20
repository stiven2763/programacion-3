class Articulo:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
if __name__ == '__main__':
    print("\tGestor de Stock")
    respuesta = "si"
    articulos = []
    precios = []
    stock = []
# Menú Principal
while True:
    print('')
    print('****** Menú Principal ******')
    print('0. SALIR')
    print('1. INGRESO DE PRODUCTO')
    print('2. BUSQUEDA DE PRODUCTO')
    print('3. ELIMINAR PRODUCTO')
    print('4. MODIFICAR PRODUCTO')
    opcion=input('Digitar una Opción: ')
    if opcion=='0':
        break
    elif opcion=='1':
      Articulo.nombre = input('Nombre de el articulo: ')
      articulos.append(Articulo.nombre)
      Articulo.precio = input('Precio de el articulo: ')
      precios.append(Articulo.precio)
      Articulo.stock = input('Cantidad de articulo: ')
      stock.append(Articulo.stock)
    elif opcion=='2':
      pro = input("cual es el producto a buscar?: ")
      if pro in articulos:
        print("\tCantidad: " + stock[articulos.index(pro)] + " unidades")
        print("\tPrecio: " + precios[articulos.index(pro)] + "$")
    elif opcion=='3':
      adios = input("Que articulo deseas eliminar? :")
      if adios in articulos:
        precios.pop(articulos.index(adios))
        cantidad.pop(articulos.index(adios))
        articulos.remove(adios)
    elif opcion=='4':
      prow = input("Ingrese el nuevo nombre del Producto ")
      articulos[articulos.index(pro)] = new
      cantidad[articulos.index(prow)] = input("Ingrese la cantidad del nuevo producto: ")
      cantidad[articulos.index(pro)] = input("Ingrese la nueva cantidad: ")
      precios[articulos.index(prow)] = input("Ingrese el precio del nuevo articulo: ")
      precios[articulos.index(pro)] = input("Ingrese el nuevo precio: ")

    else:
        print('Opción no válida')