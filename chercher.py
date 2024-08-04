def recherche_property(immeuble_list) :
    val = input("saisissez la property souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.property.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_id(immeuble_list) :
    val = input("saisissez l'id souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.id.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_date(immeuble_list) :
    val = input("saisissez la date souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.date.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_rue(immeuble_list) :
    val = input("saisissez la rue souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.rue.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_ville(immeuble_list) :
    val = input("saisissez la ville souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.ville.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    

def recherche_zip(immeuble_list) :
    val = input("saisissez la zip souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.zip.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_nom(immeuble_list) :
    val = input("saisissez la nom souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.nom.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_prenom(immeuble_list) :
    val = input("saisissez la prenom souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.prenom.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    
def recherche_id(immeuble_list) :
    val = input("saisissez la id souhaité\n")
    immeuble_list_recherche = (x for x in immeuble_list if val.lower() == x.id.lower())
    for immeuble in immeuble_list_recherche :
        print(immeuble.property, immeuble.id, immeuble.date, immeuble.rue, immeuble.ville, immeuble.zip, immeuble.nom, immeuble.prenom, immeuble.email, sep=', ')
    print("\n")
    return
    

def chercher(immeuble_list) :
    print("sur quelle colone voulez vous faire votre recherche ?")
    val = input("1: property,  2: id, 3: date, 4: rue, 5: ville, 6: zip; 7: nom, 8: prenom, 9: email\n")

    if (val == "1" or val == "property") :
        recherche_property(immeuble_list)
    if (val == "2" or val == "id") :
        recherche_id(immeuble_list)
    if (val == "3" or val == "date") :
        recherche_date(immeuble_list)
    if (val == "4" or val == "rue") :
        recherche_rue(immeuble_list)
    if (val == "5" or val == "ville") :
        recherche_ville(immeuble_list)
    if (val == "6" or val == "zip") :
        recherche_zip(immeuble_list)
    if (val == "7" or val == "nom") :
        recherche_nom(immeuble_list)
    if (val == "8" or val == "prenom") :
        recherche_prenom(immeuble_list)
    if (val == "9" or val == "email") :
        recherche_email(immeuble_list)
    return
