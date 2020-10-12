# David Damian Galan
# A01752785
import os
import matplotlib.pyplot as pyplot
%matplotlib inline
data = []  # En esta matriz se guardan los datos del archivo .csv
dates = []
# En esta lista se guardan las cadenas con las fechas del archivo .csv
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


def split_elements(init_str):
    """
    split_elements recibe una cadena de datos separada por comas
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
    elements = []
    act_var = []
    i = 0
    while(i < len(init_str)):
        act_var.clear()
        while(i < len(init_str) and init_str[i] != ','
              and init_str[i] != '\"' and init_str[i] != '\n'):
            act_var.append(init_str[i])
            i = i + 1
        act_var_str = ""
        act_var_str = act_var_str.join(act_var)
        if(len(act_var_str) > 0):
            elements.append(act_var_str)
        i = i + 1
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
    Llamar a split_elements y guardar la lista que regresa en dates
    Eliminar el primer elemento en dates (informacion inservible)
    Eliminar el primer elemento en dates
    Eliminar el primer elemento en dates
    Mientras tmp_str no este vacia
        Llamar a split_elements y agregar la lista que regresa a data
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
__file_loaded = False
# Determina si ya se leyo el archivo con datos (True) o no (False)


def read_file(name):
    """
    read_file recibe el nombre del archivo a leer y copia los datos en memoria.
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
    if(__file_loaded):
        print("Ya se ha leido el archivo anteriormente")
        return
    global data
    global dates
    data = []
    dates = []
    try:
        file = open(name)
        tmp_str = file.readline()
        dates = split_elements(tmp_str)
        dates.pop(0)
        dates.pop(0)
        dates.pop(0)
        while(tmp_str != ""):
            data.append(split_elements(tmp_str))
            tmp_str = file.readline()
        file.close()
        for i in range(1, len(data)):
            for j in range(3, len(data[i])):
                data[i][j] = int(data[i][j])
            data[i][1] = int(data[i][1])
        print("Lectura exitosa")
        __file_loaded = True
    except IOError:
        print("Error leyendo el archivo, nombre incorrecto")


def show_plot(x, y, title_str, ylabel_str):
    """
    show_plot recibe listas con valores de los ejes x,y ,
    una cadena de titulo y una cadena del nombre del eje y,
    muestra en pantalla la grafica con estos datos.

    Parameters
    ----------
    x : list
        Datos del eje x.
    y : list
        Datos del eje y.
    title_str : str
        Titulo del grafico.
    ylabel_str : str
        Nombre del eje y.

    Returns
    -------
    None.

    """
    pyplot.ion()
    pyplot.plot(x, y)
    pyplot.title(title_str)
    pyplot.ylabel(ylabel_str)
    pyplot.xticks(dates, rotation='vertical')
    pyplot.margins(0.2)
    pyplot.show()


def per_day_cases(row):
    """
    per_day_cases recibe un indice de fila y grafica los casos diarios
    segun el indice.

    Parameters
    ----------
    row : int
        Indice de la fila en la que se encuentran los datos a graficar.

    Returns
    -------
    None.

    """
    global data
    global dates
    cases = []
    for i in range(3, len(data[row])):
        cases.append(data[row][i])
    show_plot(dates, cases, f"Datos de {data[row][2]}", "Casos diarios")


def cumulative_cases(row):
    """
    cumulative_cases recibe un indice de fila, calcula los casos acumulados
    en ese indice y los grafica.

    Parameters
    ----------
    row : int
        Indice de la fila en la que se encuentran los datos a graficar.

    Returns
    -------
    None.

    """
    global data
    global dates
    cases = []
    for i in range(3, len(data[row])):
        ith_day_cases = data[row][i]
        if(len(cases) > 0):
            ith_day_cases += cases[i - 4]
        cases.append(ith_day_cases)
    show_plot(dates, cases, f"Datos de {data[row][2]}", "Casos acumulados")


def daily_percentage(row):
    """
    daily_percentage recibe un indice de fila, calcula el porcentaje
    de aumento respecto al dia anterior segun ese indice, y los grafica.

    Parameters
    ----------
    row : int
        Indice de la fila en la que se encuentran los datos a graficar.

    Returns
    -------
    None.

    """
    global data
    global dates
    cases = []
    for i in range(3, len(data[row])):
        ith_day_cases = data[row][i]
        if(len(cases) > 0):
            ith_day_cases += cases[i - 4]
        cases.append(ith_day_cases)

    percentage = []
    percentage.append(0)
    for i in range(1, len(cases)):
        if(cases[i] == 0):
            percentage.append(0)
        else:
            advance = 0
            if(cases[i - 1] == 0):
                advance = cases[i]
            else:
                advance = cases[i] / cases[i - 1] * 100 - 100
            percentage.append(advance)
    show_plot(dates, percentage, f"Datos de {data[row][2]}",
              "Porcentaje de aumento respecto al acumulado del dia anterior")


def show_pie_chart(percentage, labels, title_str):
    """
    show_pie_chart recibe una lista con porcentajes, otra con etiquetas
    y una cadena de titulo, y crea una grafica de pastel con los datos.

    Parameters
    ----------
    percentage : list
        Porcentaje correspondiente a cada clase.
    labels : list
        Nombre que se le va a dar a cada clase.
    title_str : str
        Cadena con el titulo del grafico.

    Returns
    -------
    None.

    """
    pyplot.ion()
    pyplot.pie(percentage, labels=labels, autopct='%1.1f%%')
    pyplot.title(title_str)
    pyplot.show()


def state_cases_pie_chart():
    """
    state_cases_pie_chart calcula el porcentaje de casos respecto al total
    para cada estado y crea una grafica de pastel.

    Returns
    -------
    None.

    """
    global data
    labels = []
    cases = []
    for i in range(1, len(data) - 1):
        labels.append(data[i][2])
    totalCases = 0
    for i in range(1, len(data) - 1):
        stateCases = 0
        for j in range(3, len(data[i])):
            stateCases += data[i][j]
        cases.append(stateCases)
        totalCases += stateCases
    percentage = []
    for i in range(0, len(cases)):
        percentage.append(cases[i] / totalCases * 100)
    show_pie_chart(
        percentage,
        labels,
        "Porcentaje por estado respecto al total de casos en el pais")


def healthy_vs_infected_people(row):
    """
    healthy_vs_infected_people recibe un indice de fila y calcula
    la cantidad total de infectados y no infectados en esa fila,
    despues lo muestra en grafica de pastel.

    Parameters
    ----------
    row : int
        Indice de la fila en la que se encuentran los datos a graficar.

    Returns
    -------
    None.

    """
    global data
    population = data[row][1]
    infected = 0
    for i in range(3, len(data[row])):
        infected += data[row][i]
    healthy = population - infected
    print(f"{data[row][2]} tiene una poblacion de {population}")
    print(
        f"""de los cuales {infected} estan infectados 
        y {healthy} estan no infectados""")
    show_pie_chart([healthy, infected], ["No infectados", "Infectados"],
                   f"""Porcentaje de personas infectadas y 
                   no infectadas en {data[row][2]}""")


def national_data():
    """
    national_data es la interfaz de usuario que permite navegar por las
    opciones de datos nacionales.

    Returns
    -------
    None.

    """
    id_data = 33
    print("DATOS NACIONALES\n")
    print("1. Mostrar casos por dia")
    print("2. Mostrar casos acumulados")
    print("3. Mostrar porcentaje de aumento diario")
    print("4. Mostrar porcentaje de cada estado respecto al total")
    print("5. Mostrar porcentaje de personas infectadas y no infectadas")
    print("6. Regresar")
    op = input()
    Escape = False
    if(op == '1'):
        per_day_cases(id_data)
    elif(op == '2'):
        cumulative_cases(id_data)
    elif(op == '3'):
        daily_percentage(id_data)
    elif(op == '4'):
        state_cases_pie_chart()
    elif(op == '5'):
        healthy_vs_infected_people(id_data)
    elif(op == '6'):
        Escape = True
    else:
        print("Operacion no reconocida")
    if(not Escape):
        print("Presione una tecla para continuar...")
        input()
        national_data()


def state_data(id_data):
    """
    state_data es la interfaz de usuario que permite navegar por las opciones
    del estado con indice de fila id_data.

    Parameters
    ----------
    id_data : int
        Indice de la fila de los datos de ese estado.

    Returns
    -------
    None.

    """
    global data
    print(f"DATOS POR ESTADO: {data[id_data][2]}\n")
    print("1. Mostrar casos por dia")
    print("2. Mostrar casos acumulados")
    print("3. Mostrar porcentaje de aumento diario")
    print("4. Mostrar porcentaje de personas infectadas y no infectadas")
    print("5. Regresar")
    op = input()
    Escape = False
    if(op == '1'):
        per_day_cases(id_data)
    elif(op == '2'):
        cumulative_cases(id_data)
    elif(op == '3'):
        daily_percentage(id_data)
    elif(op == '4'):
        healthy_vs_infected_people(id_data)
    elif(op == '5'):
        Escape = True
    else:
        print("Operacion no reconocida")

    if(not Escape):
        print("Presione una tecla para continuar...")
        input()
        state_data(id_data)


def select_state():
    """
    select_state es la interfaz de usuario que permite seleccionar un estado
    para ver sus datos correspondientes.

    Returns
    -------
    id_data : int
        Indice de la fila del estado seleccionado.

    """
    global data
    print("DATOS POR ESTADO\n")
    print("Por favor seleccione el estado para el cual desea consultar datos")
    for i in range(1, len(data) - 1):
        print(f"{i}. {data[i][2]}")
    id_data = input()
    if(not id_data.isnumeric()):
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
        select_state()
    id_data = int(id_data)
    if(id_data < 1 or id_data > 32):
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
        select_state()
    return id_data


def main():
    """
    main() es la interfaz de usuario principal que comunica al usuario con
    las funciones de este sistema.

    Returns
    -------
    None.

    """
    os.system("cls")
    print("BIENVENIDO AL SISTEMA DE CONSULTA DE DATOS DE COVID-19 EN MEXICO\n")
    print("POR FAVOR SELECCIONE UNA OPCION\n")
    print("1. Leer el archivo con datos")
    print("2. Acceder a datos nacionales")
    print("3. Acceder a datos por estado")
    print("4. Salir")
    os.system("pause")
    op = input()
    Escape = False
    global __file_loaded
    if((op == '2' or op == '3') and not __file_loaded):
        print("""Error: no se puede acceder a esa funcion 
              porque no se ha leido el archivo""")
    elif(op == '1'):
        print("Por favor ingrese el nombre del archivo con datos")
        name = input()
        read_file(name)
    elif(op == '2'):
        national_data()
    elif(op == '3'):
        id_data = select_state()
        state_data(id_data)
    elif(op == '4'):
        Escape = True
    else:
        print("Operacion no reconocida")
    if(not Escape):
        print("Presione una tecla para continuar")
        input()
        main()


main()
