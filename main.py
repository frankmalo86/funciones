#FUNCIONES
def saludo (nombre): # declaración de la funcion
                    # entre parentisis, separados por coma, están los parametros que RECIBE la función
  print("Hola ", nombre)   # cuerpo de la función


# una función puede retornar 0, 1 o n valores
# return



def calculadora (numero1,numero2,operacion):
    total=0
    if operacion=="suma":
        total=numero1 + numero2
    elif operacion=="resta":
        total=numero1 - numero2   
    elif operacion=="multiplicación":
        total=numero1 * numero2   
    elif operacion=="division":
        total=numero1 / numero2   

###################################################
#Programa principal



        