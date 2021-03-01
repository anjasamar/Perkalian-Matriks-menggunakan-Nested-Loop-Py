# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:06:48 2021

@author: anjas amar pradana
@lisensi: sumber terbuka
@aliansi: universitas dian nuswantoro
"""


#3x3 matrix
X = [[199, 9, 19],
     [3 , 6, 9],
     [13 , 16, 19]]

#3x4 matrix
Y = [[5, 6, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

#Hasilnya adalah 3x4
hasil = [[0 ,0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

#Iterasi melalui baris X
for anjas in range(len(X)):
   
    #Iterasi melalui kolom Y
   for amar in range(len(Y[0])):
       
       #Iterasi melalui baris Y
       for pradana in range(len(Y)):
           hasil[anjas][amar] += X[anjas][pradana] * Y[pradana][anjas]

#Keluarahn hasil Jomblo
for jomblo in hasil:
   print(jomblo)