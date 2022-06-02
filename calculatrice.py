from hashlib import new


print("calcule ?")
calc = input()
symbols = ["*", "/"]
newCalcul = ""
calculateur = ""
chiffre = ""
total = 0
newCalcul = ""
x_str = ""
x = 0
y_str = ""
y = 0
resulatMulitplication = 0
inMultiplication = False
didCalculate = False

def checkMulti(calcul :str):
    print("entrée dans la fonction calcul =", calcul)
    newCalcul = ""
    calculateur = ""
    chiffre = ""
    total = 0
    newCalcul = ""
    x_str = ""
    x = 0
    y_str = ""
    y = 0
    resulatMulitplication = 0
    inMultiplication = False
    didCalculate = False
    if calcul.__contains__("*") or calcul.__contains__("/"):
        for count, i in enumerate(calcul):
            if inMultiplication and (i == "*" or i == "/") and didCalculate == False:
                if i != "+" and i != "-" and i != "*" and i != "/":
                    y_str += i
                    print("y_str ligne 39 = " , y_str)
                print("y_str ligne 40 =" , y_str)
                y = float(y_str)
                resulatMulitplication = x * y if calculateur == "*" else x/y
                print("resultat multi ligne 37 =" , resulatMulitplication)
                newCalcul = newCalcul[:-len(x_str)]
                newCalcul += str(resulatMulitplication) + i if i == "+" or i == "-" else str(resulatMulitplication) 
                calculateur = "" 
                y_str = ""
                didCalculate = True
                #inMultiplication = False

            if (i == "*" or i == "/") and didCalculate == False:
                calculateur = i
                inMultiplication = True
                for j in range(count - 1, -2, -1):

                    if calcul[j] == "+" or calcul[j] == "-" or calcul[j] == "*" or calcul[j] == "/" or j == -1:
                        x = float(x_str)
                        break

                    else:
                        x_str = calcul[j] + x_str
                        print("x_str = " , x_str)
                continue
            if inMultiplication and didCalculate == False:
                if i != "+" and i != "-" and i != "*" and i != "/":
                    y_str += i
                    print("y_str ligne 68 = " , y_str)
                if i == "+" or i == "-" or count == len(calcul) - 1:
                    y = float(y_str)
                    y_str = ""
                    resulatMulitplication = x * y if calculateur == "*" else x/y 
                    print("resultat multi ligne 75 =" , resulatMulitplication)
                    print("new Calcul 60", newCalcul)
                    newCalcul = newCalcul[:-len(x_str)]
                    print("len(x_str)", x_str)
                    print("new Calcul 64", newCalcul)
                    #print("calcul[j] = ", i)
                    newCalcul += str(resulatMulitplication) + i if i == "+" or i == "-" else str(resulatMulitplication)
                    print("new Calcul 67", newCalcul)
                    calculateur = ""
                    x_str = ""
                    didCalculate = True
                
            else:
                newCalcul += i 
                print("else newCalcul", newCalcul)
    else:
        newCalcul = calcul

    if any([symbol in newCalcul for symbol in symbols]):
        checkMulti(newCalcul)
    else:
        print("resultat =", newCalcul)
    
    print("newCalcul ligne 95", newCalcul)
    return newCalcul

newCalcul = checkMulti(calc)

print("new calcul ligne 83 =", newCalcul)
if newCalcul.__contains__("+") or newCalcul.__contains__("-"):
    for count, i in enumerate(newCalcul):
        if i == "+" or i == "-":
            if calculateur == "+":
                total = total + float(chiffre)
                #print("total 64 =" , total)
                calculateur = ""
            elif calculateur == "-":
                total = total - float(chiffre)
                calculateur = ""
            elif chiffre != "":
                total = float(chiffre)
                #print("total 71 =" , total)
            chiffre = ""
            calculateur = i
        else:
            print("chiffre =", chiffre)
            chiffre = chiffre + i
            
        if count+1 == len(newCalcul):
            if calculateur == "+":
                total = total + float(chiffre)
                calculateur = ""
            elif calculateur == "-":
                total = total - float(chiffre)
                calculateur = ""

else:
    total = newCalcul

print("total ligne 114 =", total)
    
                

                