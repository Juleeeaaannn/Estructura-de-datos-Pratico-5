from random import random
import numpy as np

class Grafo:
    __vertices=[]
    __matriz=None
    def __init__(self,vertices):
        self.__vertices=vertices
        d=len(vertices)
        self.__matriz=np.full((d,d),None)
    def Generar(self,elemento,elemento1):
        a=-1
        b=-1
        i=0
        band=True
        while(i<len(self.__vertices) and band):
            if self.__vertices[i]==elemento:
                a=i
            if self.__vertices[i]==elemento1:
                b=i
            if a!=-1 and b!=-1:
                band=False
            i+=1
        if a!=-1 and b!=-1:
            self.__matriz[a][b]=True
            self.__matriz[b][a]=True
        else: 
            print("No existe este vertice!")
    def GenerarAleatorio(self):
        for i in range(len(self.__vertices)):
            if random.randint(0,1)==0:
                self.Generar(i,i)
    def Mostrar(self):
        for i in range(len(self.__vertices)):
            for j in range(len(self.__vertices)):
                if i<=j:
                    print(i,j)
            print("--------")
if __name__=='__main__':
    grafo=Grafo(["A","B","C"])
    grafo.Mostrar()
    print()
    grafo.Generar("A","B")
    grafo.Mostrar()