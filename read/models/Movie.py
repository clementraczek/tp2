class Movie:

    _id_counter = 31  

    def __init__(self, titre: str, annee_production: int, genre: str, age_limite: int):
        self.id = Movie._id_counter
        Movie._id_counter += 1

        # Attributs d'instance
        self.titre = titre
        self.annee_production = annee_production
        self.genre = genre
        self.age_limite = age_limite

    def __str__(self):

        return (f"{self.titre} ({self.annee_production})\n"
                f"   Genre : {self.genre}\n"
                f"   Âge minimum : {self.age_limite} ans\n"
                f"   ID : {self.id}")
