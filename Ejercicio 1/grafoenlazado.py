import numpy as np
from nodo import Nodo
class Grafo:
    __tabla=None
    __vertices=[]
    def __init__(self,vertices):
        self.__vertices=vertices
        self.__tabla= np.full(5,None)
        for i in range(len(self.__tabla)):
            nodo=Nodo(self.__vertices[i])
            self.__tabla[i]=nodo
    def Insertar(self,elemento,elemento1):
        band=True
        i=0
        while(i<len(self.__vertices) and band):
            if self.__tabla[i].getElemento() == elemento:
                band=False
            else:
                i+=1

        if self.__tabla[i].getElemento() == elemento:
                nodo=Nodo(elemento1)
                self.__tabla[i].setSig(nodo)
                print("insertado!")
        else:
            print("No se encontro el vertice para enlazarlo!")
    def Recorrido(self,nodo):
        lista=[]
        nodo=nodo.getSig()
        while(nodo!=None):
            lista.append(self.Buscar(nodo.getElemento()))
            nodo=nodo.getSig()
        print(lista)
        return lista

    def Buscar(self,elemento):
        i=0
        band=True
        while i<len(self.__vertices) and band:
            if self.__tabla[i].getElemento()==elemento:
                retorna=self.__tabla[i]
                band=False 
            else:
                i += 1
        return retorna

    def Camino(self,inicio,fin):
        i=self.Buscar(inicio)
        j=self.Buscar(fin)
        self.__Camino(i,j)

    def __Camino(self,inicio,fin,lista=[]):
        if inicio.getElemento()==fin.getElemento():
            return print(lista)
        else:
            if inicio != None and inicio.getElemento() not in lista:
                print("if", inicio.getElemento())
                lista.append(inicio.getElemento())
                for i in self.Recorrido(inicio):
                    print("for", i.getElemento())
                    self.__Camino(i,fin,lista)
            else:
                print("else", inicio.getElemento())
                self.__Camino(inicio.getSig(),fin,lista)

if __name__=='__main__':

    grafo=Grafo([1,2,3,4,5])
    grafo.Insertar(1,2)
    grafo.Insertar(2,3)
    grafo.Insertar(3,4)
    grafo.Insertar(4,5)
    grafo.Insertar(4,2)
    grafo.Camino(1,5)
