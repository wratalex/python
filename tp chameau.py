from random import *

KM_VOYAGE = 300 # Distance à parcourir pour gagner .
KM_NORM_MIN = 10 # Distance min. à la vitesse normale .
KM_NORM_MAX = 15 # Distance max à la vitesse normale .
KM_RAP_MIN = 20 # Distance min. à toute vitesse .
KM_RAP_MAX = 25 # Distance max. à toute vitesse .
AVANTAGE_VOYAGEUR = 20 # L ' avantage initial du voyageur .
GOURDE_PLEINE = 12 # Le nombre de gorgées de la gourde .
MORT_SOIF = 4 # Nombre de tours pour mourir de soif .
MORT_FATIGUE = 4 # Nombre de tours pour mourir de fatigue .
DIF_AIDE = 3 # Difficulté pour trouver de l'aide .
AVANCE_NATIFS = 4 # Vitesse des natifs 

print("Vous avez volé un chameau pour traverser le grand désert.")
print("Les natifs veulent le récupérer.")
print("Votre objectif est de survivre à la traversée de 300 km sans être attrapé(e).")

km_voyageur = 0 # Distance t o t a l e parcourue .
km_natifs = km_voyageur - AVANTAGE_VOYAGEUR # Distance parcourue par les natifs .
gourde = GOURDE_PLEINE // 2 # Nombre de gorg és dans l a gourde .
soif = 0 # Niveau de soif du voyageur .
fatigue = 0 # Niveau de fatigue du chameau .
SPECIAL=10
event=0

opt=True
while opt:
    if event!=1:
        print('''OPTIONS:
        1. Boire
        2. Avancer normalement
        3. Avancer à toute vitesse
        4. Repos
        5. Espérer de l'aide
        T. Terminer la partie
        Qu'allez vous faire ?''')
        interaction=input()
        if interaction =='T':
            opt=False
        if interaction=='1' and gourde==0:
            print("La gourde est vide !")
        elif interaction=='1' and gourde!=0:
            soif=0
            gourde-=1
            print("Vous avez bu une gorgée")
        if interaction=='2':
            fatigue+=1
            avance=randint(KM_NORM_MIN,KM_NORM_MAX)
            km_voyageur+=avance
            print("Vous avez parcourus ",km_voyageur,"km")
        elif interaction=='3':
            fatigue+=2
            avancer_r=randint(KM_RAP_MIN,KM_RAP_MAX)
            km_voyageur+=avancer_r
            print("Vous avez parcourus ",km_voyageur,"km")
        if interaction=='4':
            fatigue=0
            print("Votre chameau s'est bien reposé")
        if interaction=='5':
            aide=randint(0,DIF_AIDE)
            if aide==0:
                print("Vous avez trouvé de l'aide.")
                if gourde >=GOURDE_PLEINE:
                    print("La gourde est déjà pleine !")
                elif gourde <=9:
                    gourde+=3
                    print("Quelques gorgées ont été ajoutées à votre gourde.")
                else:
                    gourde=12
                    print("Quelques gorgées ont été ajoutées à votre gourde.")
            else:
                print("Vous n'avez pas trouvé de l'aide.")

        if interaction not in {"1","2","3","4","5","T","t"}:
            print("Option invalide !")
        if km_voyageur>=KM_VOYAGE:
            print("Vous avez gagné !!")
            opt=False
        natif=randint(0,AVANCE_NATIFS)
        if natif==0:
            natifRAP=randint(KM_RAP_MIN,KM_RAP_MAX)
            km_natifs+=natifRAP
        elif natif==1:
            natifNORM=randint(KM_NORM_MIN,KM_NORM_MAX)
            km_natifs+=natifNORM
        if km_natifs>=km_voyageur:
            print("Vous avez été attrapé par les natifs !")
            opt=False
        else:
            print("Les natifs ont parcourus ",km_natifs," km")
        if interaction in {"2","3","4","5"}:
            soif+=1
        if soif==0:
            print("Vous n'avez pas soif.")
        elif soif==1:
            print("Vous avez un peu soif.")
        elif soif==2:
            print("Vous acez beaucoup soif !")
        elif soif==3:
            print("Vous aller mourir de  soif !!")
        if soif==MORT_SOIF:
            opt=False
            print("Vous êtes mort de soif.")
        else:
            print("Il vous reste ",gourde," gorgée(s) d'eau")
        if fatigue==0:
            print("Le chameau est en bonne forme.")
        elif fatigue==1:
            print("Le chameau est un peu fatigué.")
        elif fatigue==2:
            print("Le chameau est très fatigué !")
        elif fatigue==3:
            print("Le chameau va mourir de fatigue !!")
        if fatigue==MORT_FATIGUE:
            opt=False
            print("Le chameau est mort de fatigue, les natifs vont ont attrapé.")

    event=randint(0,SPECIAL)
    if event==0:
        print("Vous avez trouvé un oasis")
        gourde=GOURDE_PLEINE
    if event==1:
        print("Une tempête s'abat sur le désert")
        natif=randint(0,AVANCE_NATIFS)
        if natif==0:
            natifRAP=randint(KM_RAP_MIN,KM_RAP_MAX)
            km_natifs+=natifRAP
        elif natif==1:
            natifNORM=randint(KM_NORM_MIN,KM_NORM_MAX)
            km_natifs+=natifNORM
        if km_natifs>=km_voyageur:
            print("Vous avez été attrapé par les natifs !")
            opt=False
        else:
            print("Les natifs ont parcourus ",km_natifs," km")

    if opt==False:
        print("Voulez-vous jouer une nouvelle partie ?")
        Nparty=input()
        if Nparty in {"oui","o","y","yes"}:
            opt=True
            km_voyageur = 0 
            km_natifs = km_voyageur - AVANTAGE_VOYAGEUR 
            gourde = GOURDE_PLEINE // 2 
            soif = 0 
            fatigue = 0