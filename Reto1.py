#______________RETO1____________

# Ingreso de fecha:
# Para que los días y los meses que tengan 1 digito salgan con 1 cero antes se debe colocar .zfill(número de la cadena)
# en este caso la cadena es 2 para el mes y el día.

ano = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes: "))
dia = int(input("Ingrese el dia: "))


# Ingreso de valor:
# Para que el valor flotante quede con los decimales que necesite, en este caso 2 ceros hay que colocar dentro de la
# función print el código ("%.2f" %variable) donde el 2 indica que se necesita 2 decimales después del punto


valor = float(input("Ingrese el valor: "))


# Valor literal:
# Hay una librería llamada num2words la cual convierte los números a literales:
# hay que instalar la librería num2words en pycharm
# luego hay que importarla de la siguiente manera (from num2words import num2words)
# por ultimo escribir num2words(el número o la variable que tenga el número, y el lenguaje)
# .upper() es para que el texto salga en mayusculas.


from num2words import num2words

lite = num2words(valor, lang = "es_CO").upper()


# Ingreso del nombre:

nom = input("Ingrese a nombre de quien: ")

# Se insatala la libreria PILLOW y se utiliza para abrir la imagen donde esta contenida la firma
# y se importa os para poder visualizar la imagen en el sistema operativo.

from PIL import Image
import os
im = Image.open("firma digital.jpg")

# Este paso se coloco para demostrar  la utilizacion del tipo de dato bool


firma = bool(int(input("¿Desea ingresar su firma? 0 = No / 1 = Si " )))


# Impresión de la consignación.

# Se utiliza saltos de linea (\n) y tabulaciones (\t) para organizar la presentacion de los datos.

print("\n")
print("Impresión de la consignación: ")
print("\n")
print("\t1. FECHA: " + str(ano) + "-" + str(mes).zfill(2) + "-" + str(dia).zfill(2))
print("\t2. VALOR: " + "%.2f" % valor + "$")
print("\t3. VALOR EN LETRAS: " + lite)
print("\t4. A NOMBRE DE QUIEN: " + nom)
print("\t5. FIRMA: "+ str(firma))
os.popen("firma digital.jpg")

