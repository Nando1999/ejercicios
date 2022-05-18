#Ingresamos un numero real puede ser positivo o negativo 
Comprobar = input("ingrese un numero ") # Ingresamos un numero 
numero = float(Comprobar)  # numero debe ser float 
if numero == 0:  # inniciamos el sentencia con if si numero es igual a cero imprime neutro 
 print("Neutro")  
elif numero < 0:  # si numero entero es menor que 0 imprime negativo 
 print ("es número negativo")
else:
 print("mnumero positivo") # O sino que nos imprima positivo
