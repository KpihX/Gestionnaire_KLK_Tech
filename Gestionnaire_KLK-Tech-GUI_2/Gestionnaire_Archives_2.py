# -*-coding:UTF-8 -*
from Manager_Functions_GUI_2 import*
import shutil

if paw("KLK-Tech") == True:
    Products = []
    try:
        openJsonFile(Products, "Products")
        assert Products != []
    except:
        pass
    Customers = {}
    try:
        openJsonFile(Customers, "Customers")
    except:
        pass
    
    while True:
        choice = input("Veuillez choisir une action :\n\
        1- Afficher les informations sur les clients.\n\
        2- Afficher les informations sur les produits en stock.\n\
        3- Supprimer un/plusieurs client(s).\n\
        4- Mettre à jour la liste des produits.\n\
        5- Réinitialiser les archives.\n\
        6- Classer les produits par ordre alphabétique et reassigner de façon croissante leurs codes.\nAction N° : ")
        if choice == '1':
            if Customers == {}:
                print("Aucun client enregistré jusqu'à présent.")
            else:
                print("Voici les informations sur les derniers clients enregistrés : ")
                for customer in Customers:
                    print(f"* -Nom : Mme/M. {customer}\n  -Nombre de passages dans la boutique : {Customers[customer][0]}.\n")
                    printTable([["Produit", "Nbre de commandes"]]+[[product, Customers[customer][1][product]] for product in Customers[customer][1]], "Liste des produits achetés")
        if choice == '2':
            if Products == []:
                print("Aucun produit en stock.")
            else:
                printTable([["Nom", "Code", "Prix unitaire", "Quantité"]]+Products, "Voici les informations sur les produits en stoock : ")
        if choice == '3':
            while True:
                if Customers == {}:
                    print("Aucun client enregistré!")
                    break
                Del = input("Entrer le nom du client à supprimer : ").title()
                shutil.rmtree(f"Factures/{Del}")
                try:
                    Customers.pop(Del)
                except:
                    print(f"Le client {Del} n'est pas dans notre liste des clients. Toutefois, si ses factures existaient encore, elles ont été toutes supprimées.")
                bool = input("Encore (o/n) : ")
                if bool.lower() != 'o':
                    break
        if choice == '4':
            while True:
                choice2 = input("Veuillez choisir une action :\n\
                a- Supprimer un/plusieurs produit(s)\n\
                b- Ajouter/modifier les informations d'un/plusieurs produit(s).\nAction N° : ")
                if choice2 == 'a':
                    while True:
                        if Products == []:
                            print("Auncun produit en stock!")
                            break
                        l = len(Products)
                        Del = input("Entrer le nom du produit à supprimer : ").title()
                        for i in range(l):
                            bool = False
                            if Products[i][0] == Del:
                                Products.pop(i)
                                bool = True
                                for j in range(i, l-1):
                                    Products[j][1] -= 1
                                break
                        if bool == False:
                            print(f"Le produit {Del} n'est pas dans notre liste des produits.")
                        bool = input("Encore (o/n) : ")
                        if bool.lower() != 'o':
                            break
                if choice2 == 'b':
                    while True:
                        Add = input("Entrer resp les infos d'un produit à ajouter/modifier en stock (NB: le code est généré automatiquement) (nom,quantité,prix unitaire (facultatif si le produit est déjà en stock; Ex : Souris,10, -> le prix unitaire reste inchangé.)) : ").title().split(',')
                        try:
                            l = len(Products)
                            val = Add[2].strip() == ''
                            assert Add[1].isnumeric() == True and (val or isUFloat(Add[2]) == True)
                            if not val:
                                Add[2] = float(Add[2])
                                assert Add[2] !=  0
                            Add[1] =  int(Add[1])
                            assert Add[1] != 0 
                            bool = False
                            for i in range(l):
                                if Products[i][0] == Add[0]:
                                    if not val:
                                        Products[i][2] = Add[2]
                                    Products[i][3] += Add[1]
                                    bool = True
                                    break
                            assert not (bool == False and val)
                            if bool == False:
                                i = 0
                                for i in range(l):
                                    if Products[i][0] > Add[0]: 
                                        Products.insert(i, [Add[0], i+1, Add[2], Add[1]])
                                        for j in range(i+1, l+1):
                                            Products[j][1] += 1
                                        break
                        except:
                            print("Données invalides.")
                        bool = input("Encore (o/n) : ")
                        if bool.lower() != 'o':
                            break
                bool = input("Encore (a,b) (o/n) : ")
                if bool.lower() != 'o':
                    break 
        if choice == '5':
            while True:
                choice2 = input("Veuillez choisir une action :\n\
                a- Réinitialiser les données sur les clients.\n\
                b- Réinitialiser les données sur les produits.\nAction N° : ")
                if choice2 == 'a':
                    Customers = {}
                    shutil.rmtree(f"Factures")
                if choice2 == 'b':
                    Products = [["Clavier", 1, 4500, 10], ["Cle 32Go", 2, 3500, 3], ["Cle 64Go", 3, 5000, 2], ["Disque Dur Externe SSD 1To", 4, 35000, 5], ["Ecouteur Bluetooth", 5, 2500, 14], ["Imprimante Lazer", 6, 50000, 4], ["Iphone 14", 7, 900000, 4], ["Itel A52", 8, 55000, 5], ["Redmi Note 8 Pro", 9, 125000, 5], ["Souris", 10, 3500, 5], ["Tecno Pop 2", 11, 50000, 3]]
                bool = input("Encore (a,b) (o/n) : ")
                if bool.lower() != 'o':
                    break 
        if choice == '6':
            Products.sort()
            for i in range(len(Products)):
                Products[i][1] == i+1
        bool = input("Encore (1,2,3,4,5) (o/n) : ")
        if bool.lower() != 'o':
            break       
    #We safeguard the changes made in the archives
    openJsonFile(Products, "Products", "w")      
    openJsonFile(Customers, "Customers", "w") 
    input("Ravi de vous avoir servi!")