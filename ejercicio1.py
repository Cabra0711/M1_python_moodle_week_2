#DATA_MARKET
products = []
total = 0 
total_expired = 0

amount = int(input("ingrese una cantidad: "))
products_expired = 0
for i in range(amount):
    product_name = input("Ingrese el nombre de su producto:")
    price = float(input("Escribe el precio de tu producto"))
    expired = input("El producto esta vencido? S/N").lower()
    if expired == "N":
        products = {"nombre": product_name, "Precio": price}
        





