# -*-coding:UTF-8 -*
from Manager_Functions_GUI_2 import*

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

window = Tk(className=" Gestionnaire KLK-Tech") 
canvas = Canvas(window, width = 1000, height=830, borderwidth=0, border=0)
frame = LabelFrame(canvas, text="KLK-Tech, le N°1 en rapport Qualité/Prix!")
scrollbar = frameVerticalScrollbar(window, canvas, frame)

name = inputWindow(window, frame,"Bienvenue chez KLK-Tech! Veuillez entrer votre nom : ").title()
printWindow(frame, f"Une fois de plus bienvenue Mme/M. {name}.")

#We check the fidelity of the customer
Fidelity_products = []
if name in Customers.keys():
    Previous_products = list(Customers[name][1].keys())
    bool =  Previous_products != []
    if bool:
        printWindow(frame,"En nous basant sur vos précédentes visites de notre boutique, vous pourriez être intéréssé par le/les article(s) suivant(s) : {}.".format(", ".join(Previous_products)))
        for product in Previous_products:
            if Customers[name][1][product]>=2:
                Fidelity_products.append(product)
        if Fidelity_products != []:      
            printWindow(frame,"Pour vous remercier de votre fidélité, nous vous offrons une réduction de 2% sur les produits suivants,\n(Vu que pour chacun d'eux, vous nous les avez déjà achetés à au moins 2 de vos passages dans notre boutique) : {}.".format(", ".join(Fidelity_products)))
else:
    Customers[name]=[0, {}] #A customer is a list where the first elt is the number of time he/she has commanded in our shop and the second one is a dict where keys are already bought products and values, the number of theirs passed commamds 
   
#We take the command of the customer and we start producing his/her bill
Bill = [["Produit", "Prix unitaire", "Quantité", "Total (FCFA)"]]
Total = 0
command = 0
while True:
    if Products == []:
        printWindow(frame,"Nous n'avons plus de produit en stock pour le moment.")
        break
    lp = len(Products)
    printWindow(frame, "Voici la liste des produits que nous avons en stock :")
    printTableWindows(frame, ["Nom", "Code", "Prix unitaire (FCFA)", "Quantité"], Products)
    product = inputWindow(window, frame,"Veuillez entrer le nom ou le code d'un produit qui vous intéresse (NB : une saisie vide interrompt le processus de commande) : ").title()
    if product.strip() == '':
        break
    #We verify if the given input is a code or a a name of a wanted product
    if product.isnumeric() == True:
        product = int(product)
        if product == 0 or product > lp:
            bool = inputWindow(window, frame,f"Nous n'avons pas de produit de code '{product}'!\n\nVoulez-vous commander un autre produit ? (o/n) : ").lower()
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
                bool = inputWindow(window, frame,f"Nous n'avons pas le produit '{product}' en stock!\n\nVoulez-vous commander un autre produit ? (o/n) : ").lower()
                if bool == 'o':
                    continue
                else:
                    break
            else:
                printWindow(frame,f"Nous n'avons pas le produit '{product}' en stock! Cependant, vous pourriez faire allusion au(x) produit(s) :")
                liste = Listbox(frame)
                liste.insert(END, "Code Produit")
                for i in Indices:
                    liste.insert(END, f"{i+1}"+" "*(6-len(str(i+1)))+f"{Products[i][0]}")
                liste.pack()
                index = inputWindow(window, frame,"Entrez le code du produit qui vous interesserait. Si aucun de ces produits ne vous interesse, Entrez :\n\t0 si vous voulez rechercher un autre produit\n\t1 si vous ne voulez plus commander de produit\nRéponse : ")
                if index == '0':
                    continue
                if index == '1':
                    break
                try:
                    index = int(index)-1
                    assert index in Indices
                    product = Products[index][0]
                except:
                    printWindow(frame,"Code invalide! Vous êtes invité à commander un autre produit. Si vous n'êtes plus intéressé, validez juste une saisie vide.")
                    continue
                
    command += 1
    #We ask for the quantity of the wanted product
    while True:
        qty = inputWindow(window, frame,f"Entrer la quantité voulue du produit '{product}' : ")
        #We verify if the last input is a non-zero positive integer
        try:
            qty = int(qty)
            assert qty >= 1
            break
        except:
            printWindow(frame,f"'{qty}' n'est pas un entier strictement positif.")
            continue
    #We check if we have enough of this product to satisfy the customer's request
    if Products[index][3]<qty:
        bool = inputWindow(window, frame,f"Nous n'avons que {Products[index][3]} exemplaire(s) du produit '{product}' en stock.\n\nVoullez vous faire avec ? (o/n) : ").lower()
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
        
    bool = inputWindow(window, frame,"Voulez-vous prendre un autre produit ? (o/n)  : ").lower()
    if bool != "o":
        break

'''We verify that the customer has commmanded at least one product in order to refresh archives and produce his/her bill'''

if command >= 1:
    Customers[name][0] += 1
    #We end with the constitution of the bill
    printWindow(frame, "Voici le bilan de vos commandes : ") 
    printTableWindows(frame, Bill[0], Bill[1:])
    printWindow(frame, f"Cela vous coûtera : {Total} FCFA.") 
    valid = inputWindow(window, frame,'Voulez-vous le valider et passer à la caisse ? (o/n) : ').lower()
    if valid == 'o':
        if len(Customers) == 1 and Customers[name][0] == 1:
            os.makedirs("Factures", exist_ok=True)
        if Customers[name][0] == 1:
            os.makedirs(f"Factures/{name}", exist_ok=True)
        printTable(Bill, f"Facture de Mme/M. {name.title()}.", f"Total : {Total} FCFA. Merci de votre fidélité!", f"Factures/{name}/{name}{Customers[name][0]}.txt")
        
        #We print the final bill of the customer
        printWindow(frame,"Voici votre facture : ")
        if sys.platform == "win32":
            os.system(f"\"Factures\{name}\{name}{Customers[name][0]}.txt\"")
        if sys.platform == "linux":
            os.system(f"xdg-open \"Factures/{name}/{name}{Customers[name][0]}.txt\"")
        
        #We safeguard the changes made in the archives
        openJsonFile(Products, "Products", "w")      
        openJsonFile(Customers, "Customers", "w") 

printWindow(frame,"Ravi de vous avoir servi!")