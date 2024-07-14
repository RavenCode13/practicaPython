def auxiliares():
    bandera01 = 0
    sumatoriaIngresos=0
    sumatoriaEgresos=0
    sumatoriaConCapital=float(input("Tiene algun capital ahorrado? nos ayudara a calcular mejor\n:::>>> "))
    return bandera01, sumatoriaIngresos, sumatoriaEgresos, sumatoriaConCapital

def inicioListas():
    ingresosNombres = []
    ingresosValor = []

    egresosNombres = []
    egresosValor = []

    metas = []
    metasCostos = []

    return ingresosNombres, ingresosValor, egresosNombres, egresosValor, metas, metasCostos

def menu():
    print("""
            ____________________________________________
            |                                           |
            |    BIENVENIDO A SISTEMA PARA CALCULAR     |
            |   SUS INGRESOS Y EGRESOS PARA  DEFINIR    |
            | EN CUANTO TIEMPO PODRA LOGRAR SUS METAS   |
            |___________________________________________|""")

def subMenu(sumatoriaIngresos, sumatoriaEgresos):
    print("""
SELECCIONE UNA OPCION (NUMERO)
(1) Ver Listas de Ingresos - (2) Agregar un Ingreso - (3) Eliminar un Ingreso
          
(4) Ver Listas de Egreso   - (5) Agregar un Egreso  - (6) Eliminar un Egreso
          
(7) Ver Listas de Metas    - (8) Agregar una Meta   - (9) Eliminar una Meta
          
(10) Salir
""")
    if sumatoriaIngresos>0:
        print(f"Tienes acumulado {sumatoriaIngresos}$ en solo ingresos")
    if sumatoriaEgresos>0:
        print(f"Tienes acumulado -{sumatoriaEgresos}$ en solo Egresos")
    while True:
        opcion = int(input("Ingrese la Opcion\n:::>>> "))
        if opcion>0 and opcion<11:
            break
        else:
            print("Opcion no valida")
    return opcion
    
def seccionarOpciones(opcion, sumatoriaIngresos, sumatoriaEgresos, ingresosNombres, ingresosValor, egresosNombres, egresosValor, metas, metasCostos):
    bandera = 0
    match opcion:
        case 1:
            opcion01(ingresosNombres, ingresosValor)
        case 2:
            sumatoriaIngresos = opcion02(ingresosNombres, ingresosValor, sumatoriaIngresos)
        case 3:
            sumatoriaIngresos = opcion03(ingresosNombres, ingresosValor, sumatoriaIngresos)
        case 4:
            opcion04(egresosNombres, egresosValor)
        case 5:
            sumatoriaEgresos = opcion05(egresosNombres, egresosValor, sumatoriaEgresos)
        case 6:
            sumatoriaEgresos = opcion06(egresosNombres, egresosValor, sumatoriaEgresos)
        case 7:
            opcion07(metas, metasCostos)
        case 8:
            opcion08(metas, metasCostos)
        case 9:
            opcion09(metas, metasCostos)
        case 10:
            bandera = terminarCiclo()
        case _:
            print("FATAL ERROR!")
    if opcion==1 or opcion==4 or opcion==7:
        espera=input("Presione Enter para continuar o Ingrese cualquier dato\n:::>>>")
    return bandera, sumatoriaIngresos, sumatoriaEgresos

#(1) Ver Listas de Ingresos
def opcion01(ingresosNombres, ingresosValor):
    if len(ingresosNombres)==0:
        print("No hay ningun dato para imprimir")
    else:
        for pos in range(len(ingresosNombres)):
            print(f"#{pos+1} Ingreso: {ingresosNombres[pos]} Monto: {ingresosValor[pos]}")
#(2) Agregar un Ingreso
def opcion02(ingresosNombres, ingresosValor, sumatoriaIngresos):
    print("----------------------------------")
    while True:
        dato01=input("De que se trata el ingreso a Cargar? (Nombre del ingreso)\n:::>>> ")
        dato02=float(input("Ingrese el monto que genera con ese Ingreso:\n:::>>> "))
        if dato01!="" and dato02>0:
            break
        else:
            print("Ingreso mal un dato:")
            if dato01=="":
                print("Error en el nombre del Ingreso")
            if dato02<1:
                print("Error en el monto del ingreso")
    sumatoriaIngresos+=dato02
    ingresosNombres.append(dato01)
    ingresosValor.append(dato02)
    return sumatoriaIngresos
#(3) Eliminar un Ingreso
def opcion03(ingresosNombres, ingresosValor, sumatoriaIngresos):
    opcion01(ingresosNombres, ingresosValor)
    if len(ingresosNombres)>0:
        while True:
            indice=int(input("Que indice quiere borrar?"))
            print(indice)
            if indice>0 and indice<len(ingresosNombres)+1:
                break
            else:
                print("Ingreso mal el indice a borrar")
        sumatoriaIngresos-=ingresosValor[indice-1]
        ingresosNombres.pop(indice-1)
        ingresosValor.pop(indice-1)
        return sumatoriaIngresos
#(4) Ver Listas de Egreso
def opcion04(egresosNombres, egresosValor):
    if len(egresosNombres)==0:
        print("No hay ningun dato para imprimir")
    else:
        for pos in range(len(egresosNombres)):
            print(f"#{pos+1} Ingreso: {egresosNombres[pos]} Monto: {egresosValor[pos]}")
#(5) Agregar un Egreso
def opcion05(egresosNombres, egresosValor, sumatoriaEgresos):
    print("----------------------------------")
    while True:
        dato01=input("De que se trata el egreso a Cargar? (Nombre del egreso)\n:::>>> ")
        dato02=float(input("Ingrese el monto que genera con ese egreso:\n:::>>> "))
        if dato01!="" and dato02>0:
            break
        else:
            print("Ingreso mal un dato:")
            if dato01=="":
                print("Error en el nombre del Egreso")
            if dato02<1:
                print("Error en el monto del Egreso")
    sumatoriaEgresos+=dato02
    egresosNombres.append(dato01)
    egresosValor.append(dato02)
    return sumatoriaEgresos
#(6) Eliminar un Egreso
def opcion06(egresosNombres, egresosValor, sumatoriaEgresos):
    opcion04(egresosNombres, egresosValor)
    if len(egresosNombres)>0:
        while True:
            indice=int(input("Que indice quiere borrar?"))
            print(indice)
            if indice>0 and indice<len(egresosNombres)+1:
                break
            else:
                print("Ingreso mal el indice a borrar")
        sumatoriaEgresos-=egresosValor[indice-1]
        egresosNombres.pop(indice-1)
        egresosValor.pop(indice-1)
        return sumatoriaEgresos
#(7) Ver Listas de Metas
def opcion07(metas, metasCostos):
    if len(metas)==0:
        print("No hay ningun dato para imprimir")
    else:
        for pos in range(len(metas)):
            print(f"#{pos+1} Ingreso: {metas[pos]} Monto: {metasCostos[pos]}")
#(8) Agregar una Meta
def opcion08(metas, metasCostos):
    print("----------------------------------")
    while True:
        dato01=input("De que se trata la meta a cumplir?\n:::>>> ")
        dato02=float(input("Ingrese el monto que necesita para completar la meta:\n:::>>> "))
        if dato01!="" and dato02>0:
            break
        else:
            print("Ingreso mal un dato:")
            if dato01=="":
                print("Error en el nombre de la Meta")
            if dato02<1:
                print("Error en el monto del Meta")
    metas.append(dato01)
    metasCostos.append(dato02)
#(9) Eliminar una Meta
def opcion09(metas, metasCostos):
    opcion07(metas, metasCostos)
    if len(metas)>0:
        while True:
            indice=int(input("Que indice quiere borrar?"))
            print(indice)
            if indice>0 and indice<len(metas)+1:
                break
            else:
                print("Ingreso mal el indice a borrar")
        metas.pop(indice-1)
        metasCostos.pop(indice-1)
#(10) Salir
def terminarCiclo():
    while True:
        respuesta = input("Desea continuar? (SI) para continuar, (NO) para Finalizar\n:::>>> ").upper()
        if respuesta == "SI":
            bandera=0
            break
        elif respuesta == "NO":
            bandera=1
            break
        else:
            print("\nComando no Permitido\n")

    return bandera

def calculos(metas, metasCostos, sumatoriaIngresos, sumatoriaEgresos, sumatoriaConCapital):
    for pos in range(len(metas)):
        if sumatoriaConCapital>metasCostos[pos]:
            print(f"Usted tiene posibilidad actualmente para comprar <{metas[pos]}>")
        else:
            paraAhorrar=sumatoriaIngresos-sumatoriaEgresos
            cantMeses01=metasCostos[pos]/paraAhorrar
            metasMenosCapital=metasCostos[pos]-sumatoriaConCapital
            cantMeses02=metasMenosCapital/paraAhorrar
            print(f"""
Para lograr la meta <{metas[pos]}> que tiene un costo de <{metasCostos[pos]}>
Tienes la capacidad de ahorrar cada mes de {paraAhorrar}$
Si se comienza ahorrando de cero lo conseguiras en {cantMeses01} meses
Pero tienes ahorrado {sumatoriaConCapital}$ entonces lo podras lograr en {cantMeses02} meses
""")

#CuerpoPrincipal
menu()
bandera01, sumatoriaIngresos, sumatoriaEgresos, sumatoriaConCapital = auxiliares()
ingresosNombres, ingresosValor, egresosNombres, egresosValor, metas, metasCostos = inicioListas()
while bandera01 ==0:
    opcion = subMenu( sumatoriaIngresos, sumatoriaEgresos)
    bandera01, sumatoriaIngresos, sumatoriaEgresos = seccionarOpciones(opcion, sumatoriaIngresos, sumatoriaEgresos, ingresosNombres, ingresosValor, egresosNombres, egresosValor, metas, metasCostos)
calculos(metas, metasCostos, sumatoriaIngresos, sumatoriaEgresos, sumatoriaConCapital)