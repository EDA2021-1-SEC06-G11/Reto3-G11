"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    analyzer = {'features': None,
                'dataIndex': None}
    
    analyzer['features'] = lt.newList('ARRAY_LIST')

    analyzer['instrumentalness'] = om.newMap(omaptype='BST')

    analyzer['liveness'] = om.newMap(omaptype='BST')

    analyzer['speechiness'] = om.newMap(omaptype='BST')

    analyzer['danceability'] = om.newMap(omaptype='BST')

    analyzer['valence'] = om.newMap(omaptype='BST')

    analyzer['loudness'] = om.newMap(omaptype='BST')

    analyzer['tempo'] = om.newMap(omaptype='BST')

    analyzer['acousticness'] = om.newMap(omaptype='BST')

    analyzer['energy'] = om.newMap(omaptype='BST')

    return analyzer



# Funciones para agregar informacion al catalogo
def addMusic(analyzer,music):

    lt.addLast(analyzer['features'],music)
    updateIndex(analyzer['instrumentalness'],music, 'instrumentalness')
    updateIndex(analyzer['liveness'],music, 'liveness')
    updateIndex(analyzer['speechiness'],music,'speechiness')
    updateIndex(analyzer['danceability'],music,'danceability')
    updateIndex(analyzer['valence'],music,'valence')
    updateIndex(analyzer['loudness'],music,'loudness')
    updateIndex(analyzer['tempo'],music,'tempo')
    updateIndex(analyzer['acousticness'],music,'acousticness')
    updateIndex(analyzer['energy'],music,'energy')

    return analyzer

def updateIndex(map, music, name):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    num = music[name]
    entry = om.get(map, num)
    if entry is None:
        datentry = newDataEntry(music)
        om.put(map, num, datentry)
    else:
        datentry = me.getValue(entry)
    addIndex(datentry, music)
    return map


def addIndex(datentry, music):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstmusic']

    lt.addLast(lst, music)
    
    return datentry

def newDataEntry(crime):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'lstmusic': None}
    entry['lstmusic'] = lt.newList('SINGLE_LINKED')
    
    return entry
    
# Funciones para creacion de datos

# Funciones de consulta

def getMusicByRange(analyzer,minimo,maximo,car):

    lst = om.values(analyzer[car],minimo,maximo)
    num = 0
    for i in lt.iterator(lst):
        num += lt.size(i['lstmusic'])
       
    return num


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
