# crear cambios en archivos originales en abrir archivos y modificarlos
# "r" solo lectura ej: open(archivo.txt','r')
# "w" solo escritura ej: open(archivo.txt','w')
# "a"

archivo = open("texto.txt",'r')
archivo.write("soy el nuevo texto")
archivo.close()



