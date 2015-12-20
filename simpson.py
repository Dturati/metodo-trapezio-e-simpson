#!/usr/bin/env python
#_*_ coding:UTF-8 _*_
"""
Python 3
David Turati
Implementação de integral numérica pela forma de 1/3 de simpson

"""
# a equação deve ser mudada no arquivo Equação.py
from Equacao import * 
from math import *

class Simpson(object):
	vetor = []
	def __init__(self,h,i,n):
		self.h = h
		self.i = i
		self.n = n

	def tamanho(self):
		temp = self.i
		while(temp <= self.n):
			self.vetor.append(temp)
			temp = temp + self.h
		self.vetor.append(temp)

	def calcula(self,equacao):
		nv = equacao()
		resultado = nv.eq(self.vetor[0])
		n = 4
		for j in range(1,len(self.vetor)-1):
			resultado += n*nv.eq(self.vetor[j])
			if n == 4:
			   	n = n-2
			else:
			   	 n = n+2

		resultado += nv.eq(self.vetor[len(self.vetor)-1])
		resultado = (self.h/3) *(resultado)
		print(resultado)

#inicio 
h = float(input("Digite o valor de h:"))
i = int(input("Digite o valode inferior i da integral:"))
n = int(input("Digite o vlor superior n da integral:"))
s = Simpson(h,i,n)
s.tamanho()
s.calcula(Equacao)