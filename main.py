#/// https://github.com/guifresp/Recommandation-Livres-Projet-L1-EFREI- ///

def user_profile():
    profile_1 = {}
    profile_2 = []

    #demander pseudo

    profile_1["pseudonyme"] = str(input("PSEUDONYME : "))

    # pour donner le choix entre homme et femme

    g = input("Votre genre : \n""1:Homme \n""2:Femme\n")
    if g == 1:
        profile_1["genre"] = str("Homme")
        profile_2.append(1)
    elif g == 2:
        profile_1["genre"] = str("Femme")
        profile_2.append(2)
    else:
        profile_1["genre"] = str("Peu importe")
        profile_2.append(3)

    # demander l age :

    g = input("votre age")

    while g.isnumeric() == False:
        g = input("votre age re")

    profile_1["age"] = g






    profile_1["style"] = str(input("votre style de lecture : "))


    style = input("Style de lecture \n1. Science-fiction \n2. Biographie\n3. Horreur\n4. Romance\n5. Fable\n6. Histoire\n7. Comédie")




