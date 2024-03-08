
archivo = open("../Unidad 3/Archivos/ejemplo.csv", "w")

listaNombre = [
    ["Clemente",78],
    ["Cristobal",32],
    ["Ana",35],
    ["Orozco",18],
    ["Jorge",99],
    ["Aquino",65],
    ["Badillo",23],
    ["Segovioano",56],
    ["Salazar",44],
    ["Eduardo",1],
    ["Natalia",12],
    ["Rodrigo",77],
    ["Miguel",68],
    ["Amando",22],
    ["Raul",11],
    ["Lexiss",3],
    ["Mariana",33],
    ["Angel",46],
    ["Emmanuel",90],
    ["Isaac",80],
    ["Sergio",58],
    ["Paniagua",19]
]

print(listaNombre)
for datosNombre in listaNombre:
    for dato in datosNombre:
        archivo.write(str(dato) + ",")
    archivo.write("\n")

archivo.flush()
archivo.close()
