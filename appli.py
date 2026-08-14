from tkinter import *
from random import *

# Couleur par défaut
blanc = "#dddddd"
noir = "#333333"
bleu = "#0099ff"

# Fonctions de design
def changer_sombre():
  main.config(bg = noir)
  theme.config(bg = noir)
  instruction.config(bg = noir, fg = blanc)
  combinaison.config(bg = noir, fg = blanc)
  citation.config(bg = noir, fg = "orange")
  bienvenue.config(bg = noir)
  cadre.config(bg = noir)

def changer_clair():
  main.config(bg = blanc)
  theme.config(bg = blanc)
  instruction.config(bg = blanc, fg = "black")
  combinaison.config(bg = blanc, fg = "black")
  citation.config(bg = blanc, fg = "green")
  bienvenue.config(bg = blanc)
  cadre.config(bg = blanc)

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
main.option_add("*Font", "Arial 15")
#*********************************************


bienvenue = Label(main, text = "Bienvenue sur le générateur de citations !", font = ("Arial", 25), fg = "#0077ff")
bienvenue.pack(ipadx = 10, ipady = 10)


# Theme de l'application
theme = Label(main, text = "Thème de l'application", fg = "#777777")
theme.pack()

cadre = Frame(main)
cadre.pack()

clair = Button(cadre, text = "Clair", command = changer_clair)
clair.pack(side = "left", padx = 5, pady = 5)

sombre = Button(cadre, text = "Sombre", command = changer_sombre)
sombre.pack(padx = 5, pady = 5)
#*********************************************


# Fonctions principales
instruction = Label(main, text = "Appuyer sur le bouton pour générer une citation inédite !")
instruction.pack()

generer1 = Button(main, text = "Générer un proverbe court", command = lambda: generer_citation(citation, 0))
generer1.pack(padx = 10, pady = 10)

generer2 = Button(main, text = "Générer un proverbe long", command = lambda: generer_citation(citation, 1))
generer2.pack(padx = 10, pady = 10)

citation = Label(main, text = '~~~~""~~~~', font = ("Imperial Script", 25, "bold"), fg = "green")
citation.pack()

combinaison = Label(main, text = "Vous verrez ici quels proverbes on été combinés")
combinaison.pack()
#*********************************************


# Proverbes
sagesse = [
  [
    {
      "1ere partie": "L'erreur",
      "2eme partie": "est humaine",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "La patience",
      "2eme partie": "est amère, mais son fruit est doux",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "La nuit",
      "2eme partie": "porte conseil",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "L'expérience",
      "2eme partie": "est la mère de la sagesse",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "La vérité",
      "2eme partie": "sort de la bouche des enfants",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "Celui qui sait",
      "2eme partie": "ne parle pas",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui veut voyager loin",
      "2eme partie": "ménage sa monture",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ],
  [
    {
      "proverbe": "Chassez le naturel, il revient au galop",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Il faut tourner sept fois sa langue dans sa bouche avant de parler",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "Loin des yeux, loin du cœur",
      "caractéristiques": ('singulier', 'invariable', '-')
    },
    {
      "proverbe": "Petit à petit, l'oiseau fait son nid",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Prudence est mère de sûreté",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Rira bien qui rira le dernier",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ]
]

travail = [
  [
    {
      "1ere partie": "L'oisiveté",
      "2eme partie": "est la mère de tous les vices",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '-')
    },
    {
      "1ere partie": "Les bons comptes",
      "2eme partie": "font les bons amis",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "1ere partie": "Le travail",
      "2eme partie": "anoblit l'homme",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "L'effort",
      "2eme partie": "récompense toujours la persévérance",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui ne risque rien",
      "2eme partie": "n'a rien",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Qui cherche",
      "2eme partie": "trouve",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ],
  [
    {
      "proverbe": "C'est au pied du mur qu'on voit le maçon",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Cent fois sur le métier remettez votre ouvrage",
      "caractéristiques": ('pluriel', 'invariable', '+')
    },
    {
      "proverbe": "Il faut battre le fer tant qu'il est chaud",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "Chaque chose en son temps",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "Pierre qui roule n'amasse pas mousse",
      "caractéristiques": ('singulier', 'féminin', '-')
    },
    {
      "proverbe": "Paris ne s'est pas fait en un jour",
      "caractéristiques": ('singulier', 'masculin', '-')
    }
  ]
]

temps = [
  [
    {
      "1ere partie": "Le temps",
      "2eme partie": "est un grand maître",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Le temps",
      "2eme partie": "guérit toutes les blessures",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "L'avenir",
      "2eme partie": "appartient à ceux qui se lève tôt",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Les jours",
      "2eme partie": "se suivent et ne se ressemblent pas",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '-')
    },
    {
      "1ere partie": "Qui prend son temps",
      "2eme partie": "arrive à temps",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ],
  [
    {
      "proverbe": "Autre temps, autres mœurs",
      "caractéristiques": ('pluriel', 'invariable', '-')
    },
    {
      "proverbe": "Il faut donner du temps au temps",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "Chaque jour suffit sa peine",
      "caractéristiques": ('singulier', 'féminin', '-')
    },
    {
      "proverbe": "Demain est un autre jour",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "On ne peut pas être et avoir été",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Après la pluie, le beau temps",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "L'oisiveté perd le temps",
      "caractéristiques": ('singulier', 'féminin', '-')
    }
  ]
]

amour = [
  [
    {
      "1ere partie": "L'amour",
      "2eme partie": "est aveugle",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Le cœur",
      "2eme partie": "a ses raisons que la raison ne connaît point",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "L'amour",
      "2eme partie": "triomphe de tout",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Les absents",
      "2eme partie": "ont toujours tort",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '-')
    },
    {
      "1ere partie": "Qui aime bien",
      "2eme partie": "châtie bien",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui s'y frotte",
      "2eme partie": "s'y pique",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '-')
    }
  ],
  [
    {
      "proverbe": "Loin des yeux, près du cœur",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "Abondance de biens ne nuit pas",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "On ne badine pas avec l'amour",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Il vaut mieux être seul que mal accompagné",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "L'amour fait passer le temps, le temps fait passer l'amour",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Un de perdu, dix de retrouvés",
      "caractéristiques": ('pluriel', 'masculin', '+')
    }
  ]
]

amitie = [
  [
    {
      "1ere partie": "Un ami",
      "2eme partie": "se connaît dans le besoin",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Les vrais amis",
      "2eme partie": "sont rares comme les diamants",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "1ere partie": "L'amitié",
      "2eme partie": "est une âme en deux corps",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "1ere partie": "Les amis de nos amis",
      "2eme partie": "sont nos amis",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "1ere partie": "Qui trouve un ami",
      "2eme partie": "trouve un trésor",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ],
  [
    {
      "proverbe": "Dis-moi qui tu fréquentes, je te dirai qui tu es",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Mieux vaut un bon voisin qu'un distant parent",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Au besoin on connaît l'ami",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Les petits cadeaux entretiennent l'amitié",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "proverbe": "On ne choisit pas sa famille, mais on choisit ses amis",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Entre amis, tout est commun",
      "caractéristiques": ('pluriel', 'invariable', '+')
    },
    {
      "proverbe": "Un ami fidèle est un refuge puissant",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ]
]

argent = [
  [
    {
      "1ere partie": "L'argent",
      "2eme partie": "ne fait pas le bonheur",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "L'argent",
      "2eme partie": "est un bon serviteur mais un mauvais maître",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Les affaires",
      "2eme partie": "sont les affaires",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'féminin', '-')
    },
    {
      "1ere partie": "Avare",
      "2eme partie": "amasse pour les autres",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Qui paie ses dettes",
      "2eme partie": "s'enrichit",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui donne aux pauvres",
      "2eme partie": "prête à Dieu",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    }
  ],
  [
    {
      "proverbe": "Plaie d'argent n'est pas mortelle",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Le temps, c'est de l'argent",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Bien mal acquis ne profite jamais",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Il n'y a pas de petit profit",
      "caractéristiques": ('singulier', 'invariable', '+')
    },
    {
      "proverbe": "L'argent n'a pas d'odeur",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Rien n'est gratuit en ce bas monde",
      "caractéristiques": ('singulier', 'masculin', '-')
    }
  ]
]

verite = [
  [
    {
      "1ere partie": "Le mensonge",
      "2eme partie": "a les jambes courtes",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Toute vérité",
      "2eme partie": "n'est pas bonne à dire",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '-')
    },
    {
      "1ere partie": "Les paroles",
      "2eme partie": "s'envolent, les écrits restent",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'féminin', '+')
    },
    {
      "1ere partie": "Un homme averti",
      "2eme partie": "en vaut deux",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui ne dit mot",
      "2eme partie": "consent",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui sème le vent",
      "2eme partie": "récolte la tempête",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '-')
    }
  ],
  [
    {
      "proverbe": "Il n'y a que la vérité qui blesse",
      "caractéristiques": ('singulier', 'invariable', '-')
    },
    {
      "proverbe": "Mieux vaut une vérité qui blesse qu'un mensonge qui séduit",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Chacun voit midi à sa porte",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "proverbe": "Promesse faite est dette due",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Il ne faut pas dire : Fontaine, je ne boirai pas de ton eau",
      "caractéristiques": ('singulier', 'invariable', '-')
    },
    {
      "proverbe": "Au royaume des aveugles, les unijambistes sont rois",
      "caractéristiques": ('pluriel', 'masculin', '+')
    }
  ]
]

nature = [
  [
    {
      "1ere partie": "Chien qui aboie",
      "2eme partie": "ne mord pas",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Une hirondelle",
      "2eme partie": "ne fait pas le printemps",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'féminin', '-')
    },
    {
      "1ere partie": "Les chats",
      "2eme partie": "ne font pas des chiens",
      "type de phrase": "phrase simple",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "1ere partie": "L'arbre",
      "2eme partie": "cache souvent la forêt",
      "type de phrase": "phrase simple",
      "caractéristiques": ('singulier', 'masculin', '-')
    },
    {
      "1ere partie": "Qui dort",
      "2eme partie": "dîne",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "1ere partie": "Qui vole un œuf",
      "2eme partie": "vole un bœuf",
      "type de phrase": "subordonnée relative",
      "caractéristiques": ('singulier', 'masculin', '-')
    }
  ],
  [
    {
      "proverbe": "Quand le chat n'est pas là, les souris dansent",
      "caractéristiques": ('pluriel', 'féminin', '+')
    },
    {
      "proverbe": "Il ne faut pas vendre la peau de l'ours avant de l'avoir tué",
      "caractéristiques": ('singulier', 'invariable', '-')
    },
    {
      "proverbe": "La nuit, tous les chats sont gris",
      "caractéristiques": ('pluriel', 'masculin', '+')
    },
    {
      "proverbe": "Il ne faut pas mettre tous ses œufs dans le même panier",
      "caractéristiques": ('singulier', 'invariable', '-')
    },
    {
      "proverbe": "À cheval donné, on ne regarde pas les dents",
      "caractéristiques": ('singulier', 'masculin', '+')
    },
    {
      "proverbe": "Goutte à goutte, l'eau creuse la pierre",
      "caractéristiques": ('singulier', 'féminin', '+')
    },
    {
      "proverbe": "Aux innocents les mains pleines",
      "caractéristiques": ('pluriel', 'masculin', '+')
    }
  ]
]

pvb_cmplx = [sagesse[0], travail[0], temps[0], amour[0], amitie[0], argent[0], verite[0], nature[0]]
pvb_smpl = [sagesse[1], travail[1], temps[1], amour[1], amitie[1], argent[1], verite[1], nature[1]]

def verifier_caracteristiques1(i_debut, i_fin, limite, cate):
    pvb1 = cate[i_debut]
    pvb2 = cate[i_fin]

    # Si le proverbes de départ est une phrase simple, le deuxième proverbe doit aussi l'être
    # Sinon, on passe directement à la recherche d'un proverbe ayant les mêmes caractéristiques grammaticales et sémantique à part lui-même
    if pvb1["caractéristiques"] == "phrase simple":
      candidats = [cate.index(p) for p in cate if ((pvb1["caractéristiques"] == p["caractéristiques"]) and (cate.index(p) != i_debut) and (pvb1["type de phrase"] == "phrase simple") and (p["type de phrase"] != "subordonnée relative"))]
      if candidats == []:
        return -1
      else:
        i_fin = candidats[randint(0, len(candidats) - 1)]
    else:
      candidats = [cate.index(p) for p in cate if ((pvb1["caractéristiques"] == p["caractéristiques"]) and (cate.index(p) != i_debut))]
      if candidats == []:
        return -1
      else:
        i_fin = candidats[randint(0, len(candidats) - 1)]
    return i_fin

def verifier_caracteristiques2(i_debut, i_fin, cate):
  pvb1 = cate[i_debut]
  pvb2 = cate[i_fin]

  # A la recherche d'un proverbe ayant les mêmes caractéristiques grammaticales autre que le proverbe  de départ
  # Si ils ont le même sens, le connecteur qui les séparera sera ".", sinon on utilisera des connecteurs d'opposition
  connecteur = (" mais", " sauf que", " toutefois")
  candidats = [cate.index(p) for p in cate if ((pvb1["caractéristiques"][0:2] == p["caractéristiques"][0:2]) and (cate.index(p) != i_debut))]
  if candidats == []:
      print("Pas de valeur similaire")
      return -1
  else:
      i_fin = candidats[randint(0, len(candidats) - 1)]
      pvb2 = cate[i_fin]
  if pvb1["caractéristiques"][2] != pvb2["caractéristiques"][2]:
    i_dernier_connecteur = len(connecteur) - 1
    mot = connecteur[randint(0, i_dernier_connecteur)]
  else:
    mot = '.'
  return i_fin, mot


# Fonction proncipale
def generer_citation(citation, opt):
    if opt == 1:

        # Ici, in génère des proverbe court
        i_dernier_cate = len(pvb_smpl) - 1
        cate = pvb_smpl[randint(0, i_dernier_cate)]
        limite = len(cate) - 1
        i_debut = randint(0, limite)
        i_fin = randint(0, limite)
        i_fin, connecteur = verifier_caracteristiques2(i_debut, i_fin, cate)

        # Si il n'y a pas de proverbes qui peut être mélangé avec celui de départ, on regénère un nouveau
        if i_fin == -1:
          debut_citation, fin_citation = generer_citation(citation, 1)
          return None
        debut_citation = cate[i_debut]["proverbe"] + connecteur
        fin_citation = cate[i_fin]["proverbe"]
        pvb1 = debut_citation
        pvb2 = fin_citation
                
    else:

        # Ici, in génère des proverbe court
        i_dernier_cate = len(pvb_cmplx) - 1
        cate = pvb_cmplx[randint(0, i_dernier_cate)]
        limite = len(cate) - 1
        i_debut = randint(0, limite)
        i_fin = randint(0, limite)
        i_fin = verifier_caracteristiques1(i_debut, i_fin, limite, cate)

        # Si il n'y a pas de proverbes qui peut être mélangé avec celui générer de base, on regénère un nouveau
        if i_fin == -1: 
          debut_citation, fin_citation = generer_citation(citation, 0)
          return None
        pvb1 = cate[i_debut]["1ere partie"] + " " + cate[i_debut]["2eme partie"]
        pvb2 = cate[i_fin]["1ere partie"] + " " + cate[i_fin]["2eme partie"]
        debut_citation = cate[i_debut]["1ere partie"]
        fin_citation = cate[i_fin]["2eme partie"]
    
    # Màj des étiquettes
    citation.config(text = f'~~~~ " {debut_citation} {fin_citation} " ~~~~')
    combinaison.config(text = f""" Cette citation a été obtenu en combinant  "{pvb1}" \n et  "{pvb2}" """)
    return debut_citation, fin_citation

mainloop()