from tkinter import *
from random import *
from tkinter.messagebox import *
from json import *

# NB: 0 représente les proverbes simples, tandis 1 représente les proverbes complexes

# Proverbes chargés depuis le fichier json
try:
  with open("donnee.json", "r", encoding="utf-8") as f:
    liste_pvb = load(f)
except FileNotFoundError:
  print("Il vous manque un fichier")

cate = []
for valeur in liste_pvb.values():
  cate.append(valeur)

# ==================== FONCTIONS DE L'APPLICATION ====================

def verifier_caracteristiques1(i_debut, i_fin, limite, pvb):
    pvb1 = pvb[i_debut]
    pvb2 = pvb[i_fin]

    # Si le proverbes de départ est une phrase simple, le deuxième proverbe doit aussi l'être
    # Sinon, on passe directement à la recherche d'un proverbe ayant les mêmes caractéristiques grammaticales et sémantique à part lui-même
    if pvb1["type de phrase"] == "phrase simple":
      candidats = [pvb.index(p) for p in pvb if ((pvb1["caractéristiques"] == p["caractéristiques"]) and (pvb.index(p) != i_debut) and (p["type de phrase"] != "subordonnée relative"))]
    else:
      candidats = [pvb.index(p) for p in pvb if ((pvb1["caractéristiques"] == p["caractéristiques"]) and (pvb.index(p) != i_debut))]
    if candidats == []:
        print("Pas de valeur similaire")
        return -1
    else:
        i_fin = candidats[randint(0, len(candidats) - 1)]
    return i_fin

def verifier_caracteristiques2(i_debut, i_fin, pvb):
  pvb1 = pvb[i_debut]
  pvb2 = pvb[i_fin]

  # A la recherche d'un proverbe ayant les mêmes caractéristiques grammaticales autre que le proverbe  de départ
  # Si ils ont le même sens, le connecteur qui les séparera sera ";", sinon on utilisera des connecteurs d'opposition
  connecteur = (", mais", ", sauf que", ", toutefois")
  candidats = [pvb.index(p) for p in pvb if ((pvb1["caractéristiques"][0:2] == p["caractéristiques"][0:2]) and (pvb.index(p) != i_debut))]
  if candidats == []:
      print("Pas de valeur similaire")
      return -1, None
  else:
      i_fin = candidats[randint(0, len(candidats) - 1)]
      pvb2 = pvb[i_fin]
  if pvb1["caractéristiques"][2] != pvb2["caractéristiques"][2]:
    i_dernier_connecteur = len(connecteur) - 1
    mot = connecteur[randint(0, i_dernier_connecteur)]
  else:
    mot = ' ;'
  return i_fin, mot


# Fonction proncipale
def generer_citation(citation, opt, choix):
    if type(choix) == StringVar: 
      choix = choix.get()
      if choix == "": # Si l'utilisateur n'a pas choisi de catégorie alors on en génère un aléatoirement
        i_dernier_cate = len(cate) - 1
        choix = cate[randint(0, i_dernier_cate)]
      else:
        choix = liste_pvb[choix]
    pvb = choix[opt]
    if pvb == []:
      return None
    limite = len(pvb) - 1
    i_debut = randint(0, limite)
    i_fin = randint(0, limite)

    if opt == 1: # Ici, on génère des proverbe long

        i_fin, connecteur = verifier_caracteristiques2(i_debut, i_fin, pvb)

        # Si il n'y a pas de proverbes qui peut être mélangé avec celui de départ, on regénère un nouveau
        if i_fin == -1:
          generer_citation(citation, 1, choix)
          return None
        debut_citation = pvb[i_debut]["proverbe"] + connecteur
        fin_citation = pvb[i_fin]["proverbe"]
        fin_citation = fin_citation[0].lower() + fin_citation[1:]
        pvb1 = debut_citation
        pvb2 = fin_citation

    else: # Ici, in génère des proverbe court
      
        i_fin = verifier_caracteristiques1(i_debut, i_fin, limite, pvb)

        # Si il n'y a pas de proverbes qui peut être mélangé avec celui générer de base, on regénère un nouveau
        if i_fin == -1: 
          generer_citation(citation, 0, choix)
          return None
        pvb1 = pvb[i_debut]["1ere partie"] + " " + pvb[i_debut]["2eme partie"]
        pvb2 = pvb[i_fin]["1ere partie"] + " " + pvb[i_fin]["2eme partie"]
        debut_citation = pvb[i_debut]["1ere partie"]
        fin_citation = pvb[i_fin]["2eme partie"]
    
    # Màj des étiquettes
    citation.config(text = f'~~~~ " {debut_citation} {fin_citation} " ~~~~')
    combinaison.config(text = f""" "{pvb1}" \n et \n "{pvb2}" """)

def ajouter_pvb(options, categorie, new_categorie, new_caracteristiques, liste_pvb, proverbe, verbe = None):

  # On récupère ce que l'utilisateur a saisi
  proverbe = proverbe.get()
  new_caracteristiques = new_caracteristiques.get().lower()
  new_caracteristiques = new_caracteristiques.replace(" ", "")
  new_caracteristiques = new_caracteristiques.split(",")
  new_categorie = new_categorie.get().strip().lower()
  
  # On affiche un message d'erreur si l'utilisateur n'a rien entré
  if (proverbe == "") or (new_caracteristiques == "") or (new_categorie == ""):
    creer_fenetre_alerte()
    return None

  caracteristiques = []
  for car in new_caracteristiques:
    caracteristiques.append(car)

  if new_categorie not in options:
    liste_pvb.update({new_categorie: [[], []]})
    new_categorie = f"{new_categorie}"
    categorie["menu"].add_command(label = new_categorie)

  if verbe != None:
    verbe = verbe.get()
    proverbe = proverbe.split(verbe, 1)
    if ("Qui" in proverbe[0]) or ("qui" in proverbe[0]):
      type_phrase = "subordonnée relative"
    else:
      type_phrase = "phrase simple"
    zone = liste_pvb[new_categorie][0]
    ajout = {
      "1ere partie": proverbe[0],
      "2eme partie": verbe + proverbe[1],
      "type de phrase": type_phrase,
      "caractéristiques": caracteristiques
    }
    zone.append(ajout)
  else:
    zone = liste_pvb[new_categorie][1]
    ajout = {
      "proverbe": proverbe,
      "caractéristiques": caracteristiques
    }
    zone.append(ajout)
  with open("donnee.json", "w", encoding="utf-8") as f:
    dump(liste_pvb, f, indent = 4, ensure_ascii = False)
  return None


# ==================== INTERFACE GRAPHIQUE ====================

# Couleur par défaut
blanc = "#dddddd"
noir = "#333333"
bleu = "#0099ff"

# Fonctions de design
def creer_fenetre_alerte():
    main.bell()
    showwarning("Attention", "vous avez oubliez de saisir quelque chose")

def changer_sombre(fenetre):
  for widget in fenetre.winfo_children():
    fg_inchange = [bienvenue, theme]
    if type(widget) == Label and (widget not in fg_inchange):
      widget.config(bg = noir, fg = blanc)
    elif type(widget) == Label:
      widget.config(bg = noir)
    elif (type(widget)) == Frame:
      widget.config(bg = noir)
      changer_sombre(widget) 
  main.config(bg = noir)
  citation.config(bg = noir, fg = "orange")
  sombre.config(bg = bleu, fg = "white")
  clair.config(bg = blanc, fg = "black")

def changer_clair(fenetre):
  for widget in fenetre.winfo_children():
    fg_inchange = [bienvenue, theme]
    if type(widget) == Label and (widget not in fg_inchange):
      widget.config(bg = blanc, fg = "black")
    elif type(widget) == Label:
      widget.config(bg = blanc)
    elif (type(widget)) == Frame:
      widget.config(bg = blanc)
      changer_clair(widget)
  main.config(bg = blanc)
  citation.config(bg = blanc, fg = "green")
  sombre.config(bg = blanc, fg = "black")
  clair.config(bg = bleu, fg = "white")

def ignorer(opt, verbe, instruction):
  save.pack()
  if opt == 0:
    instruction.config(text = "Catégorie, Caractéristiques (nombre, genre, sens + ou -), \nProverbe et Verbe noyau")
    verbe.pack(padx = 10, pady = 10)
    save.config(command = lambda: ajouter_pvb(options, categorie, new_categorie, new_caracteristiques, liste_pvb, proverbe, verbe))
  else:
    instruction.config(text = f"""Catégorie, Caractéristiques (nombre, genre, sens + ou -) et Proverbe \n\nLe genre sera "invariable" si le sujet du proverbe n'est pas bien défini """)
    verbe.pack_forget()
    save.config(command = lambda: ajouter_pvb(options, categorie, new_categorie, new_caracteristiques, liste_pvb, proverbe))

# Fenêtre principale
main = Tk()
main.title('Générateur de citations')
main.iconbitmap('projet_algo.ico')
main.config(bg = blanc)
main.state('zoomed')
main.option_add("*Background", blanc)
main.option_add("*Button.Background", bleu)
main.option_add("*Button.Foreground", "white")
main.option_add("*Button.Relief", "solid")
main.option_add("*Entry.Background", "white")
main.option_add("*Font", "Arial 15")
#=============================================


bienvenue = Label(main, text = f"{7 * "—"} Bienvenue sur le générateur de citations ! {7 * "—"}", font = ("Arial", 25), fg = "#0077ff")
bienvenue.pack(ipadx = 10, ipady = 10)


# Theme de l'application
theme = Label(main, text = "Thème de l'application", fg = "#777777")
theme.pack()

cadre1 = Frame(main)
cadre1.pack()

clair = Button(cadre1, text = "|| Clair", command = lambda: changer_clair(main))
clair.pack(side = "left", padx = 5, pady = 5)

sombre = Button(cadre1, text = "◯ Sombre", bg = blanc, fg = "black", command = lambda: changer_sombre(main))
sombre.pack(padx = 5, pady = 5)
#=============================================


# Widgets principaux
cadre2 = Frame(main)
cadre2.pack()

Label(cadre2, text = "Choisissez la catégorie de proverbes que vous souhaitez ").pack(side = "left")

choix = StringVar(cadre2)
choix.set("")
options = []
for cle in liste_pvb.keys():
  options.append(cle)
categorie = OptionMenu(cadre2, choix, *options)
categorie.pack(side = "bottom")

generer1 = Button(main, text = "Générer un proverbe court", command = lambda: generer_citation(citation, 0, choix))
generer1.pack(padx = 10, pady = 10)

generer2 = Button(main, text = "Générer un proverbe long", command = lambda: generer_citation(citation, 1, choix))
generer2.pack(padx = 10, pady = 10)

citation = Label(main, text = '~~~~""~~~~', font = ("Imperial Script", 25, "bold"), fg = "green")
citation.pack()

combinaison = Label(main, text = "Vous verrez ici quels proverbes on été combinés", font = ("Lucida Bright", 13, "bold"))
combinaison.pack()

cadre3 = Frame(main)
cadre3.pack()

simple = Button(cadre3, text = "Ajouter un proverbe simple", command = lambda: ignorer(0, verbe, instruction))
simple.pack(padx = 10, pady = 10)

complexe = Button(cadre3, text = "Ajouter proverbe complexe", command = lambda: ignorer(1, verbe, instruction))
complexe.pack(padx = 10, pady = 10)

Label(cadre3, text = "Les proverbes simples sont des proverbes qui n'ont qu'un seul verbe noyau \n ou qui sont des phrases contenant une subordonnée relative")

instruction = Label(cadre3, text = "")
instruction.pack()
new_categorie = Entry(cadre3)
new_categorie.pack(side = "left", padx = 10, pady = 10)

new_caracteristiques = Entry(cadre3)
new_caracteristiques.pack(side = "left", padx = 10, pady = 10)

proverbe = Entry(cadre3)
proverbe.pack(side = "left", padx = 10, pady = 10)

verbe = Entry(cadre3)
verbe.pack(padx = 10, pady = 10)

save = Button(main, text = "Enregistrer")

#=============================================

mainloop()