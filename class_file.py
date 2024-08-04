class ImmeubleClass:
    def __init__(self, property, id, date, rue, ville, zip, nom, prenom, email):
        self.property = property
        self.id = id
        self.date = date
        self.rue = rue
        self.ville = ville
        self.zip = zip
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __lt__(self, other):
        if self.id == other.id:
            return self.nom < other.nom
        return self.id < other.id
