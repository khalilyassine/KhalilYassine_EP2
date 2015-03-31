# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:11:38 2015

@author: Khalil
"""

jogo = 0
sim = 0
while jogo == sim:
    
    from unicodedata import normalize
    
    def remover_acentos(txt):
        return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
    
    if __name__ == '__main__':
        from doctest import testmod
        testmod()
        
        import turtle             
        window = turtle.Screen()    
        window.bgcolor("lightblue")
        window.title("Forca")
        
        arquivo = open("entrada.txt",encoding="utf-8")
        S1=arquivo.readlines()
        limpa = []
        for q in range(0,len(S1)-1):
            k=S1[q].strip()
            limpa.append(k)
        print (S1)
    #------------------------------------------------------------------------------
    #Montando a Forca
    
    tartaruga   = turtle.Turtle()  
    tartaruga.speed(5)
    tartaruga.penup()       
    tartaruga.setpos(-300,-200)
    tartaruga.pendown()
    tartaruga.left(90)
    tartaruga.forward(500)
    tartaruga.right(90)
    tartaruga.forward(200)
    tartaruga.right(90)
    tartaruga.forward(150)
    tartaruga.color("orange")
    
    tartaruga.penup()
    tartaruga.setpos(50,200)
    tartaruga.write("Boa Sorte!", font = ("Arial", 20))
    tartaruga.penup()
    
    #------------------------------------------------------------------------------
    #Criando definições para o corpo do boneco
    
    
    def cabeça():
        cabeça = turtle.Turtle()
        cabeça.speed(5)
        cabeça.penup()
        cabeça.setpos(-100,50)
        cabeça.pendown()
        cabeça.circle(50)
        cabeça.color("orange")
        
    
    def corpo():
        corpo = turtle.Turtle()
        corpo.speed(5)
        corpo.penup()
        corpo.setpos(-100,50)
        corpo.pendown()
        corpo.right(90)
        corpo.forward(200)
        corpo.color("orange")
    
    
    def braço1():
        braço1 = turtle.Turtle()
        braço1.speed(5)
        braço1.penup()
        braço1.setpos(-100,0)
        braço1.pendown()
        braço1.right(120)
        braço1.forward(100)
        braço1.color("orange")
        
    
    def braço2():
        braço2 = turtle.Turtle()
        braço2.speed(5)
        braço2.penup()
        braço2.setpos(-100,0)
        braço2.pendown()
        braço2.left(120)
        braço2.forward(-100)
        braço2.color("orange")
    
    def perna1():
        perna1 = turtle.Turtle()
        perna1.speed(5)
        perna1.penup()
        perna1.setpos(-100,-120)
        perna1.pendown()
        perna1.pendown()
        perna1.left(120)
        perna1.forward(-100)
        perna1.color("orange")
    
    def perna2():
        perna2 = turtle.Turtle()
        perna2.speed(5)
        perna2.penup()
        perna2.setpos(-100,-120)
        perna2.pendown()
        perna2.pendown()
        perna2.right(120)
        perna2.forward(100)
        perna2.color("orange")
    
    #-----------------------------------------------------------------------------
    #Encontrando a palavra
    acertos = 0
    erros = 0
    i = 0
    x = 0
    letra = []
    from random import randint
    x = limpa[randint(0,len(S1))-1]
    palavrasorteada=x.lower()
    palavrasorteada= remover_acentos(palavrasorteada)
    comprimento = len(palavrasorteada)
    tartaruga.setpos(-300,-250)
    tartaruga.left(90)
    for i in range (comprimento-1):
        
        if palavrasorteada[i]== " ":
            acertos +=1
            tartaruga.penup()
            tartaruga.forward(20)
        else:
            
            tartaruga.speed(100)
            tartaruga.color("orange")
            tartaruga.pendown()
            tartaruga.forward(20)
            tartaruga.penup()
            tartaruga.forward(15)
            tartaruga.pendown()
            
    #-----------------------------------------------------------------------------
    #Verificando possibilidades
    
    
    while erros != 6 and acertos != len(palavrasorteada):
        
        chute = window.textinput("Digite uma letra","Digite uma letra")
       
        if chute not in palavrasorteada:
            erros +=1
            if erros==1:
                cabeça()
            if erros ==2 :
                corpo()
            if erros ==3:
                braço1()
            if erros ==4:
                braço2()
            if erros==5:
                perna1()
            if erros ==6:
                perna2()
                tartaruga.penup()
                tartaruga.setpos(50,100)
                tartaruga.write("GAME OVER", font= ("Arial", 40))
                tartaruga.pendown()
                R = window.textinput("Reinicio","Você deseja reiniciar o jogo?")
                if R == sim:
                   jogo = sim
                
                           
      
        for k in range(0,len(palavrasorteada)):
                if chute == palavrasorteada[k]:
                    
                    tartaruga.penup()
                    tartaruga.setpos(-300 +30*k,-250)
                    tartaruga.pendown()
                    tartaruga.write(chute, font= ("Arial",15))
                    acertos +=1
                if acertos == comprimento:
                    tartaruga.penup()
                    tartaruga.setpos(50,50)
                    tartaruga.write("VOCÊ GANHOU!!", font= ("Arial", 30))
                    tartaruga.pendown()
                    R = window.textinput("Reinicio","Você deseja reiniciar o jogo?")
                    if R == sim:
                       jogo = sim
                
    window.exitonclick()           