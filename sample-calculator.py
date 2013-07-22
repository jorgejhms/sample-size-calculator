# -- coding: utf-8 --
# Formula de tamaño de muestra
# Autor: Jorge Meneses <jorgejhms@gmail.com>
# Versión: 0.2
# Licencia: GPL versión 3
# Registro de cambios:
#   --Provee por defecto un grado de heterogeneidad
#   --Consulta al usuario si su margen de error es correcto si usa un valor superior a 0.5
#   --Corrige si el usuario ingresa un grado de confiabilidad diferente de 2 o 3
#   --Corregido error que no mostraba margen de error en el resultado

###Definición de funciones###
def muestra(N, p, q, z2, E2):
    "Calculo del tamaño de muestra"
    n = (z2*N*p*q)/(N*E2+z2*p*q)
    return n
    
def universo():
    "Obtiene el tamaño del universo del usuario"
    N = raw_input("\n¿Cual es el tamaño de tu Universo?\n> " )
    return int (N)

def hetero():
    "Obtiene el grado de heterogeneidad del usuario"
    hetero = raw_input("\n¿Cual es el grado de heterogeneidad de la población?\n(si tienes dudas presiona ENTER)\n> ")
    if hetero == "": 
        p = 0.5 #valor de heterogeniedad por defecto
    else:
        p = hetero
    return float (p)

def error():
    "Obtiene el margen de error del usuario"
    E = raw_input("\n¿Cual es el margen de error deseado?\n(No debería ser mayor a 0.05)\n> ")
    if float (E) > 0.05: #Consulta al usuario si su margen de error es mayor al recomendable
        print "\nTu margen de error es mayor al recomendable. ¿Seguro que deseas usarlo?"
        respuesta = raw_input("¿Si/No? > ")
        if respuesta == "No":
            return error() #return permite reiniciar la función
        elif respuesta == "Si":
            return float (E)
        else:
            print "\nNo entiendo tu respuesta..."
            print "\n...Volveré a preguntar"
            return error()
    else:
        return float (E)
    
def confiabilidad ():
    "Obtiene del usuario el grado de confiabilidad"
    z = raw_input("\n¿Cuál es la confiabiliad deseada?\n(escribir 3 para 99.73% de confiabilidad y 2 para 95,45% de confiabilidad)\n> ")
    if int (z) != 3 and int (z) != 2:
        print "\nNo entiendo que confiabilidad requieres.\n Vuelvela a escribir"
        return confiabilidad()
    else:
        return int (z)
         
###Mensaje de bienvenida###
print """
Bienvenidos al programa para determinar el tamaño de muestra.
Tras unos pequeños pasos determinaremos el tamaño de muestra adecuado para el universo que quieres estudiar
"""

###Aplicación de la formula###
N = universo()
p = hetero()
E = error()
z = confiabilidad()
q = 1 - p
z2 = z*z
E2 = E*E
n = muestra (N, p, q, z2, E2)

###Presentación de resultado al usuario###
print """
Para un universo de %r, una heterogeniedad de %r, un margen de error de %r y una confiabilidad de %r.
El tamaño de muestra debe ser %r\n""" % (N, p, E, z, n)
