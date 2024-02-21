from email.mime import image
import imaplib
from tkinter import *
from tkinter import messagebox, ttk
import tempfile
import random
from time import strftime
import os

#interface graphique
class SuperMarche:
    def __init__(self, root):
        self.root = root
        self.root.title("KLK_TEK")
        self.root.geometry("2000x1000+0+0")
        title = Label(self.root, text="KLK_TEK", font=("Algerian", 45), bg="cyan", fg="black")
        title.pack(side=TOP, fill=X)

        def heure():
            heur = strftime("%H:%M:%S")
            lblheure.config(text=heur)
            lblheure.after(1000,heure)

        lblheure = Label(self.root, text="HH:MM:SS", font=("times new roman", 15, "bold"),bg="cyan", fg="black")
        lblheure.place(x=0, y=25, width=120, height=45)
        
        heure()
        
        #fin heure
        
        # Déclaration des variables

        self.c_nom = StringVar()
        self.c_phon = StringVar()

        self.n_factu = StringVar()
        z = random.randint(1000,9999)
        self.n_factu.set(z)

        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = IntVar()
        self.qte = IntVar()
        self.totalbrute = StringVar()
        self.taxe = StringVar()
        self.totalnet = StringVar()

        ##Liste catégorie

        self.list_categorie = ["Selection", "Stockage", "Impression"]

        #Sous catégorie stockage 

        self.list_souscategorieStockage = ["Clé USB", "CD Rom", "Disque Dur"]
        
        self.cle_usb = ["4G", "8G", "16G","32G","64G"]
        self.price_4G = 2000
        self.price_8G = 3500
        self.price_16G = 5000
        self.price_32G = 7000
        self.price_64G = 9000

        self.cd_rom = ["4Go", "8Go", "16Go","32Go","64Go"]
        self.price_4Go = 1000
        self.price_8Go = 2500
        self.price_16Go = 4000
        self.price_32Go = 6000
        self.price_64Go = 7500

        self.disque_dur = ["4Gb", "8Gb", "16Gb","32Gb","64Gb"]
        self.price_4Gb = 3000
        self.price_8Gb = 5000
        self.price_16Gb = 8000
        self.price_32Gb = 10000
        self.price_64Gb = 12000

        #Sous catégorie impression 

        self.list_souscategorieImpression = ["Ram de format", "Imprimante", "Encre"]

        self.Ram_de_format = ["A0", "A1", "A2","A3","A4"]
        self.price_A0 = 17500
        self.price_A1 = 15000
        self.price_A2 = 12500
        self.price_A3 = 10000
        self.price_A4 = 7500

        self.Imprimante = ["LX", "LL", "XX","XS","SS"]
        self.price_LX = 35000
        self.price_LL = 50000
        self.price_XX = 65000
        self.price_XS = 75000
        self.price_SS = 90000

        self.Encre = ["LXL", "XXL", "XSX","XSL","SLS"]
        self.price_LXL = 3500
        self.price_XXL = 5000
        self.price_XSX = 6500
        self.price_XSL = 8000
        self.price_SLS = 9500
        
        #interface graphique
        Main_Frame = Frame(self.root, bd=2, relief=GROOVE, bg='white')
        Main_Frame.place(x=0, y=72, width=1850, height=2000)

        #client
        client_frame = LabelFrame(Main_Frame, text="client", font=("times new roman", 15), bg="white")
        client_frame.place(x=3, y=0, width=320, height=120)

        self.lbl_contact = Label(client_frame, text='contact', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_contact.grid(row=0, column=0, sticky=W,  padx=0, pady=0)

        self.lbl_nomClient = Label(client_frame, text='Nom Client', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_nomClient.grid(row=1, column=0, sticky=W,  padx=0, pady=0)

        self.lbl_email = Label(client_frame, text='Email', font=("times new roman", 15, "bold"), bg="white")
        self.lbl_email.grid(row=2, column=0, sticky=W,  padx=0, pady=0)

        self.txt_contact = ttk.Entry(client_frame, textvariable=self.c_phon, font=("times new roman", 15))
        self.txt_contact.grid(row=0, column=1, sticky=W,  padx=0, pady=0)

        self.txt_nomClient = ttk.Entry(client_frame, textvariable=self.c_nom, font=("times new roman", 15))
        self.txt_nomClient.grid(row=1, column=1, sticky=W,  padx=0, pady=0)

        self.txt_email = ttk.Entry(client_frame, textvariable=self.c_email, font=("times new roman", 15))
        self.txt_email.grid(row=2, column=1, sticky=W,  padx=0, pady=0)

        #Nos produits

        produit_frame = LabelFrame(Main_Frame, text="Produit", font=("times new roman", 15), bg="white")
        produit_frame.place(x=330, y=0, width=600, height=120)

        self.lbl_categori = Label(produit_frame, text="Selectionnez la catégorie", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_categori.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        self.lbl_souscategori = Label(produit_frame, text="Sous catégorie", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_souscategori.grid(row=1, column=0, sticky=W, padx=0, pady=0)

        self.lbl_nomproduit = Label(produit_frame, text="Nom Produit", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_nomproduit.grid(row=2, column=0, sticky=W, padx=0, pady=0)

        self.lbl_prix = Label(produit_frame, text="Prix", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_prix.grid(row=0, column=2, sticky=W, padx=0, pady=0)
        
        self.lbl_qte = Label(produit_frame, text="Quantité", font=("times new roman", 15, "bold"), bg="white")
        self.lbl_qte.grid(row=1, column=2, sticky=W, padx=0, pady=0)

        self.txt_categorie = ttk.Combobox(produit_frame, font=("times new roman", 10), values=self.list_categorie, width=20, state="readonly")
        self.txt_categorie.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.txt_categorie.current(0)
        self.txt_categorie.bind("<<ComboboxSelected>>", self.fonctionCategorie)

        self.txt_souscategorie = ttk.Combobox(produit_frame, font=("times new roman", 10), values=[""], width=20, state="readonly")
        self.txt_souscategorie.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.txt_souscategorie.current(0)
        self.txt_souscategorie.bind("<<ComboboxSelected>>", self.fonctionsousCategorie)

        self.txt_nomproduit = ttk.Combobox(produit_frame, font=("times new roman", 10), textvariable=self.produit, width=20, state="readonly")
        self.txt_nomproduit.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.txt_nomproduit.bind("<<ComboboxSelected>>", self.fonctionnomproduit)

        self.txt_prix = ttk.Combobox(produit_frame, font=("times new roman", 10), textvariable=self.prix, width=20, state="readonly")
        self.txt_prix.grid(row=0, column=3, sticky=W, padx=0, pady=0)

        self.txt_qte = ttk.Entry(produit_frame, font=("times new roman", 10), textvariable=self.qte, width=20)
        self.txt_qte.grid(row=1, column=3, sticky=W, padx=0, pady=0)
        
        #recherche

        recher_Frame = Frame(Main_Frame, bd=2, bg="white")
        recher_Frame.place(x=935, y=0, width=1000, height=70)

        self.lbl_recherche = Label(recher_Frame, text="N° Facture",font=("times new roman",20, "bold"), bg='white')
        self.lbl_recherche.grid(row=0, column=0, sticky=W, padx=0, pady=0)

        self.txt_recherche = ttk.Entry(recher_Frame, textvariable=self.rech_factu, font=("times new roman",23), width=9)
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        self.btn_recherch = Button(recher_Frame, text="Rechercher", command=self.rechercher, height=2, font=("times new roman", 10, "bold"), bg="yellow", width=15, cursor="hand2")
        self.btn_recherch.grid(row=0, column=2)

        #Espace Facture

        Facture_label = LabelFrame(Main_Frame, text="Facture", font=("times new roman", 15, "bold"), bg="white")
        Facture_label.place(x=940, y=45, width=415, height=467)

        scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        self.textarea = Text(Facture_label, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), bg="white", fg="blue")
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        #en bas
        enbas_frame = LabelFrame(Main_Frame, text="Boutton", font=("times new roman", 15), bg="white")
        enbas_frame.place(x=0, y=511, width=1355, height=150)

        self.lbl_totalbrute = Label(enbas_frame, text="Total Brute", font=("times new roman", 20, "bold"), bg="white")
        self.lbl_totalbrute.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.lbl_taxe = Label(enbas_frame, text="Taxe", font=("times new roman", 20, "bold"), bg="white")
        self.lbl_taxe.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.lbl_totalnet = Label(enbas_frame, text="Total Net", font=("times new roman", 20, "bold"), bg="white")
        self.lbl_totalnet.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txt_totalbrute = ttk.Entry(enbas_frame, textvariable=self.totalbrute, font=("times new roman", 20), width=13, state='readonly')
        self.txt_totalbrute.grid(row=0, column=1, sticky=W, padx=0, pady=0)

        self.txt_taxe = ttk.Entry(enbas_frame, textvariable=self.taxe, font=("times new roman", 20), width=13, state='readonly')
        self.txt_taxe.grid(row=1, column=1, sticky=W, padx=0, pady=0)

        self.txt_totalnet = ttk.Entry(enbas_frame, textvariable=self.totalnet, font=("times new roman", 20), width=13, state='readonly')
        self.txt_totalnet.grid(row=2, column=1, sticky=W, padx=0, pady=0)

        #image
        
        #boutton
        
        Btn_Frame = Frame(enbas_frame, bd=0, bg="white")
        Btn_Frame.place(x=350, y=0)
        
        self.ajoutPanier = Button(Btn_Frame, text="Ajouter Card", command=self.ajouter, height=2, font=("times new roman", 14, "bold"), bg="green", width=14, cursor="hand2")
        self.ajoutPanier.grid(row=0, column=0)
        
        self.generer = Button(Btn_Frame, text="Générer", command=self.genererFacture, height=2, font=("times new roman", 14, "bold"), bg="green", width=14, cursor="hand2")
        self.generer.grid(row=0, column=1)
        
        self.sauvegarde = Button(Btn_Frame, text="Sauvegarde Facture", command=self.sauvegarder, height=2, font=("times new roman", 14, "bold"), bg="green", width=15, cursor="hand2")
        self.sauvegarde.grid(row=0, column=2)
        
        self.imprime = Button(Btn_Frame, text="Imprimer", command=self.imprimer, height=2, font=("times new roman", 14, "bold"), bg="green", width=14, cursor="hand2")
        self.imprime.grid(row=0, column=3)
        
        self.reini = Button(Btn_Frame, text="Réinitialiser", command=self.rein, height=2, font=("times new roman", 14, "bold"), bg="green", width=14, cursor="hand2")
        self.reini.grid(row=0, column=4)
        
        self.quitte = Button(Btn_Frame, text="Quitter", height=2, font=("times new roman", 14, "bold"), bg="green", width=13, cursor="hand2")
        self.quitte.grid(row=0, column=5)
        
        self.Bienvenu()
        self.l=[]

        #Fonctions
        
    def Bienvenu(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\tBienvenu Chez KLK-TEK")
        self.textarea.insert(END, f"\n\nNuméro Facture : {self.n_factu.get()}")
        self.textarea.insert(END, f"\nNom Client : {self.c_nom.get()}")
        self.textarea.insert(END, f"\nTéléphone : {self.c_phon.get()}")
        self.textarea.insert(END, f"\nEmail : {self.c_email.get()}")
        self.textarea.insert(END, "\n**************************************")
        self.textarea.insert(END, f"\nProduits\t\tQTE\t\tPrix")
        self.textarea.insert(END, "\n**************************************")
        
    def sauvegarder(self):
        op=messagebox.askyesno("Sauvegarder","Voulez-vous sauvegarder la facture ?")
        if op== True:
            self.donneFacture=self.textarea.get(1.0,END)
            f1=open("C:/Users/HP/Desktop/exposé final/Facture/"+str(self.n_factu.get())+".txt","w")
            f1.write(self.donneFacture)
            messagebox.showinfo("Sauvegarder", f"La facture numéro {self.n_factu.get()} a été enregistrée avec succès")
            f1.close()
        
    def ajouter(self):
        self.n = self.prix.get()
        self.m = self.qte.get() * self.n
        self.l.append(self.m)
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Selectionnez un produit")
        else:
            self.textarea.insert(END, f"\n{self.produit.get()}\t\t{self.qte.get()}\t\t{self.m}")
            self.totalbrute.set(str("Rs.%.2f"%(sum(self.l))))
            self.taxe.set(str("Rs.%.2f"%((((sum(self.l))-(self.prix.get()))*1)/100)))
            self.totalnet.set(str("Rs.%.2f"%(((sum(self.l))+((((sum(self.l))-(self.prix.get()))*1)/100)))))
            
    def genererFacture(self):
        if self.produit.get()=="":
            messagebox.showerror("Erreur", "Ajouter d'abord un produit")
        else:
            text= self.textarea.get(9.10, (12.0+float(len(self.l))))
            self.Bienvenu()
            text = self.textarea.insert(END, text)
            self.textarea.insert(END, "\n**************************************")
            self.textarea.insert(END, f"\nTotal Brute : \t\t{self.totalbrute.get()}")
            self.textarea.insert(END, f"\nTaxe : \t\t{self.taxe.get()}")
            self.textarea.insert(END, f"\nTotal Net : \t\t{self.totalnet.get()}")
            
            
    def imprimer(self):
        fichier = tempfile.mktemp(".txt")
        open(fichier, "w").write(self.textarea.get("1.0",END))
        os.startfile(fichier, "print")
        
    def rechercher(self):
        trouver ="non"
        for i in os.listdir("C:/Users/HP/Desktop/exposé final/Facture"):
            if i.split(".")[0]==self.rech_factu.get():
                f1 = open(f"C:/Users/HP/Desktop/exposé final/Facture/{i}","r")
                self.textarea.delete(1.0, END)
                for d in f1:
                    self.textarea.insert(END, d)
                    f1.close
                    trouver="oui"
        if trouver=="non":
            messagebox.showerror("Erreur", "La facture n'existe pas")
            
    def rein(self):
        self.textarea.delete(1.0, END)
        self.c_nom.set("")
        self.c_phon.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.n_factu.set(str(x))
        self.rech_factu.set("")
        self.produit.set("")
        self.prix.set(0)
        self.qte.set(0)
        self.l=[0]
        self.totalbrute.set("")
        self.taxe.set("")
        self.totalnet.set("")
        self.Bienvenu()

    def fonctionCategorie(self, event=""):
        if self.txt_categorie.get()=="Stockage":
            self.txt_souscategorie.config(values=self.list_souscategorieStockage)
            self.txt_souscategorie.current(0)

        if self.txt_categorie.get()=="Impression":
            self.txt_souscategorie.config(values=self.list_souscategorieImpression)
            self.txt_souscategorie.current(0)

    def fonctionsousCategorie(self, event=""):
        #stockage
        if self.txt_souscategorie.get()=="Clé USB":
            self.txt_nomproduit.config(values=self.cle_usb)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="CD Rom":
            self.txt_nomproduit.config(values=self.cd_rom)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Disque Dur":
            self.txt_nomproduit.config(values=self.disque_dur)
            self.txt_nomproduit.current(0)

        #impression
        if self.txt_souscategorie.get()=="Ram de format":
            self.txt_nomproduit.config(values=self.Ram_de_format)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Imprimante":
            self.txt_nomproduit.config(values=self.Imprimante)
            self.txt_nomproduit.current(0)

        if self.txt_souscategorie.get()=="Encre":
            self.txt_nomproduit.config(values=self.Encre)
            self.txt_nomproduit.current(0)
        
    def fonctionnomproduit(self, event=""):
        if self.txt_nomproduit.get()=="4G":
            self.txt_prix.config(values=self.price_4G)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="8G":
            self.txt_prix.config(values=self.price_8G)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="16G":
            self.txt_prix.config(values=self.price_16G)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="32G":
            self.txt_prix.config(values=self.price_32G)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="64G":
            self.txt_prix.config(values=self.price_64G)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="4Go":
            self.txt_prix.config(values=self.price_4Go)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="8Go":
            self.txt_prix.config(values=self.price_8Go)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="16Go":
            self.txt_prix.config(values=self.price_16Go)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="32Go":
            self.txt_prix.config(values=self.price_32Go)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="64Go":
            self.txt_prix.config(values=self.price_64Go)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="4Gb":
            self.txt_prix.config(values=self.price_4Gb)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="8Gb":
            self.txt_prix.config(values=self.price_8Gb)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="16Gb":
            self.txt_prix.config(values=self.price_16Gb)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="32Gb":
            self.txt_prix.config(values=self.price_32Gb)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="64Gb":
            self.txt_prix.config(values=self.price_64Gb)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="A0":
            self.txt_prix.config(values=self.price_A0)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="A1":
            self.txt_prix.config(values=self.price_A1)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="A2":
            self.txt_prix.config(values=self.price_A2)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="A3":
            self.txt_prix.config(values=self.price_A3)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="A4":
            self.txt_prix.config(values=self.price_A4)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="LX":
            self.txt_prix.config(values=self.price_LX)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="LL":
            self.txt_prix.config(values=self.price_LL)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="XX":
            self.txt_prix.config(values=self.price_XX)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="XS":
            self.txt_prix.config(values=self.price_XS)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="SS":
            self.txt_prix.config(values=self.price_SS)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="LXL":
            self.txt_prix.config(values=self.price_LXL)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="XXL":
            self.txt_prix.config(values=self.price_XXL)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="XSX":
            self.txt_prix.config(values=self.price_XSX)
            self.txt_prix.current(0)
            self.qte.set(1)
        
        if self.txt_nomproduit.get()=="XSL":
            self.txt_prix.config(values=self.price_XSL)
            self.txt_prix.current(0)
            self.qte.set(1)

        if self.txt_nomproduit.get()=="SLS":
            self.txt_prix.config(values=self.price_SLS)
            self.txt_prix.current(0)
            self.qte.set(1)

        

    

if __name__=="__main__":
    root=Tk()
    obj = SuperMarche(root)
    root.mainloop()