inventory = []
def add_product():
            product_name = input("Escribe el nombre del producto que deseas agregar: ").lower()
            amount = int(input("Ingrese la cantidad deseada: "))
            prices = float(input("Ingrese el precio de sus productos: "))
            total_costs = amount*prices
            return{
                    'Producto': product_name, 
                    'Cantidad': amount, 
                    'Precio' : prices, 
                    'TOTAL': total_costs} 
def show_inventory():
    print("========INVENTARIO ACTUAL==========")
    for show_storage in inventory:
        print(f"Producto: ", show_storage["Producto"], "Cantidad: ", show_storage["Cantidad"], "Precio", show_storage["Precio"] )

def calculate_estadistics():
      print("=========NO HAY ESTADISTICAS QUE MOSTRAR=============")
      for total_cost in inventory:
        print(f"Producto: ", show_storage["Producto"], "Cantidad: ", show_storage["Cantidad"], "Precio", show_storage["Precio"], "TOTAL: ", show_storage["Total"])
        print(f"")
        show_storage["Total"]  
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
            if enter <= 1 or enter >= 5:
                  print("Opcion invalida intente un numero entre 1 y el 4")
        except ValueError:
            print("Opcion invalida intente de nuevo")
            continue
        if enter == 1:
                  new_product = add_product()
                  inventory.append(new_product)
                  print(inventory)
        elif enter == 2:
            if inventory :
             show= show_inventory()
            else:
                  print("==========INVENTARIO VACIO=============")
        elif enter == 3:
            if inventory :
                 show2 = calculate_estadistics()
            else:
                 print("======NO HAY ESTADISTICAS QUE MOSTRAR=======")

                        


       
          