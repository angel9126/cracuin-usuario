palabra1 = input("introduce primera palabra:")
palabra2 = input("introduce segunda palabra:")
palabra3 = input("introduce tercera palabra:")
if len(palabra1)  >=4 <=8:
 palabra1 = "X" + palabra1
if len (palabra2) >=4 <=8:
  palabra2 ="X" + palabra2
if len (palabra3) >=4 <=8:
  palabra3 = "X" + palabra3
contraseña = palabra1[0] + palabra2[0] + palabra3[0] + palabra1[1] + palabra2[1] + palabra3[1]
print(" la contraseña es:", contraseña);
contraseña_usuario = input ("introduce contraseña");
if len(contraseña_usuario) < len(contraseña):
 print("hacen Falta letras solo tienes", len(contraseña) - len(contraseña_usuario),"letras")
elif len(contraseña_usuario) > len(contraseña):
  print("sobran letras tiene solo tienes", len(contraseña_usuario) - len(contraseña),"letras")
elif contraseña_usuario == contraseña:
  print("contraseña correcta")
else:
  print("contraseña incorrecta")