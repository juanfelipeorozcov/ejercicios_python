# if = si  siempre se pone dos puntos al final if:
# elif = si no
# else = si no

#if 10 > 9 :
   # print("es correcto")

#else:
    #print("no es correcto ")


mascota = "perro"

if mascota == "gato":
    print("tienes un gato")
elif mascota == "perro":
    print("tienes un perro")
elif mascota == "pez":
    print("tienes un pez")
else:
    print(" no se que animal tienes ")


# anidar condiciones if

edad = 16
calificacion = 9
if edad < 18:
    print(" eres menor de edad ")
    if calificacion >= 7:
        print("Aprovado")
    else:
        print("no aprobado")
else:
    print("eres adulto")




