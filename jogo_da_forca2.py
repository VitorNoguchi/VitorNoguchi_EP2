# -*- coding: utf-8 -*-
#vitor shoji formaggio noguchi
import turtle
from random import*

def desenhar_forca():
    pincel.penup()                      #começa a desenhar a forca
    pincel.color('pink')
    pincel.setpos(-250,0)  
    pincel.pendown()
    pincel.back(50)
    pincel.forward(100)
    pincel.setpos(-250,0)
    pincel.left(90)
    pincel.forward(200)
    pincel.right(90)
    pincel.forward(50)
    pincel.right(90)
    pincel.forward(20)

def riscos (computador_choice):
    for c in computador_choice:               #cria os espaços entre os traços
        if c==" ":
            lapis.penup()
            lapis.forward(40)
            lapis.pendown()
        if c !=" ":               #cria os riscos para as letras
            lapis.forward(20)
            lapis.penup()
            lapis.forward(10)
            lapis.pendown()
