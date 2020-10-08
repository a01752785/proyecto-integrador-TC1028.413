#David Damian Galan
#A01752785
import os
import sys
import matplotlib
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
Inicializar data como una lista 
Si ya se habia cargado el archivo
    Imprimir que el archivo ya se ha leido anteriormente
    Retornar la funcion
Intentar:
    Abrir el archivo y guardarlo en el objeto file
    Declarar tmp_str e inicializarlo con la primera linea del archivo
    Llamar a splitElements y guardar la lista que regresa en dates
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
    data=[]
    try:
        file=open(name)
        tmp_str=file.readline()
        dates=splitElements(tmp_str)
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

def perDayGraphics(id_data):
    

def nationalData():
    pass


def main():
    os.system("cls")
    print("BIENVENIDO AL SISTEMA DE CONSULTA DE DATOS DE COVID-19 EN MEXICO\n")
    print("POR FAVOR SELECCIONE UNA OPCION\n")
    print("1. Leer el archivo con datos")
    print("2. Acceder a datos nacionales")
    print("3. Acceder a datos por estado")
    print("4. Salir")
    op=input()
    if(op=='1'):
        print("Por favor ingrese el nombre del archivo con datos")
        name=input()
        readFile(name)
        print("Presione una tecla para continuar...")
        input()
        main()
    elif(op=='2'):
        print(len(data))
        perDayGraphics(33)
    elif(op=='3'):
        pass
    elif(op=='4'):
        pass
    else:
        print("Operacion no reconocida")
        print("Presione una tecla para continuar...")
        input()
        main()

file_loaded=False        
main()