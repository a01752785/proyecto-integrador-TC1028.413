#David Damian Galan
#A01752785
import os
import matplotlib.pyplot as pyplot
data=[]
dates=[]
"""
Recibir la cadena inicial
Inicializar elements como lista vacia
Inicializar act_var como lista vacia
Inicializar i en 0
Mientras i sea menor a la longitud de la cadena inicial
    Limpiar el contenido de act_number
    Mientras i sea menor a la longitud de la cadena inicial 
    y el caracter de la cadena inicial en posicion i sea diferente a 
    alguno de los siguientes caracteres: ',', '\"', '\n'
        Agregar el caracter actual a act_number
        Avanzar i en 1
    #En este punto tenemos un nuevo dato de la cadena
    Inicializar act_var_str como cadena vacia
    Convertir act_var a cadena y guardarlo en act_var_str
    Si la cadena act_var_str no esta vacia
        Agregar act_var_str a la lista elements
Regresar la lista elements
"""
def splitElements(init_str):
    """
    splitElements recibe una cadena de datos separada por comas 
    y la transforma en una lista con los datos

    Parameters
    ----------
    init_str : str
        Cadena inicial con datos.

    Returns
    -------
    numbers : list
        Lista con los datos de la cadena.

    """
    elements=[]
    act_var=[]
    i=0
    while(i<len(init_str)):
        act_var.clear()
        while(i<len(init_str) and init_str[i]!=',' and init_str[i]!='\"' and init_str[i]!='\n'):
            act_var.append(init_str[i])
            i=i+1
        act_var_str=""
        act_var_str=act_var_str.join(act_var)
        if(len(act_var_str)>0):
            elements.append(act_var_str)
        i=i+1
    return elements

"""
Recibir name
Inicializar data como una lista vacia global
Inicializar dates como una lista vacia global
Si ya se habia cargado el archivo
    Imprimir que el archivo ya se ha leido anteriormente
    Retornar la funcion
Intentar:
    Abrir el archivo y guardarlo en el objeto file
    Declarar tmp_str e inicializarlo con la primera linea del archivo
    Llamar a splitElements y guardar la lista que regresa en dates
    Eliminar el primer elemento en dates (informacion inservible)
    Eliminar el primer elemento en dates
    Eliminar el primer elemento en dates
    Mientras tmp_str no este vacia
        Llamar a splitElements y agregar la lista que regresa a data
        Leer la siguiente linea del archivo y guardarla en tmp_str
    Cerrar el archivo
    Imprimir lectura exitosa
    Para cada i en el rango [1,cantidad de filas de data)
        Para cada j en el rango[3,cantidad de columnas de data)
            Convertir data[i][j] a int
        Convertir data[i][1] a int
    Marcar que ya se ha leido el archivo
Excepcion de error de lectura:
    Imprimir error al leer el archivo, nombre incorrecto
"""
__file_loaded=False
def readFile(name):
    """
    readFile recibe el nombre del archivo a leer y copia los datos en memoria.
    Si ya se ha leido el archivo no hace nada.
    Si encuentra un error al leer aborta la ejecucion y retorna.
    Parameters
    ----------
    name : str
        Nombre del archivo a leer.

    Returns
    -------
    None.

    """
    global __file_loaded
    if(__file_loaded==True):
        print("Ya se ha leido el archivo anteriormente")
        return
    global data
    global dates
    data=[]
    dates=[]
    try:
        file=open(name)
        tmp_str=file.readline()
        dates=splitElements(tmp_str)
        dates.pop(0)
        dates.pop(0)
        dates.pop(0)
        while(tmp_str!=""):
            data.append(splitElements(tmp_str))
            tmp_str=file.readline()
        file.close()
        for i in range(1,len(data)):
            for j in range(3,len(data[i])):
                data[i][j]=int(data[i][j])
            data[i][1]=int(data[i][1])
        print("Lectura exitosa")
        __file_loaded=True
    except IOError:
        print("Error leyendo el archivo, nombre incorrecto")

def showPlot(x,y,title_str,ylabel_str):
    pyplot.ion()
    pyplot.plot(x,y)
    pyplot.title(title_str)
    pyplot.ylabel(ylabel_str)
    pyplot.xticks(dates,rotation='vertical')
    pyplot.margins(0.2)
    pyplot.show()

def perDayCases(row):
    global data
    global dates
    cases=[]
    for i in range(3,len(data[row])):
        cases.append(data[row][i])
    showPlot(dates,cases,f"Datos de {data[row][2]}","Casos diarios")

def cumulativeCases(row):
    global data
    global dates
    cases=[]
    for i in range(3,len(data[row])):
        ith_day_cases=data[row][i]
        if(len(cases)>0):
            ith_day_cases+=cases[i-4]
        cases.append(ith_day_cases)
    showPlot(dates,cases,f"Datos de {data[row][2]}","Casos acumulados")

def dailyPercentage(row):
    global data
    global dates
    cases=[]
    for i in range(3,len(data[row])):
        ith_day_cases=data[row][i]
        if(len(cases)>0):
            ith_day_cases+=cases[i-4]
        cases.append(ith_day_cases)
    
    percentage=[]
    percentage.append(0)
    for i in range(1,len(cases)):
        if(cases[i]==0):
            percentage.append(0)
        else:
            advance=0
            if(cases[i-1]==0):
                advance=cases[i]
            else:
                advance=cases[i]/cases[i-1]*100-100
            percentage.append(advance)
    showPlot(dates,percentage,f"Datos de {data[row][2]}",
             "Porcentaje de aumento respecto al acumulado del dia anterior")

def showPieChart(percentage,labels,title_str):
    pyplot.ion()
    pyplot.pie(percentage,labels=labels,autopct='%1.1f%%')
    pyplot.title(title_str)
    pyplot.show()

def stateCasesPieChart():
    global data
    labels=[]
    cases=[]
    for i in range(1,len(data)-1):
        labels.append(data[i][2])
    totalCases=0
    for i in range(1,len(data)-1):
        stateCases=0
        for j in range(3,len(data[i])):
            stateCases+=data[i][j]
        cases.append(stateCases)
        totalCases+=stateCases
    percentage=[]
    for i in range(0,len(cases)):
        percentage.append(cases[i]/totalCases*100)
    showPieChart(percentage, labels, 
                 "Porcentaje por estado respecto al total de casos en el pais")

def healthy_vs_infected_people(row):
    global data
    population=data[row][1]
    infected=0
    for i in range(3,len(data[row])):
        infected+=data[row][i]
    healthy=population-infected
    print(f"{data[row][2]} tiene una poblacion de {population}")
    print(f"de los cuales {infected} estan infectados y {healthy} estan no infectados")
    showPieChart([healthy,infected], ["No infectados","Infectados"], 
                 f"Porcentaje de personas infectadas y no infectadas en {data[row][2]}")

def nationalData():
    id_data=33
    print("DATOS NACIONALES\n")
    print("1. Mostrar casos por dia")
    print("2. Mostrar casos acumulados")
    print("3. Mostrar porcentaje de aumento diario")
    print("4. Mostrar porcentaje de cada estado respecto al total")
    print("5. Mostrar porcentaje de personas infectadas y no infectadas")
    print("6. Regresar")
    op=input()
    Escape=False
    if(op=='1'):
        perDayCases(id_data)
    elif(op=='2'):
        cumulativeCases(id_data)
    elif(op=='3'):
        dailyPercentage(id_data)
    elif(op=='4'):
        stateCasesPieChart()
    elif(op=='5'):
        healthy_vs_infected_people(id_data)
    elif(op=='6'):
        Escape=True
    else:
        print("Operacion no reconocida")
    print("Presione una tecla para continuar...")
    input()
    if(not Escape):
        nationalData()

def stateData(id_data):
    global data
    print(f"DATOS POR ESTADO: {data[id_data][2]}\n")
    print("1. Mostrar casos por dia")
    print("2. Mostrar casos acumulados")
    print("3. Mostrar porcentaje de aumento diario")
    print("4. Mostrar porcentaje de personas infectadas y no infectadas")
    print("5. Regresar")
    op=input()
    Escape=False
    if(op=='1'):
        perDayCases(id_data)
    elif(op=='2'):
        cumulativeCases(id_data)
    elif(op=='3'):
        dailyPercentage(id_data)
    elif(op=='4'):
        healthy_vs_infected_people(id_data)
    elif(op=='5'):
        Escape=True
    else:
        print("Operacion no reconocida")
    print("Presione una tecla para continuar...")
    input()
    if(not Escape):
        stateData(id_data)

def selectState():
    global data
    print("DATOS POR ESTADO\n")
    print("Por favor seleccione el estado para el cual desea consultar datos")
    for i in range(1,len(data)-1):
        print(f"{i}. {data[i][2]}")
    id_data=input()
    if(not id_data.isnumeric()):
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
        selectState()
    id_data=int(id_data)
    if(id_data<1 or id_data>32):
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
        selectState()
    return id_data

def main():
    os.system("cls")
    print("BIENVENIDO AL SISTEMA DE CONSULTA DE DATOS DE COVID-19 EN MEXICO\n")
    print("POR FAVOR SELECCIONE UNA OPCION\n")
    print("1. Leer el archivo con datos")
    print("2. Acceder a datos nacionales")
    print("3. Acceder a datos por estado")
    print("4. Salir")
    os.system("pause")
    op=input()
    Escape=False
    if(op=='1'):
        print("Por favor ingrese el nombre del archivo con datos")
        name=input()
        readFile(name)
        print("Presione una tecla para continuar...")
        input()
    elif(op=='2'):
        nationalData()
    elif(op=='3'):
        id_data=selectState()
        stateData(id_data)
        pass
    elif(op=='4'):
        Escape=True
    else:
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
    if(not Escape):
        main()
    
main()