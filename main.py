import os,random
os.system ("cls")
PODER_MIN = 1
PODER_MAX = 20
poder_base = random.randint(PODER_MIN, PODER_MAX)
BONO_STARK = 2
BONO_LANNISTER = -3
BONO_TARGARYEN = 5
BONO_BARATHEON = 0
print(poder_base)
nombre = input("cual es tu nombre?\n")
flag = True


while flag:
    try:
        edad = int(input("cual es tu edad?\n"))
        flag = False
    except:
        print("ingresa un valor valido")
while True:
    casa = input("a que casa perteneces? puede ser la casa Stark, Lannister, Targaryen, Baratheon definela con la inicial de tu casa \n")
    casa = casa.upper()
    if  casa == "S" or casa == "L" or casa == "T" or casa == "B":
        break
    else:
        print("ingresa la casa en el formato correcto") 
        
        
if casa == "S":
    poder_final = poder_base + BONO_STARK
elif casa == "L":
    poder_final = poder_base + BONO_LANNISTER
elif casa == "T":
    poder_final = poder_base + BONO_TARGARYEN



if poder_final >= 20:
    resultado = "Victoria epica"
elif poder_final >= 10 and poder_final <= 19:
    resultado = "Victoria ajustada"
else:
    resultado = "Derrota"
    
    
print(f"nombre de jugador: {nombre}")
print(f"edad: {edad}")
print(f"casa seleccionada: {casa}")
print(f"poder base: {poder_base}")
print(f"poder final: {poder_final}")
print(f"resultado de la batalla: {resultado}")