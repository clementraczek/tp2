import csv

CSV_FILE = "data/movies.csv"



def get_movie_by_title(titre):
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["titre"].lower() == titre.lower():
                return row
    return None


def get_movies_by_genre(genre_recherche):
    films = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["genre"].lower() == genre_recherche.lower():
                films.append(row)
    return films


def get_movies_by_age_limit(max_age):
    films = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["age_limite"]) <= max_age:
                films.append(row)
    return films



def afficher_menu():
    print("1. Rechercher un film par titre")
    print("2. Lister les films par genre")
    print("3. Lister les films par limite d’âge")
    print("4. Quitter")



def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Entrez le titre du film : ")
            film = get_movie_by_title(titre)
            if film:
                print(f"\n Film trouvé : {film['titre']} ({film['annee_production']}) - Genre : {film['genre']} - Âge limite : {film['age_limite']}")
            else:
                print("\ Film non trouvé.")
        
        elif choix == "2":
            genre = input("Entrez le genre à rechercher : ")
            films = get_movies_by_genre(genre)
            if films:
                print(f"\Films du genre '{genre}' :")
                for f in films:
                    print(f"- {f['titre']} ({f['annee_production']}) - Âge limite : {f['age_limite']}")
            else:
                print("\ Aucun film trouvé pour ce genre.")

        elif choix == "3":
            try:
                age = int(input("Entrez la limite d’âge maximale : "))
                films = get_movies_by_age_limit(age)
                if films:
                    print(f"\ Films avec une limite d’âge ≤ {age} :")
                    for f in films:
                        print(f"- {f['titre']} ({f['annee_production']}) - Genre : {f['genre']}")
                else:
                    print("\Aucun film trouvé avec cette limite d’âge.")
            except ValueError:
                print("Merci de saisir un nombre valide.")

        elif choix == "4":
            print("\Au revoir !")
            break

        else:
            print("\Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
