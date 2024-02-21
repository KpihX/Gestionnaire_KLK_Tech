# -*-coding:UTF-8 -*
from Manager_Functions_cmd_2 import*

'''Opening of archives'''

Products = []
try:
    openJsonFile(Products, "Products")
    assert Products != []
except:
    Products = [["Clavier", 1, 4500, 10], ["Cle 32Go", 2, 3500, 3], ["Cle 64Go", 3, 5000, 2], ["Disque Dur Externe SSD 1To", 4, 35000, 5], ["Ecouteur Bluetooth", 5, 2500, 14], ["Imprimante Lazer", 6, 50000, 4], ["Iphone 14", 7, 900000, 4], ["Itel A52", 8, 55000, 5], ["Redmi Note 8 Pro", 9, 125000, 5], ["Souris", 10, 3500, 5], ["Tecno Pop 2", 11, 50000, 3]]

Customers = {}
try:
    openJsonFile(Customers, "Customers")
except:
    pass
    
'''Dialogue with the customer'''

name = input("Bienvenue chez KLK-Tech! Veuillez entrer votre nom : ").title()
print(f"\nUne fois de plus bienvenue Mme/M. {name}.\n")

#We check the fidelity of the customer
Fidelity_products = []
if name in Customers.keys():
    Previous_products = list(Customers[name][1].keys())
    bool =  Previous_products != []
    if bool:
        print("En nous basant sur vos précédentes visites de notre boutique, vous pourriez être intéréssé par le/les article(s) suivant(s) : {}.\n".format(", ".join(Previous_products)))
        for product in Previous_products:
            if Customers[name][1][product]>=2:
                Fidelity_products.append(product)
        if Fidelity_products != []:      
            print("Pour vous remercier de votre fidélité, nous vous offrons une réduction de 2% sur les produits suivants,\n(Vu que pour chacun d'eux, vous nous les avez déjà achetés à au moins 2 de vos passages dans notre boutique) : {}.\n".format(", ".join(Fidelity_products)))
else:
    Customers[name]=[0, {}] #A customer is a list where the first elt is the number of time he/she has commanded in our shop and the second one is a dict where keys are already bought products and values, the number of theirs passed commamds 
   
#We take the command of the customer and we start producing his/her bill
Bill = [["Produit", "Prix unitaire", "Quantité", "Total (FCFA)"]]
Total = 0
command = 0
while True:
    if Products == []:
        print("Nous n'avons plus de produit en stock pour le moment.\n")
        break
    lp = len(Products)
    printTable([["Nom", "Code", "Prix unitaire (FCFA)", "Quantité"]]+Products, "Voici dans l'ordre alphabétique la liste des produits en stock : ")
    product = input("Veuillez entrer le nom ou le code d'un produit qui vous intéresse (NB : une saisie vide interrompt le processus de commande) : ").title()
    print('')
    if product.strip() == '':
        break
    #We verify if the given input is a code or a a name of a wanted product
    if product.isnumeric() == True:
        product = int(product)
        if product == 0 or product > lp:
            bool = input(f"Nous n'avons pas de produit de code '{product}'!\n\nVoulez-vous commander un autre produit ? (o/n) : ").lower()
            print('')
            if bool == 'o':
                continue
            else:
                break
        index = product-1
        product = Products[index][0]
    else:
        #We verify if the wanted product is in stock or if it is similar to a product in stock
        Indices = []
        index = -1
        for i in range(lp):
            if Products[i][0] == product:
                index = i
                break
            if closeSubStr(product, Products[i][0]) == True:
                Indices.append(i)
        if index == -1:
            if Indices == []:
                bool = input(f"Nous n'avons pas le produit '{product}' en stock!\n\nVoulez-vous commander un autre produit ? (o/n) : ").lower()
                if bool == 'o':
                    continue
                else:
                    break
            else:
                print(f"Nous n'avons pas le produit '{product}' en stock! Cependant, vous pourriez faire allusion au(x) produit(s) :\n\tCode\tProduit")
                for i in Indices:
                    print(f"\t{i+1}\t{Products[i][0]}")
                index = input("Entrez le code du produit qui vous interesserait. Si aucun de ces produits ne vous interesse, Entrez :\n\t0 si vous voulez rechercher un autre produit\n\t-1 si vous ne voulez plus commander de produit\nRéponse : ")
                print('')
                if index == '0':
                    continue
                if index == '-1':
                    break
                try:
                    index = int(index)-1
                    assert index in Indices
                    product = Products[index][0]
                except:
                    print("Code invalide! Vous êtes invité à commander un autre produit. Si vous n'êtes plus intéressé, validez juste une saisie vide.\n")
                    continue
                
    command += 1
    #We ask for the quantity of the wanted product
    while True:
        qty = input(f"Entrer la quantité voulue du produit '{product}' : ")
        print('')
        #We verify if the last input is a non-zero positive integer
        try:
            qty = int(qty)
            assert qty >= 1
            break
        except:
            print(f"'{qty}' n'est pas un entier strictement positif.\n")
            continue
    #We check if we have enough of this product to satisfy the customer's request
    if Products[index][3]<qty:
        bool = input(f"Nous n'avons que {Products[index][3]} exemplaire(s) du produit '{product}' en stock.\n\nVoullez vous faire avec ? (o/n) : ").lower()
        print('')
        qty=Products[index][3]
    else:
        bool="o"
        
    if bool=="o":
        #We verify if the customer has already bought at least one time this product before in our shop
        if product in Customers[name][1].keys():
            Customers[name][1][product]+=1
        else:
            Customers[name][1][product]=1
        #We modify the information about the stock of the wanted product
        Products[index][3]-=qty
        #We evealuate the expenditure of the customer and we considerate a reduction of 2% if the customer has been at least twice in our shop
        price=Products[index][2]
        if product in Fidelity_products:
            price=Products[index][2]*0.98
        total = price*qty
        Total += total
        Bill.append([product, price, qty, total])
        #We delete the product in our archives if it is no more in stock and actualise the codes of the following products
        if Products[index][3] == 0:
            Products.pop(index)
            for i in range(index, lp-1):
                Products[i][1] -= 1
        
    bool = input("Voulez-vous prendre un autre produit ? (o/n)  : ").lower()
    print('')
    if bool != "o":
        break

'''We verify that the customer has commmanded at least one product in order to refresh archives and produce his/her bill'''

if command >= 1:
    Customers[name][0] += 1
    #We end with the constitution of the bill
    printTable(Bill, "Voici le bilan de vos commandes : ", f"Cela vous coûtera : {Total} FCFA.") 
    valid = input('Voulez-vous le valider et passer à la caisse ? (o/n) : ').lower()
    print('')
    if valid == 'o':
        if len(Customers) == 1 and Customers[name][0] == 1:
            os.makedirs("Factures", exist_ok=True)
        if Customers[name][0] == 1:
            os.makedirs(f"Factures/{name}", exist_ok=True)
        printTable(Bill, f"Facture de Mme/M. {name.title()}.", f"Total : {Total} FCFA. Merci de votre fidélité!", f"Factures/{name}/{name}{Customers[name][0]}.txt")

        #We print the final bill of the customer
        print("Voici votre facture : ")
        if sys.platform == "win32":
            os.system(f"\"Factures\{name}\{name}{Customers[name][0]}.txt\"")
        if sys.platform == "linux":
            os.system(f"xdg-open \"Factures/{name}/{name}{Customers[name][0]}.txt\"")
        
        #We safeguard the changes made in the archives
        openJsonFile(Products, "Products", "w")      
        openJsonFile(Customers, "Customers", "w") 

input("Ravi de vous avoir servi!")