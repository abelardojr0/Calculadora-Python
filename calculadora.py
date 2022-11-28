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
janela.geometry("235x310")
janela.config(bg=cor1)


# DIVISÕES
#PARTE DE CIMA, ONDE FICAR OS VALORRES 
input_janela = Frame(janela, width=235, height=50, bg=cor3)
input_janela.grid(row=0, column=0)

#PARTE DE BAIXO ONDE FICAM OS BOTÕES
corpo_janela = Frame(janela, width=235, height=260)
corpo_janela.grid(row=1, column=0)


#LABEL 
valor_texto = StringVar() # VARIAVEL QUE VAI COLOCAR NA TELA OS VALORES DIGITADOS

# VARIAVEL COM TODOS OS VALORES
todos_valores = "" #VARIAVEL PRINCIPAL QUE VAI GUARDAR OS VALORES DIGITADOS PARA QUE POSSAMOS MANIPULA-LO
usado = False #USO PARA CONTROLAR SE ALGUM OPERADOR JÁ FOI USADO
operacoes = 0 # USO PARA SABER QUANTAS OPERAÇÕES JÁ TEM DENTRO DO INPUT

#FUNÇÃO QUE COLOCA OS VALORES CLICADOS NA TELA
def entrar_valores(event): #CONTROLE DO INPUT DOS NÚMEROS DIGITADOS
    global todos_valores
    global operacoes
    global usado
    
    todos_valores = todos_valores + str(event) #ATUALIZO A VARIAVEL PRINCIPAL, COM O VALOR QUE ELA JÁ TINHA + O PRÓXIMO VALOR DIGITADO
    
    lista = [] 
    lista[:0] = todos_valores #TRANSFORMANDDO A STRING EM UM ARRAY
    
    valor_texto.set(todos_valores) #DEPOIS EU MOSTRO NA TELA ESSE NOVO VALOR
    
    if("*" in lista or "-" in lista or "+" in lista or "/" in lista): #SE DENTRO DO INPUT DIGITADO JÁ TIVER UM OPERADOR
        operacoes += 1
        
    if(str(event) == "*" or str(event) == "/" or str(event) == "+" or str(event) == "-"): #SE O QUE O USUARIO ACABOU DE DIGITAR FOR UM OPERADOR
        usado = True    
    # print(operacoes)
    # if(event == "*" and operacoes >=2 and lista[-1] == "+" or lista[-1] == "-" or lista[-1] == "*" or lista[-1] == "/"):
    #     lista.pop()
    #     lista[-1] = "*"
    #     todos_valores = "".join(lista)
    #     print(todos_valores)
    #     valor_texto.set(todos_valores)

    
    if( usado and operacoes >2 and event == "+" or event == "-" or event == "*" or event == "/"): # SE O CARA ACABOU DE USAR UM OPERADOR, E JÁ É A SEGUNDA OPERAÇÃO, OU SEJA, UM NUMÉRO DEPOIS DE UMA OPERAÇÃO MATEMÁTICA
        calcular() # EU CHAMO A FUNÇÃO PARA CALCULAR EM VEZ DE SAIR ADICIONANDO

#FUNÇÃO QUE CALCULA
def calcular():
    global todos_valores
    global operacoes
    global usado
    
    operacoes = 1 # DEPOIS DE EFETUAR O CALCULAR, EU FALO QUE AS OPERAÇÕES ESTÁ EM 1 (PQ FICA O RESULTADO LÁ)
    usado = False # E TIRO O MARCADOR QUE VERIFICA SE JÁ TEM UM OPERADOR NA PARADA
    
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
app_label = Label(input_janela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 18"), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


# BOTÕES
B1 = Button(corpo_janela, command= limpar, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B1.place(x=0, y=0)
B2 = Button(corpo_janela, command= apagarDigito, text="⌫", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B2.place(x=118, y=0)
B3 = Button(corpo_janela, command= lambda: entrar_valores("/"), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B3.place(x=177, y=0)

B4 = Button(corpo_janela, command= lambda: entrar_valores("7"), text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B4.place(x=0, y=52)
B5 = Button(corpo_janela, command= lambda: entrar_valores("8"), text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B5.place(x=59, y=52)
B6 = Button(corpo_janela, command= lambda: entrar_valores("9"), text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B6.place(x=118, y=52)
B7 = Button(corpo_janela, command= lambda: entrar_valores("*"), text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B7.place(x=177, y=52)


B8 = Button(corpo_janela, command= lambda: entrar_valores("4"), text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B8.place(x=0, y=104)
B9 = Button(corpo_janela, command= lambda: entrar_valores("5"), text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B9.place(x=59, y=104)
B10 = Button(corpo_janela, command= lambda: entrar_valores("6"), text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B10.place(x=118, y=104)
B11 = Button(corpo_janela, command= lambda: entrar_valores("-"), text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B11.place(x=177, y=104)


B12 = Button(corpo_janela, command= lambda: entrar_valores("1"), text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B12.place(x=0, y=156)
B13 = Button(corpo_janela, command= lambda: entrar_valores("2"), text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B13.place(x=59, y=156)
B14 = Button(corpo_janela, command= lambda: entrar_valores("3"), text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B14.place(x=118, y=156)
B15 = Button(corpo_janela, command= lambda: entrar_valores("+"), text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B15.place(x=177, y=156)


B16 = Button(corpo_janela, command= lambda: entrar_valores("0"), text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B16.place(x=0, y=208)
B17 = Button(corpo_janela, command= lambda: entrar_valores("."), text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B17.place(x=118, y=208)
B18 = Button(corpo_janela, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
B18.place(x=177, y=208)


janela.mainloop()
