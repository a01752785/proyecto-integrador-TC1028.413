#David Damian Galan
#A01752785
data=[]
dates=[]
"""
Recibir la cadena inicial
Inicializar numbers como lista vacia
Inicializar act_number como lista vacia
Inicializar i en 0
Mientras i sea menor a la longitud de la cadena inicial
    Limpiar el contenido de act_number
    Mientras i sea menor a la longitud de la cadena inicial 
    y el caracter de la cadena inicial en posicion i sea diferente a ','
        Agregar el caracter actual a act_number
        Avanzar i en 1
    #En este punto tenemos un nuevo numero de la cadena
    Inicializar number_str como cadena vacia
    Convertir act_number a cadena y guardarlo en number_str
    Convertir number_str a entero y agregarlo a la lista numbers
Regresar la lista numbers
"""
def splitElements(init_str):
    """
    splitNumbers recibe una cadena de numeros separada por comas 
    y la transforma en una lista con los numeros

    Parameters
    ----------
    init_str : str
        Cadena inicial con numeros.

    Returns
    -------
    numbers : list
        Lista con los numeros de la cadena.

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
        elements.append(act_var_str)
        i=i+1
    return elements

"""
Recibir name, row, column
Inicializar data como una lista vacia
Abrir el archivo y guardarlo en el objeto file
Declarar tmp_str e inicializarlo con la primera linea del archivo
Mientras tmp_str no este vacia
    Llamar a splitNumbers y agregar la lista que regresa a data
    Leer la siguiente linea del archivo y guardarla en tmp_str
Cerrar el archivo
Regresar data en indices row y column
"""
def readFile(name):
    """
    readFile recibe el nombre del archivo a leer y copia los datos en memoria

    Parameters
    ----------
    name : str
        Nombre del archivo a leer.
    row : int
        Indice de la fila del valor deseado.
    column : int
        Inidice de la columna del valor deseado.

    Returns
    -------
    int
        Valor deseado de acuerdo a los indices.

    """
    file=open(name)
    tmp_str=file.readline()
    dates=splitElements(tmp_str)
    while(tmp_str!=""):
        data.append(splitElements(tmp_str))
        tmp_str=file.readline()
        print(data[len(data)-1])
    file.close()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if(data[i][j]=='') data[i][j].

readFile("datos_covid19.csv")