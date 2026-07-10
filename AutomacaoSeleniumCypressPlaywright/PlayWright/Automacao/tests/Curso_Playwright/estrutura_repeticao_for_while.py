for numero in range(1, 11):
    print(numero)
print("--------------------------------------------------------")
for numero in range(5):
    print("Execução!")
print("--------------------------------------------------------")
for numero in range(5):
    print("Execução!" + str(numero++1))
print("--------------------------------------------------------")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
print("--------------------------------------------------------")
contador = 0
while contador <= 10:
    print("Número: " + str(contador))
    contador += 1
print("--------------------------------------------------------")
status_codes = [200, 200, 500, 200]
for status in status_codes:
    if status == 200:
        continue
    print("Status diferente de 200!", status)