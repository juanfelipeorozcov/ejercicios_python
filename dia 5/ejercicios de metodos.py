# añadir un cuarto elemento llamado "naranja en la casilla 4 de la lista  usando metodo insert()

frutas = ["mango","banana","cerveza","ciruela","pomelo"]
frutas.insert(2,"naranja") # insert me va a insertar lo que queramos y el numero es la casilla donde queremos
print(frutas)

# verificar si los sets no tienen elementos en comun metodo isdisjoint()

marcas_smartphones = {"Samsung", "xiaomi", "aple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_tv.isdisjoint(marcas_smartphones)