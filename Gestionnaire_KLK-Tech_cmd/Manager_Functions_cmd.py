import os
import sys
from pickle import Pickler, Unpickler

def closeStr(S1:str, S2:str, precision = 1/3):
    """It evaluates with a precision given (default=1/3), how closed are two strings S1 and S2"""
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()
    Diff = symDiffList([i for i in S1], [i for i in S2])
    l1 = len(S1)
    l2 = len(S2)
    d = abs(l1-l2)
    m = max(l1, l2)
    #We considerate firstly the differences inside the two strings that we divide by two (because they are counted twice in Diff), and secondly, those due to the difference of length of S1 and S2
    #Then we express how significant are those differences from the longest string between S1 and S2
    if ((len(Diff)-d)/2+d)/m <= precision: 
        return True
    return False

def closeSubStr(S1:str, S2:str, precision = 0.25):
    """It evaluates with a precision given (default=1/3), how closed is a string S1 to an eventual substring of S2"""
    S1 = S1.replace(' ', '').lower()
    S2 = S2.replace(' ', '').lower()
    l1 = len(S1)
    l2 = len(S2)
    for i in range(l2-l1+1):
        if closeStr(S1, S2[i: i+l1], precision) == True:
            return True
    return False

def extend(I, J):
    """It extends an immutable iterable (list, dict or set) I with another one J of same type and return the result"""
    if type(I)==type(J):
        if type(I) == list:
            I.extend(J)
        if type(I) == dict:
            I.update(J)
        if type(I) == set:
            I.update(J)
    return I

def isUFloat(S:str):
    """It evaluates whether S is an unsigned float or not"""
    L = S.split('.')
    if len(L) <= 2 and all([i.isdigit() for i in L]):
        return True
    else:
        return False

def openBinaryFile(Datas, path, mode='rb'):
    """It takes as input the path of a binary file, the mode of access to this file ('rb' or 'wb') and a data structure 'Datas'
    -If mode='rb' it puts the contents of this file in 'Datas'
    -If mode='wb', it copies the contents of 'Datas' in this file
    """
    with open(path, mode) as f:
        if mode == 'rb':
            p = Unpickler(f)
            extend(Datas, p.load())  
        if mode == 'wb':
            p = Pickler(f)
            p.dump(Datas)

def paw(password:str, test:int = 3):
    """it grants access to a system via a password 'password' with 'test' test(s)"""
    if type(test) != int or test <= 0:
        return f"'{test}' n'est pas un nombre entier strictement positif"
    else:
        i = 0
        while True:
            if i == test:
                print("Vous avez épuisé toutes vos possibilités! Veuillez sortir!")
                return False
            p = input("Mot de passe : ")
            if p == password:
                break
            i += 1
        print("Bienvenue!")
        return True

def printTable(Datas, Label:str = '',End = '', place="cmd"):
    """This functions displays datas in 'Datas' on 'place' with the label 'label'and an end expression 'End'
    Args:
        Label (str): title of the datas that are going to be displayed
        Datas (list(list)): it contains the datas to display. It's a table
        End (str): it is a final eventual expression. Defaults to ""
        place (str): it indicates the place where to display the datas. Defaults to "cmd". it can also take as value the path of a file where to diplay the table
    """
    try:
        if all([len(i)==len(Datas[0]) for i in Datas]) == False:
            print("Le structure fournie n'est pas un tableau n*m valide")
        else:
            Space = [max([len(str(data)) for data in Data]) for Data in tranpose(Datas)]
            Str = ''
            if Label != '':
                Str = Label.center(sum([i+3 for i in Space])+1)+"\n"
            for i in range(len(Datas)):
                Str+="+"
                for j in range(len(Datas[i])):
                    Str += "-"*(Space[j]+2)+"+"
                Str+="\n| "
                for j in range(len(Datas[i])):
                    Str += f"{Datas[i][j]}".center(Space[j])+" | "
                Str+="\n"
                if i == len(Datas)-1:
                    Str+="+"
                    for j in range(len(Datas[i])):
                        Str += "-"*(Space[j]+2)+"+"
                    Str+="\n"
                    
            if End != "":
                Str+=End.center(sum([i+3 for i in Space])+1)+"\n"
            
            if place == "cmd":
                print(Str)
            else:
                with open(place, "w") as f:
                    f.writelines(Str)
    except:
        pass

def symDiffList(L1:list, L2:list):
    """It returns a list which elts indicate a chronological difference between the two lists given as parameters """
    Diff = []
    while True:
        l1 = len(L1)
        l2 = len(L2)
        if l2 < l1:
            L1, L2 = L2, L1
        if L1 == []:
            Diff.extend(L2)
            break
        i = 0
        while i < l2:
            #We try to find if the concerned elt is in L2 too and so, can't be count as a difference
            if L1[0] == L2[i] and i <= abs(l2-l1):
                #To ensure the chronological similarity between L1 and L2, we remove all elts before L2[i] because they indicate a chronological difference between the two lists
                L1.pop(0)
                for j in range(i):
                    Diff.append(L2[0])
                    L2.pop(0)
                L2.pop(0)
                break
            i += 1
        if i == l2:
            #In this case, no elts of L2 corresponds to L1[0], so we count it as a difference between the two lists
            Diff.append(L1[0])
            L1.pop(0)
    return Diff

def tranpose(Table):
    """It returns the transpose of a table Table"""
    return [[Table[j][i] for j in range(len(Table))] for i in range(len(Table[0]))]

if __name__ == "__main__":
    import Manager_Functions_cmd
    print("'Manager_Functions' is a module full of functions and objects, varied and very practical for a shop manager. Here are some detailed help : ")      
    help(Manager_Functions_cmd)
    input("")