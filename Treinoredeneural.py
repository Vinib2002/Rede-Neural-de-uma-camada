# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:36:25 2022

@author: vini
"""

import numpy as np
'''logica and
entradas = np.array([[0,0],[0,1],[1,0],[1,1]])#Matriz com as duas entradas
saidas=np.array([0,0,0,1])#Arrays com as saidas, das matrizes
'''
entradas = np.array([[0,1],[1,0],[0,0],[1,1]])#Matriz com as duas entradas
saidas=np.array([0,0,0,1])#Arrays com as saidas, das matrizes
pesos=np.array([0.0,0.0])#Pesos
taxaAprendizagem=0.1#O quanto o algoritimo vai mudando a cada teste

def stepFunction(soma):#Função que define o valor 0 e 1
    if(soma>=1):
        return 1
    return 0
def calculaSaida(registro):#Calculo do somatorio
    s=registro.dot(pesos)#produto escalar
    return stepFunction(s)#Salva o valor obtido na stepfunction
def treinar():
    erroTotal=1
    while(erroTotal!=0):
        erroTotal=0
        for i in range(len(saidas)):
            saidaCalculada=calculaSaida(np.array(entradas[i]))
            erro= abs(saidas[i]- saidaCalculada)
            erroTotal+= erro
            for j in range(len(pesos)):
                pesos[j]=pesos[j]+(taxaAprendizagem)*entradas[i][j]*erro
                print('Peso atualizado:'+str(pesos[j]))
            print("Total de erros"+str(erroTotal))
treinar()
print("Redes neurais treinadas")
print(calculaSaida(entradas[0]))
print(calculaSaida(entradas[1]))
print(calculaSaida(entradas[2]))
print(calculaSaida(entradas[3]))