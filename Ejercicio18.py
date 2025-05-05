
var = int(input("Introduzca un número: "))
var2 = 0
var3 = var + 101

while var < var3:
    if var >= 0:  # Ejemplo de uso del if: solo sumar si el número es positivo
        var2 += var
    else:
        print(f"Se ignoró el número negativo: {var}")
    var += 1

print("La suma del número y los 100 números siguientes (ignorando negativos) es:", var2)





