telRegister = {}

while True:
    namn = input("Skriv in namn:")
    if namn in telRegister:
        print("Finns redan")
    else:
        telnr = input(f"Vilket telefonnummer har {namn}?")
        telRegister[namn] = telnr
        
    if len(telRegister) == 5:
        break

print("Telregister lookup")
while True:
    namn = input("Ange namn:")
    if namn in telRegister:
        telnr = telRegister[namn]
        print(f"Telnr:{telnr}")
    else:
        print("Finns ej i registret")        