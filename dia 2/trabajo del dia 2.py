# hacer un programa que donde una empresa pregunte las comisiones y pregunte los nombres y el monto por comisiones

nombre = input("dime tu nombre: ")
ventas = input("cuales son tus ventas totales del mes: ")

ventas = input(ventas)

comision = round(ventas*13/100,2)

print(f"Hola {nombre}, tus comisiones de este mes son : {comision}")