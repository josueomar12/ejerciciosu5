import re


def pedirNumeroEntero():

    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Escribe un numero de las siguientes instrucciones: "))
            correcto = True
        except ValueError:
            print("Error, no elegiste la opcion correcta")

    return num


salir = False
opcion = 0

while not salir:
    print ("------------------LENGUAJES Y AUTOMATAS----------------------")
    print("")
    print("Alumno: josue omar pech un")
    print("")
    print("1. Sentencia de asignación. ")
    print("2. Operaciones aritméticas básicas")
    print("3. Expresiones booleanas básicas")
    print("4. Formulas más complejas del tipo c = a op ( b op d)")
    print("5. El encabezado de estructura de control. if, while, for, etc")
    print("6. Salir")


    print("Elige una opcion")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        print("Sentencia de asignación. ")
        f = open (
            "ejemplos.txt"
        ).read() 
        ExpReg = r'([a-z0-9]+\s*[=]+\s*[a-z0-9+]+)'  
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print(exp)

    elif opcion == 2:
        print ("Operaciones aritméticas básicas")
        f = open(
            "ejemplos.txt"
        ).read()
        ExpReg = r'([A-Za-z0-9-_]+\s*[=]+\s*[A-Za-z0-9-_|0-9.0-9]+\s*[\+,\-,\*,\/,\%]+\s*[A-Za-z0-9-_|0-9.0-9]+)'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)
           
    elif opcion == 3:
        print ("Expresiones booleanas básicas")
        f = open(
            "ejemplos.txt"
        ).read()
        ExpReg = r'([A-Za-z0-9]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)

    elif opcion == 4:
        print("Formulas más complejas del tipo c = a op ( b op d)")    
        f = open(
            "ejemplos.txt"
        ).read()
        ExpReg = r'([A-Za-z0-9]+\s*=+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]\s*[(]+\s*[A-Za-z0-9]+\s*[|<|>|!|<=|>=|\+|\-\*\/]+\s*[A-Za-z0-9]+\s*[)])'
        exp = re.findall(ExpReg, f, flags=re.MULTILINE)
        print (exp)

    elif opcion == 5:
        print("El encabezado de estructura de control. if, while, for, etc")
        f = open(
            "ejemplos.txt"
        ).read()
        ExpRegIf = r'(if+\s*[A-Za-z0-9-]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-]+\s*:)'
        ExpRegWhile = r'(while+\s*[A-Za-z0-9-_]+\s*[|<|>|!|<=|>=]=+\s*[A-Za-z0-9-_]+\s*:)'
        ExpRegFor = r'(for+\s*[A-Za-z0-9-_]+\s*[in]+\s*[A-Za-z0-9-_]+\s*:)' 
        expIf = re.findall(ExpRegIf, f, flags=re.MULTILINE)
        expWhile = re.findall(ExpRegWhile , f, flags=re.MULTILINE)
        expFor = re.findall(ExpRegFor, f, flags=re.MULTILINE)
        print (expIf)
        print("")
        print (expWhile)
        print("")
        print (expFor)

    elif opcion == 6:
        salir = True
    else:
        print("Introduce un numero entre el rango 1 y 6")


