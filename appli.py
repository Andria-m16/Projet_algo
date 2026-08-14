from tkinter import *
from random import *

def changer_sombre():
  main.config(bg = "#333333")
  theme.config(bg = "#333333", fg = "white")
  instruction.config(bg = "#333333", fg = "white")
  citation.config(bg = "#333333", fg = "white")
  bienvenue.config(bg = "#333333", fg = "white")
  cadre.config(bg = "#333333")
  clair.config(bg = "#333333", fg = "white")
  sombre.config(bg = "#333333", fg = "white")

def changer_clair():
  main.config(bg = "white")
  theme.config(bg = "white", fg = "black")
  instruction.config(bg = "white", fg = "black")
  citation.config(bg = "white", fg = "black")
  bienvenue.config(bg = "white", fg = "black")
  cadre.config(bg = "white")
  clair.config(bg = "white", fg = "black")
  sombre.config(bg = "white", fg = "black")

main = Tk()
main.title('Générateur de citations')
main.iconbitmap('projet_algo.ico')
main.config(bg = "white")
main.option_add("*Background", "white")
main.state('zoomed')
main.option_add("*Button.Relief", "solid")
main.option_add("*Font", "Arial 15")

bienvenue = Label(main, text = "Bienvenue sur le générateur de citations !", font = ("Arial", 25))
bienvenue.pack(ipadx = 10, ipady = 10)

cadre = Frame(main)
cadre.pack()

theme = Label(cadre, text = "Thème de l'application")
theme.pack()

clair = Radiobutton(cadre, text = "Clair", command = changer_clair)
clair.pack(side = "left")

sombre = Radiobutton(cadre, text = "Sombre", command = changer_sombre)
sombre.pack()
sombre.deselect()

instruction = Label(main, text = "Appuyer sur le bouton pour générer une citation inédite !")
instruction.pack()

generer = Button(main, text = "Générer un proberbe court", bg = "#0099ff", fg = "white", activebackground = "orange", command = lambda: generer_citation(citation, 0))
generer.pack(padx = 10, pady = 10)

generer = Button(main, text = "Générer un proberbe long", bg = "#0099ff", fg = "white", activebackground = "orange", command = lambda: generer_citation(citation, 1))
generer.pack(padx = 10, pady = 10)


citation = Label(main, text = '""', font = ("Imperial Script", 25, "bold"))
citation.pack()

pvb_cmplx = [
{
  "catégorie": "Sagesse",
  "1ere partie": "La nuit",
  "2eme partie": "porte conseil",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Qui sème le vent",
  "2eme partie": "récolte la tempête",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Qui veut voyager loin",
  "2eme partie": "ménage sa monture",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Les absents",
  "2eme partie": "ont toujours tort",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "neutre", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "L'erreur",
  "2eme partie": "est humaine",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Qui trop embrasse",
  "2eme partie": "mal étreint",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Qui veut la fin",
  "2eme partie": "veut les moyens",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Les actes",
  "2eme partie": "parlent plus fort que les mots",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Travail",
  "1ere partie": "L'oisiveté",
  "2eme partie": "est la mère de tous les vices",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Travail",
  "1ere partie": "Le travail",
  "2eme partie": "paie toujours",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Travail",
  "1ere partie": "Qui dort",
  "2eme partie": "dîne",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Travail",
  "1ere partie": "Les cordonniers",
  "2eme partie": "sont toujours les plus mal chaussés",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "-")
},

{
  "catégorie": "Travail",
  "1ere partie": "Qui cherche",
  "2eme partie": "trouve",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Travail",
  "1ere partie": "Le travail",
  "2eme partie": "éloigne de nous trois grands maux",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Travail",
  "1ere partie": "Les petites ruisseaux",
  "2eme partie": "font les grandes rivières",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "Le temps",
  "2eme partie": "guérit toutes les blessures",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "Qui va lentement",
  "2eme partie": "va sûrement",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "Le temps",
  "2eme partie": "c'est de l'argent",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "Chaque chose",
  "2eme partie": "vient à point à qui sait attendre",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "Les jours",
  "2eme partie": "se suivent et ne se ressemblent pas",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Temps",
  "1ere partie": "L'avenir",
  "2eme partie": "appartient à ceux qui se lèvent tôt",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Amitié",
  "1ere partie": "Les bons comptes",
  "2eme partie": "font les bons amis",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Amitié",
  "1ere partie": "Les vrais amis",
  "2eme partie": "se révèlent dans le besoin",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Amitié",
  "1ere partie": "Qui se ressemble",
  "2eme partie": "s'assemble",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Amitié",
  "1ere partie": "L'amour",
  "2eme partie": "rend aveugle",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Amitié",
  "1ere partie": "Les paroles",
  "2eme partie": "s'envolent mais les écrits restent",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "féminin", "+")
},

{
  "catégorie": "Amitié",
  "1ere partie": "Qui aime bien",
  "2eme partie": "châtie bien",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Vérité",
  "1ere partie": "La vérité",
  "2eme partie": "sort de la bouche des enfants",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Vérité",
  "1ere partie": "Les murs",
  "2eme partie": "ont des oreilles",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "masculin", "-")
},

{
  "catégorie": "Vérité",
  "1ere partie": "Qui ne dit mot",
  "2eme partie": "consent",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Vérité",
  "1ere partie": "Un homme averti",
  "2eme partie": "en vaut deux",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Vérité",
  "1ere partie": "Le mensonge",
  "2eme partie": "a des jambes courtes",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Argent",
  "1ere partie": "L'argent",
  "2eme partie": "ne fait pas le bonheur",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Argent",
  "1ere partie": "L'argent",
  "2eme partie": "est un bon serviteur mais un mauvais maître",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Argent",
  "1ere partie": "Qui paie ses dettes",
  "2eme partie": "s'enrichit",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Argent",
  "1ere partie": "Bien mal acquis",
  "2eme partie": "ne profite jamais",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Argent",
  "1ere partie": "L'avarice",
  "2eme partie": "rompt le sac",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Danger",
  "1ere partie": "Un chien qui aboie",
  "2eme partie": "ne mord pas",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Danger",
  "1ere partie": "Chat échaudé",
  "2eme partie": "craint l'eau froide",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Danger",
  "1ere partie": "La peur",
  "2eme partie": "donne des ailes",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Danger",
  "1ere partie": "Qui joue avec le feu",
  "2eme partie": "se brûle",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Danger",
  "1ere partie": "Qui s'y frotte",
  "2eme partie": "s'y pique",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Apparence",
  "1ere partie": "L'habit",
  "2eme partie": "ne fait pas le moine",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Apparence",
  "1ere partie": "Tout ce qui brille",
  "2eme partie": "n'est pas de l'or",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Apparence",
  "1ere partie": "Les apparences",
  "2eme partie": "sont souvent trompeuses",
  "type de phrase": "phrase simple",
  "caractéristiques": ("pluriel", "féminin", "-")
},

{
  "catégorie": "Apparence",
  "1ere partie": "La beauté",
  "2eme partie": "est dans l'œil de celui qui regarde",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Apparence",
  "1ere partie": "Qui se fie aux apparences",
  "2eme partie": "se trompe souvent",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "La raison du plus fort",
  "2eme partie": "est toujours la meilleure",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Goutte à goutte",
  "2eme partie": "l'eau creuse la pierre",
  "type de phrase": "phrase simple",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Sagesse",
  "1ere partie": "Qui veut tout",
  "2eme partie": "perd tout",
  "type de phrase": "subordonnée relative",
  "caractéristiques": ("singulier", "neutre", "-")
}
]

pvb_smpl = [
{
  "catégorie": "Sagesse",
  "proverbe": "On ne peut pas avoir le beurre et l'argent du beurre.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Sagesse",
  "proverbe": "On récolte ce que l'on sème.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Sagesse",
  "proverbe": "On apprend à tout âge.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Sagesse",
  "proverbe": "Il faut battre le fer quand il est chaud.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Sagesse",
  "proverbe": "Il faut rendre à César ce qui est à César.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Sagesse",
  "proverbe": "Autre temps, autres mœurs.",
  "caractéristiques": ("pluriel", "elliptique", "+")
},

{
  "catégorie": "Sagesse",
  "proverbe": "Tel père, tel fils.",
  "caractéristiques": ("singulier", "elliptique", "+")
},

{
  "catégorie": "Travail.",
  "proverbe": "C'est en forgeant qu'on devient forgeron.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Travail",
  "proverbe": "Petit à petit, l'oiseau fait son nid.",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Travail",
  "proverbe": "On n'a rien sans rien.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Travail",
  "proverbe": "Il faut travailler pour vivre et non vivre pour travailler.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Travail",
  "proverbe": "À l'œuvre, on reconnaît l'artisan.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Travail",
  "proverbe": "Cent fois sur le métier remettez votre ouvrage.",
  "caractéristiques": ("pluriel", "impératif", "+")
},

{
  "catégorie": "Travail",
  "proverbe": "Vingt métiers, quatorze misères.",
  "caractéristiques": ("pluriel", "elliptique", "-")
},

{
  "catégorie": "Temps",
  "proverbe": "Après la pluie, le beau temps.",
  "caractéristiques": ("singulier", "elliptique", "+")
},

{
  "catégorie": "Temps",
  "proverbe": "Il faut laisser du temps au temps.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Temps",
  "proverbe": "On ne rattrape pas le temps perdu.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Temps",
  "proverbe": "Chassez le naturel, il revient au galop.",
  "caractéristiques": ("pluriel", "impératif", "-")
},

{
  "catégorie": "Temps",
  "proverbe": "Mieux vaut tard que jamais.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Temps",
  "proverbe": "Paris ne s'est pas fait en un jour.",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Amitié",
  "proverbe": "Loin des yeux, loin du cœur.",
  "caractéristiques": ("singulier", "elliptique", "-")
},

{
  "catégorie": "Amitié",
  "proverbe": "On connaît l'ami dans le besoin.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Amitié",
  "proverbe": "Autant d'hommes, autant d'avis.",
  "caractéristiques": ("pluriel", "elliptique", "+")
},

{
  "catégorie": "Amitié",
  "proverbe": "Il n'y a pas d'amour sans jalousie.",
  "caractéristiques": ("singulier", "impersonnel", "-")
},

{
  "catégorie": "Amitié",
  "proverbe": "Les bons comptes font les bons amis.",
  "caractéristiques": ("pluriel", "masculin", "+")
},

{
  "catégorie": "Amitié",
  "proverbe": "Pour bien connaître quelqu'un, il faut avoir mangé un sac de sel avec lui.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Vérité",
  "proverbe": "Toute vérité n'est pas bonne à dire.",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Vérité",
  "proverbe": "Il n'y a que la vérité qui blesse.",
  "caractéristiques": ("singulier", "impersonnel", "-")
},

{
  "catégorie": "Vérité",
  "proverbe": "On ne peut cacher le soleil avec la main.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Vérité",
  "proverbe": "Il n'y a pas de fumée sans feu.",
  "caractéristiques": ("singulier", "impersonnel", "-")
},

{
  "catégorie": "Vérité",
  "proverbe": "À menteur, menteur et demi.",
  "caractéristiques": ("singulier", "elliptique", "-")
},

{
  "catégorie": "Vérité",
  "proverbe": "Chose promise, chose due.",
  "caractéristiques": ("singulier", "elliptique", "+")
},

{
  "catégorie": "Argent",
  "proverbe": "L'argent ne pousse pas sur les arbres.",
  "caractéristiques": ("singulier", "masculin", "-")
},

{
  "catégorie": "Argent",
  "proverbe": "On ne prête qu'aux riches.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Argent",
  "proverbe": "Plaie d'argent n'est pas mortelle.",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Argent",
  "proverbe": "Abondance de biens ne nuit pas.",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Argent",
  "proverbe": "Il faut donner au pauvre pour recevoir du ciel.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Argent",
  "proverbe": "Mains froides, cœur chaud.",
  "caractéristiques": ("pluriel", "elliptique", "+")
},

{
  "catégorie": "Danger",
  "proverbe": "Prudence est mère de sûreté.",
  "caractéristiques": ("singulier", "féminin", "+")
},

{
  "catégorie": "Danger",
  "proverbe": "Il vaut mieux prévenir que guérir.",
  "caractéristiques": ("singulier", "impersonnel", "+")
},

{
  "catégorie": "Danger",
  "proverbe": "Au danger on connaît le courage.",
  "caractéristiques": ("singulier", "elliptique", "+")
},

{
  "catégorie": "Danger",
  "proverbe": "On ne réveille pas le chat qui dort.",
  "caractéristiques": ("singulier", "neutre", "-")
},

{
  "catégorie": "Danger",
  "proverbe": "Il ne faut pas vendre la peau de l'ours avant de l'avoir tué.",
  "caractéristiques": ("singulier", "impersonnel", "-")
},

{
  "catégorie": "Danger",
  "proverbe": "Quand le chat n'est pas là, les souris dansent.",
  "caractéristiques": ("pluriel", "féminin", "-")
},

{
  "catégorie": "Apparence",
  "proverbe": "Les apparences sont trompeuses.",
  "caractéristiques": ("pluriel", "féminin", "-")
},

{
  "catégorie": "Apparence",
  "proverbe": "Il ne faut pas se fier aux apparences.",
  "caractéristiques": ("singulier", "impersonnel", "-")
},

{
  "catégorie": "Apparence",
  "proverbe": "La belle cage ne nourrit pas l'oiseau.",
  "caractéristiques": ("singulier", "féminin", "-")
},

{
  "catégorie": "Apparence",
  "proverbe": "L'habit ne fait pas le moine, mais il y aide.",
  "caractéristiques": ("singulier", "masculin", "+")
},

{
  "catégorie": "Apparence",
  "proverbe": "On ne juge pas un livre à sa couverture.",
  "caractéristiques": ("singulier", "neutre", "+")
},

{
  "catégorie": "Apparence",
  "proverbe": "Chassez le naturel, il revient au galop.",
  "caractéristiques": ("singulier", "masculin", "-")
}
]

def verifier_caracteristiques(i_debut, i_fin, limite, pvb):
    pvb1 = pvb[i_debut]
    pvb2 = pvb[i_fin]
    candidats = [pvb.index(p) for p in pvb if ((pvb1["caractéristiques"] == p["caractéristiques"]) and (pvb.index(p) != i_debut))]
    if candidats == []:
      return -1
    else:
      i_fin = candidats[randint(0, len(candidats) - 1)]
    return i_fin

def verifier_type(i_debut, i_fin, limite, pvb_cmplx):
    pvb1 = pvb_cmplx[i_debut]
    pvb2 = pvb_cmplx[i_fin]
    i_fin = verifier_caracteristiques(i_debut, i_fin, limite, pvb_cmplx)
    while (pvb1["type de phrase"] == "phrase simple") and (pvb2["type de phrase"] == "subordonnée relative"):
        i_fin = randint(0, limite)
        i_fin = verifier_caracteristiques(i_debut, i_fin, limite, pvb_cmplx)
        pvb2 = pvb_cmplx[i_fin]
    return i_fin

def comparer(i_debut, limite, i_fin):
  if i_debut == i_fin:
    i_fin = randint(0, limite)
    i_fin = comparer(i_debut, i_fin)
  return i_fin

def generer_citation(citation, opt):
    if opt == 1:
        limite = len(pvb_smpl) - 1
        i_debut = randint(0, limite)
        i_fin = randint(0, limite)
        i_fin = comparer(i_debut, limite, i_fin)
        debut_citation = pvb_smpl[i_debut]["proverbe"]
        fin_citation = pvb_smpl[i_fin]["proverbe"]        
    else:
        limite = len(pvb_cmplx) - 1
        i_debut = randint(0, limite)
        i_fin = randint(0, limite)
        i_fin = verifier_type(i_debut, i_fin, limite, pvb_cmplx)
        if i_fin == -1:
          debut_citation, fin_citation = generer_citation(citation, 0)
          return None
        else:
          debut_citation = pvb_cmplx[i_debut]["1ere partie"]
          fin_citation = pvb_cmplx[i_fin]["2eme partie"]
    citation.config(text = f'" {debut_citation} {fin_citation} "')
    return debut_citation, fin_citation

mainloop()