# desembolber taples

precios_cafe = [("capuchino", 1.5), ("Expreso",1.2),("Moka",1.9)]

for cafe,precio in precios_cafe:
    print(cafe)

 si quiero saber el precio in print pongo precio ahora si quiero saber el costo del 45 % de su valor de venta

for cafe,precio in precios_cafe:
     print(precio*0.45)

  ahora usamos las funciones

def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    cafe_mas_caro= ""

    for cafe,precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))