print("Hola, ingresa el total de tu compra")
total_compra = input()

if int(total_compra) > 100:
    tasa_descuento = 10
    importe_descuento = int(total_compra) * tasa_descuento / 100
    importe_a_pagar = int(total_compra) - importe_descuento
    
print(importe_a_pagar)
