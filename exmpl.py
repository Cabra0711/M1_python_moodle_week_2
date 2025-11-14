#Asignamos una variable llamada inventario para guardar la lista de productos que el usuario nos vaya digitando dentro de esta
inventory = []
#Añadimos una funcion llamada add_product y creamos variables con el nombre del producto, la cantidad, precio, y creamos otra variable
#Dentro de esta para que nos multiplique la cantidad  de productos por el precio que usuario añada
def add_product():
            product_name = input("Escribe el nombre del producto que deseas agregar: ").lower()
            amount = int(input("Ingrese la cantidad deseada: "))
            prices = float(input("Ingrese el precio de sus productos: "))
            total_costs = amount*prices
            #Usamos return para que nos devuelva a la consola los valores de el diccionario dentro del codigo llamando las variables y asignandoles una clave
            return{
                    'Producto': product_name, 
                    'Cantidad': amount, 
                    'Precio' : prices, 
                    'TOTAL': total_costs} 
#Agregamos otra funcion para cuando el usuario digite el boton 2 llamar a la funcion y que muestre el inventario que tiene el usario
def show_inventory():
    print("========INVENTARIO ACTUAL==========")
#Usamos un bucle for para que lea todo lo que hay adentro del inventario que el usuario digito en la primera opcion 
    for show_storage in inventory:
#Hacemos un print con un f-print para que lea las claves que asignamos arriba leyendo el inventario y el diccionario de arriba para que le arroje 
#Los productos que el usuario guardo dentro de este
        print(f"Producto: ", show_storage["Producto"], "Cantidad: ", show_storage["Cantidad"], "Precio", show_storage["Precio"] )
#hacemos otra funcion que se llame calcular estadisticas y dentro de este creamos variables de enteros para llamarlas despues y multiplicarlas por el valor TOTAL y cantidad.
def calculate_estadistics():
      total_value = 0
      total_amount = 0
#Le hacemos saber al usuario que sus estadisticas se estan cargando
      print("=======CALCULANDO ESTADISTICAS===========")
      for product in inventory:
#Llamamos a las variables y le ponemos un operador de suma y asignacion para que al usuario digitar el numero 3 le tire la cantidad  y el total 
#Sumando estos valores al diccionario
        total_value += product ["TOTAL"]
        total_amount += product ["Cantidad"]
        print("=========ESTADISTICAS FINALES==========")
        print(f"Valor total del inventario ${total_value:.2f}")
        print(f"Cantidad total de item registrados: {total_amount}")
        print("========================")
#Creamos un bloque de while True para pasar a crear el menu donde pondremoos las opciones del programa que tiene disponible el usuario para acceder
#Añadiendo un bloque Try except para que el codigo no de error cuando el usuario digite digitos invalidos dentro del menu
while True:
        print("=============MENU=============")
        print("BIENVENIDO INVENTARIO LA VAQUITA")
        enter_1 = print("1. Agregar producto")
        show_storage= print("2. Mostrar inventario")
        show_costs= print("3. Calcular estadísticas")
        exit = print("4. Salir del programa")
        print("================================")
        try:
            enter = int(input("ingrese una opcion para ingresar el menu: "))
#Ponemos un condicional if que asigne la condicion que si el usuario digita un numero menor a 1 y mayor a 5 le vuelva a pedir los datos.
            if enter <= 1 and enter >= 5:
                  print("Opcion invalida intente un numero entre 1 y el 4")
        except ValueError:
            print("Opcion invalida intente de nuevo")
            continue
#Creamos otro condicional que es para cuando el usuario ingrese un nuevo producto llamemos a la variable de add_product() y creamos
# un .append para que se añada el producto en el inventario
        if enter == 1:
                  new_product = add_product()
                  inventory.append(new_product)
                  print(inventory)
#Agregamos otro condicional para que cuando el usuario nos digite un numero igual a 2 nos llame la lista invetario y la muestre creando asi mismo
#Otra variable llamada show para que llame la funcion 2 y le muestre todo el inventario
        elif enter == 2:
            if inventory :
             show= show_inventory()
#creamos un condicional llamadado else que si no se cumplen los parametros anteriores le ponga a el usuario que le inventario se encuentra vacio
            else:
                  print("==========INVENTARIO VACIO=============")
#Repetimos el mismo proceso con el numero 3 
        elif enter == 3:
            if inventory :
                 show2 = calculate_estadistics()
            else:
                 print("======NO HAY ESTADISTICAS QUE MOSTRAR=======")
#Añadimos otro condicional elif que cuando el usuario digite un numero igual a 4 lo saque del blucle directamente.
        elif enter == 4:
             print("Gracias por acceder al inverio la vaquita nos vemos pronto!!")
             break

                        


       
          
