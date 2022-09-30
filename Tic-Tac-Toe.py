from os import *
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from random import randint

Window=Tk()
Window.geometry("290x275+1000+450")
Window.resizable(width=False, height=False)
Window.title("Tic Tac Toe")

PATH=path.dirname(path.realpath(__file__))
Map=["","","","","","","","",""]
debut=0
tour=0
score=[0,0]
couleurs=["",""]
joueur1=""
joueur2=""
MarioR=ImageTk.PhotoImage(Image.open(PATH+"/Images/mario_R.png"))
MarioV=ImageTk.PhotoImage(Image.open(PATH+"/Images/mario_V.png"))
GameOver=ImageTk.PhotoImage(Image.open(PATH+"/Images/Game over.png"))
couleur=IntVar()
couleur.set(1)
nbparties=1
parties=IntVar()
parties.set(3)
nbpartiestotal=IntVar()
nbpartiestotal.set(0)
nbpartiesgagne=IntVar()
nbpartiesgagne.set(0)
nbjoueurs=IntVar()
nbjoueurs.set(1)
nbvj1=0
nbvj2=0

def selection():
    if parties.get()==1:
        parties1.pack()
        parties2.pack_forget()
    elif parties.get()==2:
        parties1.pack_forget()
        parties2.pack()
    else:
        parties1.pack_forget()
        parties2.pack_forget()

def jouer():
    global debut,joueur1,joueur2,couleurs
    if couleur.get()==1:
        joueur1=MarioR
        joueur2=MarioV
        couleurs=["Red","Green"]
    else:
        joueur1=MarioV
        joueur2=MarioR
        couleurs=["Green","Red"]
    textejoueurs.destroy()
    joueurs.destroy()
    textecouleurs.destroy()
    choixcouleurs1.destroy()
    choixcouleurs2.destroy()
    textepartie.destroy()
    choixpartie1.destroy()
    choixpartie2.destroy()
    choixpartie3.destroy()
    parties1.destroy()
    parties2.destroy()
    enregistrer.destroy()    
    if randint(1,2)==1:
        messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
        debut=1
    else:
        messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
        debut=2
    Window.geometry("245x210+1000+450")
    B1.grid(row=0, column=0, padx=5, pady=5)
    B2.grid(row=0, column=1, padx=5, pady=5)
    B3.grid(row=0, column=2, padx=5, pady=5)
    B4.grid(row=1, column=0, padx=5, pady=5)
    B5.grid(row=1, column=1, padx=5, pady=5)
    B6.grid(row=1, column=2, padx=5, pady=5)
    B7.grid(row=2, column=0, padx=5, pady=5)
    B8.grid(row=2, column=1, padx=5, pady=5)
    B9.grid(row=2, column=2, padx=5, pady=5) 
    B1.bind("<Button-1>",Boutton1)
    B2.bind("<Button-1>",Boutton2)
    B3.bind("<Button-1>",Boutton3)
    B4.bind("<Button-1>",Boutton4)
    B5.bind("<Button-1>",Boutton5)
    B6.bind("<Button-1>",Boutton6)
    B7.bind("<Button-1>",Boutton7)
    B8.bind("<Button-1>",Boutton8)
    B9.bind("<Button-1>",Boutton9)

def check():
    global tour,Map
    if tour==9:
        fin("Egalité")
    elif Map[0]==Map[1]==Map[2]=="X":
        canvas.create_line(45,40,230,40, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[3]==Map[4]==Map[5]=="X":
        canvas.create_line(45,135,230,135, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[6]==Map[7]==Map[8]=="X":
        canvas.create_line(45,225,230,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[0]==Map[3]==Map[6]=="X":
        canvas.create_line(45,40,45,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[1]==Map[4]==Map[7]=="X":
        canvas.create_line(135,40,135,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[2]==Map[5]==Map[8]=="X":
        canvas.create_line(225,40,230,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[0]==Map[4]==Map[8]=="X":
        canvas.create_line(45,40,230,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[2]==Map[4]==Map[6]=="X":
        canvas.create_line(230,40,45,225, fill=couleurs[1], width=5, tags="ligne")
        fin("Joueur 2")
    elif Map[0]==Map[1]==Map[2]=="O":
        canvas.create_line(45,40,230,40, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[3]==Map[4]==Map[5]=="O":
        canvas.create_line(45,135,230,135, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[6]==Map[7]==Map[8]=="O":
        canvas.create_line(45,225,230,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[0]==Map[3]==Map[6]=="O":
        canvas.create_line(45,40,45,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[1]==Map[4]==Map[7]=="O":
        canvas.create_line(135,40,135,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[2]==Map[5]==Map[8]=="O":
        canvas.create_line(230,40,230,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[0]==Map[4]==Map[8]=="O":
        canvas.create_line(45,40,230,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")
    elif Map[2]==Map[4]==Map[6]=="O":
        canvas.create_line(230,40,45,225, fill=couleurs[0], width=5, tags="ligne")
        fin("Joueur 1")

def Boutton1(event):
    global tour,Map,joueur2,joueur1
    if Map[0]=="":
        if debut==1:
            if tour%2:
                Map[0]="X"
                B1.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[0]="O"
                B1.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[0]="O"
                B1.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[0]="X"
                B1.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton2(event):
    global tour,Map,joueur2,joueur1
    if Map[1]=="":
        if debut==1:
            if tour%2:
                Map[1]="X"
                B2.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[1]="O"
                B2.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[1]="O"
                B2.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[1]="X"
                B2.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()
    
def Boutton3(event):
    global tour,Map,joueur2,joueur1
    if Map[2]=="":
        if debut==1:
            if tour%2:
                Map[2]="X"
                B3.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[2]="O"
                B3.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[2]="O"
                B3.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[2]="X"
                B3.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton4(event):
    global tour,Map,joueur2,joueur1
    if Map[3]=="":
        if debut==1:
            if tour%2:
                Map[3]="X"
                B4.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[3]="O"
                B4.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[3]="O"
                B4.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[3]="X"
                B4.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton5(event):
    global tour,Map,joueur2,joueur1
    if Map[4]=="":
        if debut==1:
            if tour%2:
                Map[4]="X"
                B5.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[4]="O"
                B5.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[4]="O"
                B5.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[4]="X"
                B5.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton6(event):
    global tour,Map,joueur2,joueur1
    if Map[5]=="":
        if debut==1:
            if tour%2:
                Map[5]="X"
                B6.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[5]="O"
                B6.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[5]="O"
                B6.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[5]="X"
                B6.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton7(event):
    global tour,Map,joueur2,joueur1
    if Map[6]=="":
        if debut==1:
            if tour%2:
                Map[6]="X"
                B7.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[6]="O"
                B7.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[6]="O"
                B7.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[6]="X"
                B7.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton8(event):
    global tour,Map,joueur2,joueur1
    if Map[7]=="":
        if debut==1:
            if tour%2:
                Map[7]="X"
                B8.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[7]="O"
                B8.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[7]="O"
                B8.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[7]="X"
                B8.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def Boutton9(event):
    global tour,Map,joueur2,joueur1
    if Map[8]=="":
        if debut==1:
            if tour%2:
                Map[8]="X"
                B9.create_image(2, 2, anchor=NW, image=joueur2)
            else:
                Map[8]="O"
                B9.create_image(2, 2, anchor=NW, image=joueur1)
        else:
            if tour%2:
                Map[8]="O"
                B9.create_image(2, 2, anchor=NW, image=joueur1)
            else:
                Map[8]="X"
                B9.create_image(2, 2, anchor=NW, image=joueur2)
        tour+=1
        check()

def fin(Gagnant):
    global tour,Map,debut,score,nbparties,nbvj1,nbvj2
    Map=["","","","","","","","",""]
    if Gagnant=="Egalité":
        messagebox.showinfo(title="Égalité", message="Égalité")
        score[0];score[1]+=1;1
    else:
        messagebox.showinfo(title="Gagnant", message="Le Gagnant est : "+Gagnant)
        if Gagnant=="Joueur 1":
            score[0]+=3
            nbvj1+=1
        else:
            score[1]+=3
            nbvj2+=1
    if (parties.get()==1 and (nbpartiesgagne.get()==nbvj1 or nbpartiesgagne.get()==nbvj2)) or (parties.get()==2 and nbpartiestotal.get()==nbparties) or parties.get()==3:
        win=Toplevel(Window)
        win.title("GameOver")
        taille=str(GameOver.width())+"x"+str(GameOver.height())+"+1000+450"
        win.geometry(taille)
        can=Canvas(win,width=GameOver.width(), height=GameOver.height())
        can.create_image(2, 2, anchor=NW, image=GameOver, tags="image")
        can.pack(fill=BOTH, expand=1)
        message="Le score est actuellement de : "+str(score[0])+" pour le joueur 1 et : "+str(score[1])+" pour le joueur 2. Voulez vous recommencer ?"
        Recommencer=messagebox.askretrycancel(title="Recommencer ?",message=message)
        if Recommencer==True:
            canvas.delete("ligne")
            win.destroy()
            B1.create_image(2, 2, anchor=NW, image="")
            B2.create_image(2, 2, anchor=NW, image="")
            B3.create_image(2, 2, anchor=NW, image="")
            B4.create_image(2, 2, anchor=NW, image="")
            B5.create_image(2, 2, anchor=NW, image="")
            B6.create_image(2, 2, anchor=NW, image="")
            B7.create_image(2, 2, anchor=NW, image="")
            B8.create_image(2, 2, anchor=NW, image="")
            B9.create_image(2, 2, anchor=NW, image="")
            B1.grid(row=0, column=0, padx=5, pady=5)
            B2.grid(row=0, column=1, padx=5, pady=5)
            B3.grid(row=0, column=2, padx=5, pady=5)
            B4.grid(row=1, column=0, padx=5, pady=5)
            B5.grid(row=1, column=1, padx=5, pady=5)
            B6.grid(row=1, column=2, padx=5, pady=5)
            B7.grid(row=2, column=0, padx=5, pady=5)
            B8.grid(row=2, column=1, padx=5, pady=5)
            B9.grid(row=2, column=2, padx=5, pady=5)
            tour=0
            if randint(1,2)==1:
                messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
                debut=1
            else:
                messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
                debut=2
        else:
            Window.quit()
    else:
        canvas.delete("ligne")
        B1.create_image(2, 2, anchor=NW, image="")
        B2.create_image(2, 2, anchor=NW, image="")
        B3.create_image(2, 2, anchor=NW, image="")
        B4.create_image(2, 2, anchor=NW, image="")
        B5.create_image(2, 2, anchor=NW, image="")
        B6.create_image(2, 2, anchor=NW, image="")
        B7.create_image(2, 2, anchor=NW, image="")
        B8.create_image(2, 2, anchor=NW, image="")
        B9.create_image(2, 2, anchor=NW, image="")
        B1.grid(row=0, column=0, padx=5, pady=5)
        B2.grid(row=0, column=1, padx=5, pady=5)
        B3.grid(row=0, column=2, padx=5, pady=5)
        B4.grid(row=1, column=0, padx=5, pady=5)
        B5.grid(row=1, column=1, padx=5, pady=5)
        B6.grid(row=1, column=2, padx=5, pady=5)
        B7.grid(row=2, column=0, padx=5, pady=5)
        B8.grid(row=2, column=1, padx=5, pady=5)
        B9.grid(row=2, column=2, padx=5, pady=5)
        tour=0
        message="Le score est actuellement de : "+str(score[0])+" pour le joueur 1 et : "+str(score[1])+" pour le joueur 2."
        messagebox.showinfo(title="Score", message=message)
        if randint(1,2)==1:
            messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
            debut=1
        else:
            messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
            debut=2
        nbparties+=1

def A_propos():
    messagebox.showinfo(title="A propos", message="mubieox.github.io")


menubar=Menu(Window)

menu_aide=Menu(menubar, tearoff=0)
menu_aide.add_command(label="A propos", command=A_propos)
menu_aide.add_separator()
menu_aide.add_command(label="Quitter", command=Window.quit)
menubar.add_cascade(label="Autre", menu=menu_aide)

canvas=Canvas(Window,width=Window.winfo_width(), height=Window.winfo_height(), bg="orange")
canvas.pack(fill=BOTH, expand=1)

B1=Canvas(canvas,width=68,height=56)
B2=Canvas(canvas,width=68,height=56)
B3=Canvas(canvas,width=68,height=56)
B4=Canvas(canvas,width=68,height=56)
B5=Canvas(canvas,width=68,height=56)
B6=Canvas(canvas,width=68,height=56)
B7=Canvas(canvas,width=68,height=56)
B8=Canvas(canvas,width=68,height=56)
B9=Canvas(canvas,width=68,height=56)

textejoueurs=Label(Window, text="Choisissez le nombre de joueur(s) :")
textejoueurs.pack()
joueurs=Spinbox(Window, from_=1, to=2, textvariable=nbjoueurs)
joueurs.pack()
textecouleurs=Label(Window, text="Joueur 1, choisissez votre couleur :")
textecouleurs.pack()
choixcouleurs1=Radiobutton(Window, text="Rouge", variable=couleur, value=1)
choixcouleurs1.pack()
choixcouleurs2=Radiobutton(Window, text="Vert", variable=couleur, value=2)
choixcouleurs2.pack()
textepartie=Label(Window, text="Voulez-vous definir un nombre prédéfinit de parties ? :")
textepartie.pack()
choixpartie1=Radiobutton(Window, text="Oui, nombre de parties gagnées : ", variable=parties, value=1, command=selection)
choixpartie1.pack()
parties1=Spinbox(Window, from_=0, to=100, textvariable=nbpartiesgagne)
choixpartie2=Radiobutton(Window, text="Oui, nombre de parties totales : ", variable=parties, value=2, command=selection)
choixpartie2.pack()
parties2=Spinbox(Window, from_=0, to=100, textvariable=nbpartiestotal)
choixpartie3=Radiobutton(Window, text="Non", variable=parties, value=3, command=selection)
choixpartie3.pack()

enregistrer=Button(Window, text="Enregistrer", command=jouer)
enregistrer.pack()


Window.config(menu=menubar)
Window.mainloop()