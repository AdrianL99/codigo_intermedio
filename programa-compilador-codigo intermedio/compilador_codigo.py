import re
#AQUI USAMOS EXPRESIONES REGULARES PARA QUE EL PROGRAMA PUEDA LEER LOS PRIMEROS 2 EJERCICIOS
regex1 = r"^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+$"
regex2 = r"^\w+\s\=\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+\s[+*-/]\s\w+$"


#DECLARAMOS 4 VARIABLES PARA LUEGO USARLAS AUTOINCREMENTABLES
cont=0
cont1=0
cont2=0
cont3=0

#AQUI DECLARAMOS OPCION = INPUT PARA PODER LEER DATOA DEL TECLADO Y USAMOS LA SENTENCIA IF PARA PODER DIVIDIR EL CODIGO EN 3 PARTES Y USAMOS UN PEQUEÑO MENU
opcion=int(input("menu: \n 1-RESOLVER EJERCICIO 1 \n 2-RESOLVER EJERCICIO 2 \n 3-RESOLVER EJERCICIO 3 \n 0-SALIR \n"))

#OPCION 1 == SE EJECUTA EL CODIGO DENTRO DEL IF UNICAMENTE
if opcion ==1:
    f = open('expresiones1.txt', 'r') # AQUI SE USA ESTE CODIGO PARA PODER USAR EL ARCHIVO CORRESPONDIENTE A ESTE EJERCICIO
    dato = f.read()
    concidencias = len(re.findall(regex1, #SE USA FINDALL PARA RECORRER DENTRO DEL ARCHIVO DE TEXTO MEDIANTE LAS EXPRESIONES REGULARES
                                  dato))
    if concidencias >= 1:
        dato_div = dato.split()
   #SE USA FOR PARA PODER CHEQUEAR LA EXPRESION REGULARES
        for i in dato_div:
            cont = cont + 1
            if i == "/": # if==/ se usa para poder analizar en caso que la expresion tenga el simbolo de division y en el print se crean las variables temporales
                print("_t1= " + dato_div[cont - 2] + " / " + dato_div[cont])
                #se usa de igual manera if==* para analizar en caso que la expresion tenga el simbolo de multiplicacion y se crean las variables temporales
            if i == "*":
                print("_t1= " + dato_div[cont - 2] + " * " + dato_div[cont])

        for i in dato_div:
            cont1 = cont1 + 1
            # SE USA EL IF==+ PARA ANALIZAR EN CASO QUE LA EXPRESION TENGA EL SIMBOLO + Y EN LOS PRINT SE CREAN LAS VARIABLES TEMPORALES
            if i == "+":
                if cont1 == 4:
                    #se crean las variables temporales y se imprimen
                    print("_t2= " + dato_div[cont1 - 2] + " + " + "_t1")
                    print("x = _t2")
                if cont1 == 6:
                    # se crean las variables temporales y se imprimen
                    print("_t2= " + "_t1 " + " + " + dato_div[6])
                    print("x = _t2")
                    # SE USA EL IF==- PARA ANALIZAR EN CASO QUE LA EXPRESION TENGA EL SIMBOLO +- Y EN LOS PRINT SE CREAN LAS VARIABLES TEMPORALES
            if i == "-":
                if cont1 == 4:
                    # se crean las variables temporales y se imprimen
                    print("_t2= " + dato_div[cont1 - 2] + " - " + "_t1")
                    print("x = _t2")
                if cont1 == 6:
                    # se crean las variables temporales y se imprimen
                    print("_t2= " + "_t1 " + " - " + dato_div[6])
                    print("x = _t2")


#OPCION==2 se ejecuta cuando la opcion que ingrese sea 2 y corresponde al ejercicio 2
elif opcion==2:
    #se abre el archivo .txt y se lee, como python es un poco mas flexible no tiene problemas en que declaremos el otro archivo .txt en la variable dato que usamos anteriormente
    f = open('expresiones2.txt', 'r')
    dato = f.read()
    #se us el findall para analizar las expresiones ingresadas junto con las expresiones regulares anteriormente declarada
    coincidencias1 = len(re.findall(regex2,
                                    dato))
    if coincidencias1 >= 1:
        dato_div = dato.split()
#SE USA EL CICLO FOR PARA ANALIZAR LA EXPRESION REGULAR Y PODER RECORRERLO Y SE CREAN LAS VARIABLES TEMPORALES
        for i in dato_div:
            cont = cont + 1
            #I==/ EN CASO DE QUE EN LA EXPRESION  ESTE SIMBOLO DE DIVISION Y SE CREAN LAS VARIABLES TEMPORALES
            # TODOS LOS IF SON PARA ANALIZAR SIMBOLOS EN DADO CASO QUE ESTA TENGA EL SIMBOLO / QUE ESTA EN EL LADO IZQUIERDO DE DICHA EXPRESION
            if i == "/":
                print("_t1 = " + dato_div[cont - 2] + " " + dato_div[cont - 1] + " " + dato_div[cont])
                # DE NUEVO SE USA EL FOR PARA PODER ANALIZAR EL ARCHIVO
                for i in dato_div:
                    cont2 = cont2 + 1
                    #IF==* EN CASO DE QUE LA EXPRESION ESTE EL SIMBOLO DE MULTIPLICACION Y DE IGUAL FORMA SE CREAN LAS VARIABLES TEMPORALES
                    if i == "*":
                        #se imprimen las variables temporales
                        print("_t2 = " + dato_div[cont2 - 2] + " " + dato_div[cont2 - 1] + " " + dato_div[cont2])

                        for i in dato_div:
                            cont3 = cont3 + 1
                            if i == "+" or i == "-":
                                print("_t3 = _t1 " + dato_div[cont3 - 1] + " _t2")

                                break
                break
                #ELIF==* SE EJECUTA EN DADO CASO DE QUE LA EXPRESION TENGA EL SIMBOLO *
                #DENTRO DEL ELIF SE HACEN LOS CASOS DIFERENTE CON LOS DIFERENTES SIMBOLOS QUE SON + - * /
            elif i == "*":
                #SE CREAN LAS VARIABLES TEMPORALES para posteriormente imprimirlos
                print("_t1 = " + dato_div[cont - 2] + " " + dato_div[cont - 1] + " " + dato_div[cont])
                #DE NUEVO EL CICLO FOR PARA RECORRES LA EXPRESION
                for i in dato_div:
                    cont2 = cont2 + 1
                    #EN DADO CASO QUE EN LA EXPRESION SE ENCUENTRA EL SIMBOLO /
                    if i == "/":
                        #SE CREAN LAS VARIABLES TEMPORALES para posteriormente imprimirlos
                        print("_t2 = " + dato_div[cont2 - 2] + " " + dato_div[cont2 - 1] + " " + dato_div[cont2])

                        # SE USA EL FOR PARA RECORRER EL ARCHIVO
                        for i in dato_div:
                            cont3 = cont3 + 1
                            # SE SIMPLIFICAN PARA NO HACER OTRO IF SE PONEN LAS 2 CONDICIONES MEDIANTE EL OR
                            if i == "+" or i == "-":
                                #SE CREAN LAS VARIABLES TEMPORES para posteriormente imprimirlos
                                print("_t3 = _t1 " + dato_div[cont3 - 1] + " _t2")
                                print("x=_t3")
                                break
                break

elif opcion == 3:
    #CABE RECALCAR QUE LA MANERA DE RESOLVER EL EJERCICIO 2 YA NO ES POR EXPRESIONES REGULARES DEBIDO A QUE SE NOS HIZO ALGO COMPLICADO ENCONTRAR EL TIPO DE EXPRESION REGULAR PARA ESTE TIPO DE EXPRESIONES
    f = open('expresiones3.txt', 'r') #SE ABRE EL ARCHIVO TXT
    #SE LEE EL ARCHIVO TXT
    dato = f.read()
    #SE CREA UN ARREGLO
    pila = []
    # SE DECLARA UNA VARIABLE = A DATO , QUE ES EL NOMBRE DEL ARCHIVO A ANALIZAR , PARA QUE EL PROGRAMA PUEDA ANALIZARLO
    expresion = (dato)
    #VARIABLE POSICION PARA PODER DESGLOZAR LAS EXPRESIONES Y CREAR LAS VARIABLES TEMPORALES
    posicion = -1
    #SE RECORRE EL ARCHIVO TXT
    for i in expresion:
        if i != " ":
            pila.append(i)

    #SE CREA LA VARIABLE TEMPORAL 0
    temporalCero = ""
    #FOR PARA RECORRER DENTRO DEL ARREGLO
    for i in pila:
        posicion += 1
        #IF==() PARA PODER LEER LOS PARENTESIS Y CREAR SUS VARIABLES TEMPORALES
        if i == "(" or i == ")":
            #SE CREA LA ESTRUCTURA DE LA TEMPORAL 0 POR MEDIO DE LAS POSICIONES DE LA EXPRESION DENTRO DEL ARREGLO O PILA Y SE CREA LA TEMPORAL 0 PARA POSTERIORMENTE SOLO IMPRIMIR LAS VARIABLES
            temporalCero = "_t0 = " + pila[posicion - 4] + " " + pila[posicion - 3] + " " + pila[posicion - 2] + " " + pila[posicion - 1] + " " + pila[
                posicion]

      #SE INICIA CON LA CREACION DE LA TEMPORAL 1
    temporalUno = ""
    # FOR PARA RECORRER LA EXPRESION
    for i in pila:
        #IF EN DADO CASO DE QUE LA EXPRESION CONTENGA LOS SIMBOLOS * /
        if i == "*" or i == "/":
            # en dado caso de que en la posicion 4 este el simbolo ( que deberia estarlo por el tipo de expresion que usa el ejercicio 3 , se crean las variables temporales
            if pila[4] == "(" :
                temporalUno = "_t1 =" + " _t0 " + pila[posicion - 5] + " " + pila[posicion  - 6] + " "
            else:
                #y en dado caso que no lo haya igual se crea el else para poder crear las variables temporales sin problema
                # se crea la estructura de la variable temporal 1
                temporalUno = "_t1 = " + pila[posicion  - 2] + " " + pila[posicion  - 3] + " " + "_t0"
     #se inicia con la creacion de la variable temporal 2
    temporalDos = ""
    # se recorre la expresion por medio del ciclo for
    for i in pila:
        #if==+ or - en caso de que la expresion tenga alguno de estos simbolos pueda analizarlo sin problema
        if i == "+" or i == "-":
            #id ==( en dado caso que la expresion tenga un inicio de parentesis para poder crear su variable temporal sin problemas
            if pila[4] == "(" :
                # se crea la estructura de la variable temporal en dado caso que tenga parentesis
                temporalDos = "_t2=" + " _t1 " + pila[posicion  - 7] + " " + pila[posicion  - 8] + " "
            else:
                #else en dado caso de que la expresion no cuente con parentesis para poder crear su variable temporal sin problema de igual forma
                temporalDos = "_t2 = " + pila[posicion ] + " " + pila[posicion  - 1] + " " + "_t1"
    # se imprime los datos de la variable temporal 0
    print(temporalCero)
    # se imprime los datos de la variable temporal 1
    print(temporalUno)
    # se imprime los datos de la variable temporal 2
    print(temporalDos)
    #se crea una variable con el nombre temporal 3 =_t2
    temporalTres = "_t2"
    # se crea la estructura de la ultima temporal que solo es donde se añade la temporal X=T2
    temporalTres = " " + " " + "X = " + temporalTres
    #se imprime la ultima temporal 3
    print(temporalTres)


else:
       print("PROGRAMA FINALIZADO")