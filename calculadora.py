personas = int(input("personas:"))
while personas > 0:
  n = input("su nombre por favor:")
  m = input("apellido paterno:")
  x = input("apellido materno:")
  e = int(input("su edad en años por favor:"))
  a = float(input("su altura en metros por favor:"))
  est = a 
  m = float (input("su masa en kilogramos por favor:"))
  IMC = m/est**2 
  if(e <18):
   print("usted es menor de edad")
  else:
   print("usted es mayor de edad")
   print("IMC: " + str(IMC))
  if IMC >= 0 and IMC <= 10.99 :
   print("delgadez severa")
  elif IMC >= 16.00 and IMC <= 16.99:
   print("delgadez moderada")
  elif IMC >= 17.00 and IMC <= 18.49:
   print("deslgadez leve")
  elif IMC >= 18.50 and IMC <= 24.99:
   print("normal") 
  elif IMC >= 25.00 and IMC <= 29.99:
   print("sobre peso")
  elif IMC >= 30.00 and IMC <= 34.99:
   print("obesidad leve")
  elif IMC >= 35.00 and IMC <= 39.00:
   print("obesidad media")
  elif IMC >= 40.00:
   print("obesidad morbida")