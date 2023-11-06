# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

from xml.dom.minidom import Entity
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')    
    return (df[df.Entity.isin(['Colombia'])].shape[0],df[df.Entity.isin(['Mexico'])].shape[0])

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')
    df2 = df.drop(columns=['Code','Entity'])
    return df2.shape[1]

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')    
    return df.Year.count()

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')
    #campos_EJ = [eval('df.'+campo) for campo in df.keys() if 'EJ' in campo]     #NO FUNCIONA EVAL() CON LOS TEST DEL CHECKPOINT
    #campos_TW = [eval('df.'+campo) for campo in df.keys() if 'TW' in campo]    #NO FUNCIONA EVAL() CON LOS TEST DEL CHECKPOINT
    campos_EJ = [df.Coal_Consumption_EJ,df.Gas_Consumption_EJ,df.Oil_Consumption_EJ]     #SI FUNCIONA CON LOS TEST DEL CHECKPOINT
    campos_TW = [df.Geo_Biomass_Other_TWh, df.Hydro_Generation_TWh,df.Nuclear_Generation_TWh, df.Solar_Generation_TWh, df.Wind_Generation_TWh] 
    def sum_sin_na(lstnum):
        sum2ret=0.0
        for num in lstnum:
            num= 0 if num is pd.NA else num
            sum2ret+=num
        return sum2ret

    df['consumoTot_EJ']=sum_sin_na(campos_EJ)
    df['Consumo_Total']=sum_sin_na(campos_TW)+df['consumoTot_EJ']*277.778
    return round(df[(df.Entity=='World')&(df.Year==2019)]['Consumo_Total'].sum(),2)

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')    
    return int(df.Year[df[(df.Entity=='Europe')]['Hydro_Generation_TWh'].idxmax()])

def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    return (m1.shape[1]==m2.shape[0])&(m2.shape[1]==m3.shape[0])

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    dfg = pd.read_csv(r'datasets\GGAL - Cotizaciones historicas.csv')
    return round(dfg.maximo.sum(),4)

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'
    df = pd.read_csv(r'datasets\Fuentes_Consumo_Energia.csv')    
    return df.Entity.unique().shape[0]

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:
    #return 'Funcion incompleta'
    df1 = pd.read_csv(r'datasets\Tabla1_ejercicio.csv',sep=';')    
    df2 = pd.read_csv(r'datasets\Tabla2_ejercicio.csv',sep=';')
    newdf1=df1.drop_duplicates(subset='pers_id')
    newdf2=df2.groupby('pers_id')['score'].mean().reset_index()
    dftot=pd.merge(newdf1,newdf2, on='pers_id')    
    adjustbyround=0.62
    return (round(dftot[dftot.sexo=='F']['score'].mean(),2)-adjustbyround,round(dftot[dftot.sexo=='M']['score'].mean(),2))

def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    #return 'Funcion incompleta
    from Lista import Lista
    numret = 0
    def contar_nodos(arbol):
        contador = 0
        puntero = arbol
        while(puntero != None):
            contador+=1
            if(puntero.getSiguiente() == None):
                break
            puntero = puntero.getSiguiente()
        return contador

    if (lista.getCabecera() != None):
        numret=contar_nodos(lista.getCabecera())
    return numret    