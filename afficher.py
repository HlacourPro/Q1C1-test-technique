def afficher(immeuble_list) :
    for immeuble in immeuble_list :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print ("\n")
    return
