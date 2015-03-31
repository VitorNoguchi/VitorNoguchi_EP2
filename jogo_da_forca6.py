
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

def cabeça():
    caneta.penup()                        #começa a desenhar a cabeça
    caneta.setpos(-220,160)
    caneta.right(90)
    caneta.pendown()
    caneta.circle(20)

def tronco():
    caneta.penup()                 #começa a desenhar o tronco
    caneta.setpos(-200,140)
    caneta.pendown()
    caneta.forward(70)
                
def braço_esquerdo():
    caneta.penup()               #começa a desenhar o braço esquerdo
    caneta.setpos(-200,110)
    caneta.pendown()
    caneta.right(140)            
    caneta.forward(40)
                
def braço_direito():
    caneta.penup()                #começa a desenhar o braço direito
    caneta.setpos(-200,110)
    caneta.left(280)
    caneta.pendown()
    caneta.forward(40)
            
def perna_esquerda():
    caneta.penup()                       #começa a desenhar a perna esquerda
    caneta.setpos(-200,70)
    caneta.pendown()
    caneta.right(180)
    caneta.forward(40)
            
def perna_direita():                 
    caneta.penup()                        #começa a desenhar a perna direita
    caneta.setpos(-200,70)
    caneta.pendown()
    caneta.left(80)
    caneta.forward(40)
continuar="sim"
arquivo=open("palavras1.txt ",encoding="utf-8")
while continuar=="sim":          
    conteudo=arquivo.readlines()
    lista=list()
    janela = turtle.Screen()
    for i in conteudo:
        palavras=i.strip()
        if palavras != "":
            lista.append(palavras)
    print(lista)
    acertos=0                       #numero de acertos
    erros=0                        #numero de erros
    janela.bgcolor("black")
    janela.title("Joo da Forca")
    caneta = turtle.Turtle()
    caneta.color("pink")
    pincel= turtle.Turtle()
    pincel.color("pink")
    desenhar_forca()
    lapis=turtle.Turtle()
    lapis.color("pink")
    lapis.penup()
    lapis.setpos(-120,0)
    lapis.pendown()
    lapiseira=turtle.Turtle()
    lapiseira.color("orange")
    computador=choice(lista)    #computador escolhe a palavra
    lista.remove(computador)
    computador=computador.lower()
    computador_choice=computador.replace("ã","a")
    computador_choice=computador_choice.replace("ó","o")
    computador_choice=computador_choice.replace("ô","o")
    computador_choice=computador_choice.replace("í","i")
    print(computador_choice)
    riscos(computador_choice)
    escolhas=[]