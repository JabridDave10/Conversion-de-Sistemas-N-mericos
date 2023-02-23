hexdigits = '0123456789ABCDEF'

# Converir el número ingresado a base 10
numero = input("Ingrese el número que desea convertir:")
base = int(input("Ingrese la base del número:  "))
if base < 2 or base > 16:
    print("La base debe ser mayor o igual que 2 y menor o igual que 16.")
    exit()

base10 = 0
for i, digito in enumerate(reversed(numero)):
    if digito in hexdigits[:base]:
        base10 += int(digito, base) * (base**i)

        base_copia_1= base10

# Convertir el número dado a la base deseada
Basen = ""

base_deseada = int(input("Ingresa la base que deseas convertir el número recuerda que no puede ser menor a 2 o mayor que 16: "))
if base_deseada < 2 or base_deseada > 16:
    print("La base deseada debe ser mayor o igual que 2 y menor o igual que 16.")
    exit()

base10_copia = base10
while base10 > 0:
    Basen = hexdigits[base10 % base_deseada].upper() + Basen
    base10 = base10 // base_deseada

# Converir a Binario
binario = bin(base10_copia)[2:]

# Convertir a Decimal y Ascii

decimal = int(binario,2)
Ascii = chr(decimal)

# Cifrado Caesar

mensaje = Ascii.upper()
#mensaje = input("Ingresa el mensaje que deseas para cifrarlo a Caesar: ").upper()
direccion = int(input("Ingresa la dirección que deseas cifrar el mensaje (1 para derecha, -1 para izquierda): "))
desplazamiento = int(input("¿Cuanto casillas quieres desplazar el número: "))

#Comprobación
if abs(desplazamiento) > 26:
    raise Exception("El desplazamiento no puede ser mayor que la longitud del alfabeto (26) ni menor que su negativo")

# Cifrar
mensaje_cifrado = ""
for c in mensaje:
    if c.isalpha():
        mensaje_cifrado += chr((ord(c) - ord('A') + desplazamiento * direccion) % 26 + ord('A'))
    else:
        mensaje_cifrado += c

# Descifrar
mensaje_descifrado = ""
for c in mensaje_cifrado:
    if c.isalpha():
        mensaje_descifrado += chr((ord(c) - ord('A') - desplazamiento * direccion) % 26 + ord('A'))
    else:
        mensaje_descifrado += c

print("Número ingresado: ", numero, " en base", base)
print("Tu número en base 10 es: ", base_copia_1)
print("Tu número convertido a la base seleccionada es: ", Basen)
print("Tu número en binario es: ", binario)
print("Tu mensaje que deseas cifrar es ", mensaje," La cantidad de casillas ", desplazamiento)
print("Tu mensaje cifrado es: ", mensaje_cifrado)
print("Tu mensaje descifrado es: ", mensaje_descifrado)