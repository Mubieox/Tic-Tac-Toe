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
Map=[["","",""],["","",""],["","",""]]
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
    global debut,joueur1,joueur2,couleurs,tour
    
    def Bot():
        global Map,joueur2,joueur1,nbjoueurs,tour
        def isMovesLeft(Map) :
            for i in range(9) :
                    if Map[i//3][i%3] == "" :
                        return True
            return False
        def evaluate(b) :
            for row in range(3) :    
                if b[row][0] == b[row][1] == b[row][2] :       
                    if b[row][0] == joueur2 :
                        return 10
                    elif b[row][0] == joueur1 :
                        return -10
            for col in range(3) :
                if b[0][col] == b[1][col] == b[2][col] :
                    if b[0][col] == joueur2 :
                        return 10
                    elif b[0][col] == joueur1 :
                        return -10
            if b[0][0] == b[1][1] == b[2][2] :
                if b[0][0] == joueur2 :
                    return 10
                elif b[0][0] == joueur1 :
                    return -10
            if b[0][2] == b[1][1] == b[2][0] :
                if b[0][2] == joueur2 :
                    return 10
                elif b[0][2] == joueur1 :
                    return -10
            return 0
        def minimax(Map, depth, isMax) :
            score = evaluate(Map)
            if score == 10 :
                return score
            if score == -10 :
                return score
            if isMovesLeft(Map) == False :
                return 0
            if (isMax) :    
                best = -1000
                for i in range(9) :
                        if Map[i//3][i%3]=="" :
                            Map[i//3][i%3] = joueur2
                            best = max( best, minimax(Map,depth + 1,not isMax) )
                            Map[i//3][i%3] = ""
                return best
            else :
                best = 1000
                for i in range(9) :
                        if Map[i//3][i%3] == "" :
                            Map[i//3][i%3] = joueur1
                            best = min(best, minimax(Map, depth + 1, not isMax))
                            Map[i//3][i%3] = ""
                return best
        def findBestMove(Map) :
            bestVal = -1000
            bestMove = 0
            for i in range(9) :
                if Map[i//3][i%3] == "" :
                    Map[i//3][i%3] = joueur2
                    moveVal = minimax(Map, 0, False)
                    Map[i//3][i%3] = ""
                    if moveVal > bestVal :               
                        bestMove = i
                        bestVal = moveVal
            return bestMove
        bestMove = findBestMove(Map)
        Map[bestMove//3][bestMove%3]="X"
        canvas.create_image(80*(bestMove%3)+5, 66*(bestMove//3)+5, anchor=NW, image=joueur2, tags="image")
        tour+=1
        if tour>=3 :
            check("bot")
    
    def check(qui):
        global tour,Map
        jg=""
        for i in range(3):
            if Map[i][0]==Map[i][1]==Map[i][2]=="X":
                canvas.create_line(45,i*65+40,205,i*65+40, fill=couleurs[1], width=5, tags="ligne")
                jg="Joueur 2"
            elif Map[i][0]==Map[i][1]==Map[i][2]=="O":
                canvas.create_line(45,i*65+40,205,i*65+40, fill=couleurs[0], width=5, tags="ligne")
                jg="Joueur 1"
            elif Map[0][i]==Map[1][i]==Map[2][i]=="X":
                canvas.create_line(i*80+45,40,i*80+45,175, fill=couleurs[1], width=5, tags="ligne")
                jg="Joueur 2"
            elif Map[0][i]==Map[1][i]==Map[2][i]=="O":
                canvas.create_line(i*80+45,40,i*80+45,175, fill=couleurs[0], width=5, tags="ligne")
                jg="Joueur 1"
            elif Map[0][0]==Map[1][1]==Map[2][2]=="X":
                canvas.create_line(45,40,205,175, fill=couleurs[1], width=5, tags="ligne")
                jg="Joueur 2"
            elif Map[0][0]==Map[1][1]==Map[2][2]=="O":
                canvas.create_line(45,40,205,175, fill=couleurs[0], width=5, tags="ligne")
                jg="Joueur 1"
            elif Map[0][2]==Map[1][1]==Map[2][0]=="X":
                canvas.create_line(205,40,45,175, fill=couleurs[1], width=5, tags="ligne")
                jg="Joueur 2"
            elif Map[0][2]==Map[1][1]==Map[2][0]=="O":
                canvas.create_line(205,40,45,175, fill=couleurs[0], width=5, tags="ligne")
                jg="Joueur 1"
            elif i==2 and tour==9:
                jg="Egalité"
        if jg!="":
            fin(jg)
        elif nbjoueurs.get()==1 and qui=="bouton":
            Bot()

    def Bouton(event):
        global tour,Map,joueur2,joueur1
        x,y=-1,-1
        for i in range(3):
            if 79*i+5<=event.x<=73+66*i:
                y=i
            if 66*i+5<=event.y<=60+80*i:
                x=i
        if x!=-1 and y!=-1:
            if Map[x][y]=="":
                if debut==1:
                    if tour%2:
                        Map[x][y]="X"
                        canvas.create_image(80*y+5, 66*x+5, anchor=NW, image=joueur2, tags="image")
                    else:
                        Map[x][y]="O"
                        canvas.create_image(80*y+5, 66*x+5, anchor=NW, image=joueur1, tags="image")
                else:
                    if tour%2:
                        Map[x][y]="O"
                        canvas.create_image(80*y+5, 66*x+5, anchor=NW, image=joueur1, tags="image")
                    else:
                        Map[x][y]="X"
                        canvas.create_image(80*y+5, 66*x+5, anchor=NW, image=joueur2, tags="image")
                tour+=1
                if tour>=3 :
                    check("bouton")
                elif nbjoueurs.get()==1 :
                    Bot()

    def fin(Gagnant):
        global tour,Map,debut,score,nbparties,nbvj1,nbvj2,nbjoueurs,joueur1,joueur2,couleurs
        Map=[["","",""],["","",""],["","",""]]
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
            message="Le score est actuellement de "+str(score[0])+" pour le joueur 1 et "+str(score[1])+" pour le joueur 2. Voulez vous recommencer ?"
            Recommencer=messagebox.askretrycancel(title="Recommencer ?",message=message)
            if Recommencer==True:
                canvas.delete("ligne")
                canvas.delete("image")
                win.destroy()
                tour=0
                if randint(1,2)==1:
                    messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
                    debut=1
                else:
                    messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
                    debut=2
                    if nbjoueurs.get()==1:
                        nbrandom=randint(0,8)
                        Map[nbrandom//3][nbrandom%3] = "X"
                        canvas.create_image(80*(nbrandom%3)+5, 66*(nbrandom//3)+5, anchor=NW, image=joueur2, tags="image")
                        tour+=1
            else:
                Window.quit()
        else:
            canvas.delete("ligne")
            canvas.delete("image")
            tour=0
            message="Le score est actuellement de "+str(score[0])+" pour le joueur 1 et "+str(score[1])+" pour le joueur 2."
            messagebox.showinfo(title="Score", message=message)
            if randint(1,2)==1:
                messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
                debut=1
            else:
                messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
                debut=2
                if nbjoueurs.get()==1:
                    nbrandom=randint(0,8)
                    Map[nbrandom//3][nbrandom%3] = "X"
                    canvas.create_image(80*(nbrandom%3)+5, 66*(nbrandom//3)+5, anchor=NW, image=joueur2, tags="image")
                    tour+=1
            nbparties+=1
    
    if couleur.get()==1:
        joueur1=MarioR
        joueur2=MarioV
        couleurs=["Red","Green"]
    else:
        joueur1=MarioV
        joueur2=MarioR
        couleurs=["Green","Red"]
    jeux=Toplevel(Window)
    jeux.geometry("240x200+1000+450")
    canvas=Canvas(jeux,width=jeux.winfo_width(), height=jeux.winfo_height(), bg="orange")
    canvas.pack(fill=BOTH, expand=1)
    canvas.create_line(79,0,79,200,fill="black",width=10)
    canvas.create_line(159,0,159,200,fill="black",width=10)
    canvas.create_line(0,66,240,66,fill="black",width=10)
    canvas.create_line(0,132,240,132,fill="black",width=10)
    if randint(1,2)==1:
        messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 1.")
        debut=1
    else:
        messagebox.showinfo(title="Joueur qui commence", message="Le joueur qui commence est le joueur 2.")
        debut=2
        if nbjoueurs.get()==1:
            nbrandom=randint(0,8)
            Map[nbrandom//3][nbrandom%3]="X"
            canvas.create_image(80*(nbrandom%3)+5, 66*(nbrandom//3)+5, anchor=NW, image=joueur2, tags="image")
            tour+=1
    canvas.bind("<Button-1>", Bouton)

def A_propos():
    messagebox.showinfo(title="A propos", message="mubieox.github.io")

menubar=Menu(Window)

menu_aide=Menu(menubar, tearoff=0)
menu_aide.add_command(label="A propos", command=A_propos)
menu_aide.add_separator()
menu_aide.add_command(label="Quitter", command=Window.quit)
menubar.add_cascade(label="Autre", menu=menu_aide)

textejoueurs=Label(Window, text="Choisissez le nombre de joueur(s) :", bg="orange")
textejoueurs.pack()
joueurs=Spinbox(Window, from_=1, to=2, textvariable=nbjoueurs, bg="orange")
joueurs.pack()
textecouleurs=Label(Window, text="Joueur 1, choisissez votre couleur :", bg="orange")
textecouleurs.pack()
choixcouleurs1=Radiobutton(Window, text="Rouge", variable=couleur, value=1, bg="orange")
choixcouleurs1.pack()
choixcouleurs2=Radiobutton(Window, text="Vert", variable=couleur, value=2, bg="orange")
choixcouleurs2.pack()
textepartie=Label(Window, text="Voulez-vous definir un nombre prédéfinit de parties ? :", bg="orange")
textepartie.pack()
choixpartie1=Radiobutton(Window, text="Oui, nombre de parties gagnées : ", variable=parties, value=1, command=selection, bg="orange")
choixpartie1.pack()
parties1=Spinbox(Window, from_=0, to=100, textvariable=nbpartiesgagne, bg="orange")
choixpartie2=Radiobutton(Window, text="Oui, nombre de parties totales : ", variable=parties, value=2, command=selection, bg="orange")
choixpartie2.pack()
parties2=Spinbox(Window, from_=0, to=100, textvariable=nbpartiestotal, bg="orange")
choixpartie3=Radiobutton(Window, text="Non", variable=parties, value=3, command=selection, bg="orange")
choixpartie3.pack()

enregistrer=Button(Window, text="Enregistrer", command=jouer, bg="orange")
enregistrer.pack()

Window.config(menu=menubar, bg="orange")
Window.mainloop()