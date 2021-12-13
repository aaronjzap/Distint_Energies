import numpy as np
import networkx as nx

def Crear_matriz(n,ws):
    matriz=np.zeros((n,n))
    edges=ws.edges()
    for e in edges:
        matriz[e[0]][e[1]]=1
        matriz[e[1]][e[0]]=1
    return matriz

 
 
def Energia_vertice(valores,vectores):
    vectores, w= np.linalg.qr(vectores)
    e_v=[]
    if len(valores)==1:
        for entrada in vectores:
            suma=Decimal(entrada*abs(valores))
    else:
        suma_total=0
        for i in range(0,len(valores)):
            suma=0
            for j in range (0,len(valores)):
                suma+=vectores[i,j]*vectores[i,j]*abs(valores[j])
            e_v.append(suma)
            suma_total+=suma
       
    return e_v
    
    
def Energia(matriz):
    x, v = np.linalg.eig(matriz)
    e=np.sum(np.abs(x))
    return e,x,v



def simple_energy(grafo, n):
    matriz = Crear_matriz(n,grafo)
    x= np.linalg.eigvals(matriz)
    e=np.sum(np.abs(x))
    return e
        

def energia2(graph, n, ET):
    energies = []
    for i in range(n):
      G = graph.copy()
      G.remove_node(i)
      e1= simple_energy(G, n)
      energies.append(ET-e1)

    return energies



def energia3(graph, n, ET):
    energies = []
    for i in range(n):
      G = graph.copy()
      N = list(G.neighbors(i))
      N.append(i)
      G.remove_nodes_from(N)
      e1= simple_energy(G, n)
      energies.append(ET-e1)

    return energies





if __name__== "__main__":
    n=10
    grafo =nx.random_tree(n)
    ET,x,v = Energia(Crear_matriz(n,grafo))
    EV = Energia_vertice(x,v)/ET
    S2 = energia2(grafo, n,ET)
    S3 = energia3(grafo, n,ET)
    print(np.corrcoef(S2, EV)[0][1], np.corrcoef(EV, S3)[0][1], np.corrcoef(S2, S3)[0][1])
