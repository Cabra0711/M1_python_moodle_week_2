inventory = []

def add_product():
                product_name = input("Escribe el nombre del producto que deseas agregar: ")
                
                amount = int(input("Cantidad que deseas añadir: "))
                
                price = float(input("Ingrese el precio de su producto: "))
                
                return {product_name, amount, price}

lista_deproducto=[add_product]

while True:
    print("=============MENU=============")
    print("BIENVENIDO INVENTARIO LA VAQUITA")
    enter_1 = print("1. Agregar producto")
    show_storage= print("2. Mostrar inventario")
    show_costs= print("3. Calcular estadísticas")
    exit = print("4. Salir del programa")
    try:
        enter = int(input("ingrese una opcion para ingresar el menu: "))
    except ValueError:
        print("Opcion invalida intente de nuevo")
        continue
    if enter == 1:
           new_product = add_product()
    print(f"Producto {new_product} agregado.")
    answer = input("Deseas volver al menu principal? SI/NO ").lower
    if answer == "SI":
        continue
    if enter == 2:
           print(f"Su inventario es:{inventory}")
           
    
    
          


        

        
    



