# Paso 1: Solcitar al usuario que ingrese la edad del cliente.

edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca.
# permitido = True
# if edad >= 18:
#    permitido = True
#else: 
#    Permitido = False
# Eso había sido el paso más largo, pero se puede hacer un TERNARIO donde quedaría de la siguiente forma:

permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca.

if permitido:
    print("¡Puedes ingresar a la discoteca!")
else:
    print("¡Lo sentimos muchos, no puedes ingresar a la discoteca por ser menor de edad!")