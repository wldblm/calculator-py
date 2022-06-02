
from functools import partial
import tkinter as tk
from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("240x300")
calcul = ""

def multiplication_division(calc :str):
    calc_2 = ""
    x_str = ""
    y_str = ""
    x = 0
    y = 0
    operator = ""
    result = ""
    inOperation = False
    didOperate = False

    if "*" in calc or "/" in calc:
        for count, i in enumerate(calc):
            if (i == "*" or i == "/") and didOperate == False and inOperation == False:
                operator = i
                inOperation = True
                for j in range(count - 1, -2, -1):
                    if calc[j] == "+" or calc[j] == "-" or calc[j] == "*" or calc[j] == "/" or j == -1:
                        if calc[j] == "-" and not "-" in x_str:
                            x_str = calc[j] + x_str
                            continue
                        print("x_str", x_str)
                        x = float(x_str)
                        break
                    else:
                        x_str = calc[j] + x_str
                
            elif inOperation and didOperate == False:
                if i != "+" and i != "-" and i != "*" and i != "/":
                    y_str += i
                if i == "+" or i == "-" or i == "*" or i == "/" or count == len(calc) - 1:
                    if i == "-" and y_str == "":
                        y_str += i
                        continue
                    print("ystr", y_str)
                    y = float(y_str)
                    print(y)
                    y_str = ""
                    result =  x * y if operator == "*" else x/y 
                    calc_2 = calc_2[:-len(x_str)] + str(result)
                    if count != len(calc) - 1: calc_2 += i
                    operator = ""
                    x_str = ""
                    didOperate = True
            else:
                calc_2 += i
    else:
        calc_2 = calc    

    print("calc_2", calc_2)
    return calc_2
    
def addition_soustraction(calc :str):
    result = 0
    operator = ""
    chiffre = ""

    if calc.__contains__("+") or calc.__contains__("-"):
        for count, i in enumerate(calc):
            if i == "+" or i == "-":

                if operator == "+":
                    result += float(chiffre)
                    operator = ""
                elif operator == "-":
                    if chiffre == "":
                        operator = "+"
                        continue
                    result -= float(chiffre)
                    operator = ""
                elif chiffre != "":
                    result = float(chiffre)
                
                chiffre = ""
                operator = i

            else:
                chiffre += i
            
            if count + 1 == len(calc):
                if operator == "+":
                    result += float(chiffre)
                    operator = ""
                elif operator == "-":
                    result -= float(chiffre)
                    operator = ""

    return result
def calculatrice(calc :str):
    while "*" in calc or "/" in calc:
        calc = multiplication_division(calc)
    if "+" in calc or "-" in calc:
        calc = addition_soustraction(calc)
    return calc

def calculate():
    global calcul
    resultat = calculatrice(calcul)
    calcul = str(resultat)
    label.config(text=resultat)


def write_calc(char):
    global calcul, label
    calcul += char
    label.config(text= calcul)

def reset():
    global calcul
    calcul = ""
    label.config(text= calcul)

style = ttk.Style()
style.configure('W.TButton', font =
               ('calibri', 20, 'bold', ),
                foreground = 'black', background="grey")

label = Label(win, text="", font= ('Century 15 bold'))

btn1 = tk.Button(win, text="1",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "1"))
btn2 = tk.Button(win, text="2",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "2"))
btn3 = tk.Button(win, text="3",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "3"))
btn4 = tk.Button(win, text="4",  width=2, height=2, background="black", foreground="black",command= partial(write_calc, "4"))
btn5 = tk.Button(win, text="5",  width=2, height=2, background="black", foreground="black",command= partial(write_calc, "5"))
btn6 = tk.Button(win, text="6",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "6"))
btn7 = tk.Button(win, text="7", width=2, height=2, background="black", foreground="black", command= partial(write_calc, "7"))
btn8 = tk.Button(win, text="8",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "8"))
btn9 = tk.Button(win, text="9",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "9"))
btn0 = tk.Button(win, text="0",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "0"))

btnx = tk.Button(win, text="x",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "*"))
btnminus = tk.Button(win, text="-",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "-"))
btnplus = tk.Button(win, text="+",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "+"))
btnpoint = tk.Button(win, text=",",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "."))
btndiv = tk.Button(win, text="/",  width=2, height=2, background="black", foreground="black", command= partial(write_calc, "/"))
btnegal = tk.Button(win, text="=",  width=2, height=2, background="black", foreground="black", command= calculate)
btnreset = tk.Button(win, text="AC",  width=2, height=2, background="black", foreground="black", command= reset)


btn7.grid(row = 1, column = 1, sticky='nesw')
btn8.grid(row = 1, column = 2, sticky='nesw')
btn9.grid(row = 1, column = 3, sticky='nesw')
btnx.grid(row = 1 ,column = 4, sticky='nesw')

btn4.grid(row = 2 ,column = 1, sticky='nesw')
btn5.grid(row = 2 ,column = 2, sticky='nesw')
btn6.grid(row = 2 ,column = 3, sticky='nesw')
btnminus.grid(row = 2 ,column = 4, sticky='nesw')

btn1.grid(row = 3 ,column = 1, sticky='nesw')
btn2.grid(row = 3 ,column = 2, sticky='nesw')
btn3.grid(row = 3 ,column = 3, sticky='nesw')
btnplus.grid(row = 3 ,column = 4, sticky='nesw')

btn0.grid(row = 4 , columnspan=2, column = 1, sticky='nesw')
btnpoint.grid(row = 4 ,column = 3, sticky='nesw')
btnegal.grid(row = 4 ,column = 4, sticky='nesw')

btnreset.grid(row = 0, column = 3, sticky='nesw')
btndiv.grid(row = 0, column = 4, sticky='nesw')
label.grid(row = 0, columnspan=3)


win.mainloop()