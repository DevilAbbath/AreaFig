import math
import AreaCuadrado
import AreaTriangulo

print ("Seleccione la operacion")
print ("1. Suma de 2 numeros")
print ("2. Area de una figura")
print ("3. Area de un Triangulo Sierpinski")

option = float(input("Su opcion: "))

if option == 1:
   print ("Sumatoria de 2 numeros")
   valor1 = int(input("Ingrese valor 1: "))
   valor2 = int(input("Ingrese valor 2: "))
   result = valor1 + valor2

   print (f'El valor de la suma es de {math.ceil(result)}')

elif option == 2:
   print ("Seleccione su figura")
   print ("1. Cuadrado")
   print ("2. Triangulo")

   figure = float(input("Figura: "))

   if figure == 1:
      print ("Indique valor de uno de los lados del Cuadrado")
      lado = float(input("Longitud del lado: "))
      area = AreaCuadrado.areacuadrado(lado)

      print (f'El area del cuadrado es de: {math.ceil(area)}m2')

   elif figure == 2:
      print ("Indique base y altura del triangulo")
      base = float(input("Base: "))
      altura = float(input("Altura: "))
      area = AreaTriangulo.areatriangulo(base, altura)

      print (f'El area del triangulo es de: {math.ceil(area)}m2')

   else:
      print ("option Invalida")

elif option == 3:
   print ("Sierpinski")
else: 
   print ("option Invalida")
