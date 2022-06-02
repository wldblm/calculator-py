
print("calcule ?")
calcul = input()

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
                        x = float(x_str)
                        break
                    else:
                        x_str = calc[j] + x_str
                
            elif inOperation and didOperate == False:
                if i != "+" and i != "-" and i != "*" and i != "/":
                    y_str += i
                if i == "+" or i == "-" or i == "*" or i == "/" or count == len(calc) - 1:
                    y = float(y_str)
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

    if "*" in calc_2 or "/" in calc_2:
        calc_2 = multiplication_division(calc_2)
    if "+" in calc_2 or "-" in calc_2:
        calc_2 = addition_soustraction(calc_2)
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

resultat = multiplication_division(calcul)
print("result =", resultat)