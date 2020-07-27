from functools import partial
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase

def btnClick(opcao, janela):
    janela.destroy()
    return int(opcao.get())

def btnClick2(opcao, janela):
    janela.destroy()
    return opcao.get()

def btnClick3(opcao, janela):
    janela.destroy()
    return int(opcao.get())

def telaInicial():
    janela = Tk()
    content = StringVar()
    janela.title("JOGO DA FORCA")

    lb1 = Label(janela, text = "BEM VINDO AO JOGO DA FORCA", font = ("Consoles 20 bold"))
    lb2 = Label(janela, text = "SELECIONE O TEMA",font = ("Consoles 15 bold"))
    lb3 = Label(janela, text = "  [1] PROFISSÃO",font = ("Consoles 10 bold"))
    lb4 = Label(janela, text = "  [2] FRUTAS",font = ("Consoles 10 bold"))
    lb5 = Label(janela, text = "  [3] ANIMAIS",font = ("Consoles 10 bold"))
    lb6 = Label(janela, text = "  [4] INSTRUMENTOS",font = ("Consoles 10 bold"))
    lb7 = Label(janela, text = "  [5] CORES",font = ("Consoles 10 bold"))
    lb8 = Label(janela, text = "  [6] ALEATÓRIO",font = ("Consoles 10 bold"))
   

    opcao = Entry(janela, textvariable=content)

    btn = Button(janela, text = "OK") 
    btn["command"] = partial(btnClick, opcao, janela)
    Label(janela, text = "").pack()
    lb1.pack()
    Label(janela, text = "").pack()
    lb2.pack()
    Label(janela, text = "").pack()
    lb3.pack(anchor = W)
    lb4.pack(anchor = W)
    lb5.pack(anchor = W)
    lb6.pack(anchor = W)
    lb7.pack(anchor = W)
    lb8.pack(anchor = W)
    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    opcao.pack()
    btn.pack()

    
    janela.geometry('550x400')
    janela.mainloop()    

    return content.get()
    

def telaBoneco(dica, vidas ,palavra_secreta_pontilhada):
    janela = Tk()
    content = StringVar()
    janela.title("JOGO DA FORCA")
    lblpalavra = StringVar()
    Label(janela, text = "DICA: "+dica, font = ("Consolas 15 bold")).pack()
    Label(janela, text = "VIDAS: "+vidas, font = ("Consolas 15 bold")).pack()
    lblpalavra.set(palavra_secreta_pontilhada)
    if(vidas == '6'):
        logo = PhotoImage(file="imagens/img0.png")
        w1 = Label(janela, image=logo).pack(anchor = W)
    if(vidas == '5'):
        logo = PhotoImage(file="imagens/img1.png")
        w2 = Label(janela, image=logo).pack(anchor = W)   
    if(vidas == '4'):
        logo = PhotoImage(file="imagens/img2.png")
        w3 = Label(janela, image=logo).pack(anchor = W)    
    if(vidas == '3'):
        logo = PhotoImage(file="imagens/img3.png")
        w4 = Label(janela, image=logo).pack(anchor = W) 
    if(vidas == '2'):
        logo = PhotoImage(file="imagens/img4.png")
        w5 = Label(janela, image=logo).pack(anchor = W)
    if(vidas == '1'):
        logo = PhotoImage(file="imagens/img5.png")
        w6 = Label(janela, image=logo).pack(anchor = W)  
    if(vidas == '0'):
        logo = PhotoImage(file="imagens/img6.png")
        w7 = Label(janela, image=logo).pack(anchor = W) 
              
    Label(janela, textvariable = lblpalavra, font = ("Consolas 24 bold")).pack()
    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    lb4 = Label(janela, text = "Digite uma Letra/Palavra:", font = ("Consolas 10")).pack()
    
    opcao = Entry(janela, textvariable=content)
    opcao.pack()
    
    btn = Button(janela, text = "OK") 
    btn["command"] = partial(btnClick2, opcao, janela)
    btn.pack()

    janela.geometry('550x400')
    janela.mainloop()  
    
    return content.get() 


def verificaLetraDigitada(verifica):
    messagebox.showwarning("JOGO DA FORCA", verifica)

def ganhou(palavraSecreta):
    janela = Tk()
    janela.title("JOGO DA FORCA")
    content = StringVar()

    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    logo = PhotoImage(file="imagens/trofeu2.png")
    w = Label(janela, image=logo).pack(anchor = S)

    Label(janela, text = "Parabéns, você venceu!!", font = ("Consolas 20 bold")).pack()
    Label(janela, text = "").pack()
    Label(janela, text = "A palavra é: "+palavraSecreta, font = ("Consolas 15")).pack()
    Label(janela, text = "").pack()
    

    Label(janela, text = "Deseja continuar?", font = ("Consolas 15")).pack()
    Label(janela, text = "[1]- SIM   [2]- NÃO", font = ("Consolas 10")).pack()
   
    opcao = Entry(janela, textvariable=content).pack()
   
    btnOK = Button(janela, text = "OK")
    btnOK["command"] = partial(btnClick3, opcao, janela)
    btnOK.pack()

    janela.geometry('550x400')
    janela.mainloop()  
    
    return content.get() 


def perdeu():
    janela = Tk()
    janela.title("JOGO DA FORCA")
    content = StringVar()

    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    logo = PhotoImage(file="imagens/img6.png")
    w = Label(janela, image=logo).pack(anchor = S)
    
    Label(janela, text = "Que pena, você perdeu!!", font = ("Consolas 20 bold")).pack()
    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    Label(janela, text = "").pack()
    
    Label(janela, text = "Deseja continuar?", font = ("Consolas 15")).pack()
    Label(janela, text = "[1]- SIM   [2]- NÃO", font = ("Consolas 10")).pack()
    
    opcao = Entry(janela, textvariable=content).pack()
   
    btnOK = Button(janela, text = "OK")
    btnOK["command"] = partial(btnClick3, opcao, janela)
    btnOK.pack()

    janela.geometry('550x400')
    janela.mainloop()  
   
    return content.get() 

