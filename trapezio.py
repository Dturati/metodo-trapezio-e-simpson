#!/usr/bin/env python
# _*_ coding:UTF-8 _*_

"""
python 3
David Turati
implementação do metodo de integral numérica pela forma do trapezio

"""
# a equação deve ser mudada no arquivo Equação.py
from Equacao import *
from math import *

class Trapezio(object):
	vetor = []
	def __init__(self,h,i,n):
		print("Forma do trapezio")
		self.h = h
		self.i = i
		self.n = n

	def tamanho(self):
		temp = float(self.i)
		while(temp <= self.n):
			self.vetor.append(temp)
			temp = temp + self.h

	def calcula(self,equacao):
		nv = equacao()
		resultado = nv.eq(self.vetor[0])

		for j in range(1,len(self.vetor)-1):
			 resultado += 2*nv.eq(self.vetor[j])

		resultado += nv.eq(self.vetor[len(self.vetor)-1])
		resultado = (self.h/2) *(resultado)
		print(resultado)

#cria objeto Trapezio
#obtem dados do usuario
h = float(input("Digite o valor de h:"))
i = float(input("Digite o valor inferior i da integral:"))
n = float(input("Digite o valor superior n da integral:"))
t = Trapezio(h,i,n)
t.tamanho()
t.calcula(Equacao)


