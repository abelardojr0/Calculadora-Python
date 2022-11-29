from tkinter import *
from tkinter import ttk

# CORES UTILIZADAS
cor1 = "#1e1f1e"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#eceff1"
cor5 = "#ffab40"

# ESTRUTURA DA JANELA
janela = Tk()
janela.title("Calculadora")
janela.geometry("440x530")
janela.config(bg=cor1)


# DIVISÕES
#PARTE DE CIMA, ONDE FICAR OS VALORRES 
input_janela = Frame(janela, width=440, height=80, bg=cor3)
input_janela.grid(row=0, column=0)

#PARTE DE BAIXO ONDE FICAM OS BOTÕES
corpo_janela = Frame(janela, width=440, height=530)
corpo_janela.grid(row=1, column=0)


#LABEL 
valor_texto = StringVar() # VARIAVEL QUE VAI COLOCAR NA TELA OS VALORES DIGITADOS

# VARIAVEL COM TODOS OS VALORES
todos_valores = "" #VARIAVEL PRINCIPAL QUE VAI GUARDAR OS VALORES DIGITADOS PARA QUE POSSAMOS MANIPULA-LO
operacoes = False # VERIFICADOR DE JÁ TEM UMA OPERAÇÃO PROCESSADA

#FUNÇÃO QUE COLOCA OS VALORES CLICADOS NA TELA
def entrar_valores(event): #CONTROLE DO INPUT DOS NÚMEROS DIGITADOS
    global todos_valores
    global operacoes
    todos_valores = todos_valores + str(event) #ATUALIZO A VARIAVEL PRINCIPAL, COM O VALOR QUE ELA JÁ TINHA + O PRÓXIMO VALOR DIGITADO
    
    arrayOperadores = ["*","/","+","-"] #LISTA COM TODOS OS OPERADORES
    
    lista = [] 
    lista[:0] = todos_valores #TRANSFORMANDDO A STRING EM UM ARRAY
    
    valor_texto.set(todos_valores) #DEPOIS EU MOSTRO NA TELA ESSE NOVO VALOR
    
    if("*" in lista or "-" in lista or "+" in lista or "/" in lista): #SE DENTRO DO INPUT DIGITADO JÁ TIVER UM OPERADOR
        operacoes = True    
        
        
    if event in arrayOperadores and lista[len(lista) - 2] in arrayOperadores: #SE O BOTAO CLICADO FOI UM OPERADOR E A PENULTIMA(ÚLTIMA NA VDD, MAS COMO O NOVO OPERADOR JÁ ENTROU NO CASO O OPERADOR ANTIGO VIRA O PENULTIMO) POSICAO DA LISTA TAMBÉM FOR UM OPERADOR
        del(lista[len(lista) - 2]) #EU TIRO ESSE ANTIGO OPERADOR
        todos_valores = "".join(lista) #ATUALIZO A VARIAVEL PRINCIAPAL
        valor_texto.set(todos_valores)   #ATUALIZO O TEXTO MOSTRADO NA TELA
        
        
    if(operacoes and event == "+" or event == "-" or event == "*" or event == "/"): # SE O CARA ACABOU DE USAR UM OPERADOR, E JÁ É A SEGUNDA OPERAÇÃO, OU SEJA, UM NUMÉRO DEPOIS DE UMA OPERAÇÃO MATEMÁTICA
        calcular() # EU CHAMO A FUNÇÃO PARA CALCULAR EM VEZ DE SAIR ADICIONANDO

#FUNÇÃO QUE CALCULA
def calcular():
    global todos_valores
    global operacoes
    
    operacoes = True # DEPOIS DE EFETUAR O CALCULAR, EU FALO QUE AS OPERAÇÕES ESTÁ EM 1 (PQ FICA O RESULTADO LÁ)
        
    lista = [] 
    lista[:0] = todos_valores
    
    operadorRemovido = ""#ESSA VARIÁVEL VAI COMEÇAR VAZIA, PARA CASO ELE ESTEJA USANDO O BOTÃO DE =
    

    if lista[-1] == "*" or lista[-1] == "/" or lista[-1] == "+" or lista[-1] == "-": #SE O ÚLTIMO DIGITO FOR UM OPERADOR
        operadorRemovido = lista.pop() #EU TIRO ESSE OPERADOR E GUARDO EM UMA VARIÁVEL

    if "/" in lista and lista[-1] == "0": # SE ELE TA TENTANDO DIVIDIR POR ZERO
        valor_texto.set("Não pode dividir por 0")
    else:
        resultado = eval("".join(lista)) #FUNÇÃO EVAL CALCULA AS OPERAÇÕES BÁSICAS DO PY, DO VALOR QUE ESTÁ DENTRO DAQUELA LISTA QUE EU TRANSFORMO EM STRING, JÁ SEM O OPERADOR NO FINAL
        valor_texto.set(str(f"{resultado}{operadorRemovido}")) #COLOCO NA TELA O VALOR DO RESULTADO COM O OPERADOR QUE EU TINHA REMOVIDO NA FRENTE(EU REMOVI SÓ PARA FAZER A OPERAÇÃO)
        todos_valores = str(f"{resultado}{operadorRemovido}") # ATUALIZO A VARIAVEL PRINCIPAL


#FUNÇÃO DE APAGAR UM DIGITO

def apagarDigito():
    global todos_valores
    lista = [] 
    lista[:0] = todos_valores #TRANSFORMA A STRING EM UMA LISTA
    lista.pop() #REMOVO O ÚLTIMO ITEM DESSA LISTA
    valor_texto.set("".join(lista)) # COLOCO NA TELA O VALOR ATUALIZADO
    todos_valores = str("".join(lista)) #ATUALIZO A VARIAVEL PRINCIPAL
    

# FUNÇÃO DE LIMPAR TUDO
def limpar():
    global todos_valores
    valor_texto.set("") #LIMPO A TELA
    todos_valores = "" #LIMPO A VARIAVEL PRINCIPAL


# LOCAL QUE VAI RECEBER OS INPUTS(O RETANGULOZIM AZUL)
app_label = Label(input_janela, textvariable=valor_texto, width=22, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 24"), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


# BOTÕES
B1 = Button(corpo_janela, command= limpar, text="C", width=21, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B1.place(x=0, y=0)
B2 = Button(corpo_janela, command= apagarDigito, text="⌫", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B2.place(x=220, y=0)
B3 = Button(corpo_janela, command= lambda: entrar_valores("/"), text="/", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B3.place(x=330, y=0)

B4 = Button(corpo_janela, command= lambda: entrar_valores("7"), text="7", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B4.place(x=0, y=90)
B5 = Button(corpo_janela, command= lambda: entrar_valores("8"), text="8", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B5.place(x=110, y=90)
B6 = Button(corpo_janela, command= lambda: entrar_valores("9"), text="9", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B6.place(x=220, y=90)
B7 = Button(corpo_janela, command= lambda: entrar_valores("*"), text="*", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B7.place(x=330, y=90)


B8 = Button(corpo_janela, command= lambda: entrar_valores("4"), text="4", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B8.place(x=0, y=180)
B9 = Button(corpo_janela, command= lambda: entrar_valores("5"), text="5", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B9.place(x=110, y=180)
B10 = Button(corpo_janela, command= lambda: entrar_valores("6"), text="6", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B10.place(x=220, y=180)
B11 = Button(corpo_janela, command= lambda: entrar_valores("-"), text="-", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B11.place(x=330, y=180)


B12 = Button(corpo_janela, command= lambda: entrar_valores("1"), text="1", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B12.place(x=0, y=270)
B13 = Button(corpo_janela, command= lambda: entrar_valores("2"), text="2", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B13.place(x=110, y=270)
B14 = Button(corpo_janela, command= lambda: entrar_valores("3"), text="3", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B14.place(x=220, y=270)
B15 = Button(corpo_janela, command= lambda: entrar_valores("+"), text="+", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B15.place(x=330, y=270)


B16 = Button(corpo_janela, command= lambda: entrar_valores("0"), text="0", width=21, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B16.place(x=0, y=360)
B17 = Button(corpo_janela, command= lambda: entrar_valores("."), text=".", width=10, height=4, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B17.place(x=220, y=360)
B18 = Button(corpo_janela, command= calcular, text="=", width=10, height=4, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B18.place(x=330, y=360)


janela.mainloop()
