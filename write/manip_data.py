import os
import csv
from models.Movie import Movies
from exceptions.InvalidTitleException import InvalidTitleException
from exceptions.InvalidAgeLimitException import InvalidAgeLimitException
from exceptions.InvalidGenreException import InvalidGenreException
from exceptions.InvalidYearException import InvalidYearException

CSV_FILE = "data/movies.csv"

def get_next_id():
    """Retourne le prochain ID disponible dans le CSV."""
    ids = []

    if not os.path.exists(CSV_FILE):
        return 31  # commencer à 31 si fichier inexistant

    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)  # sauter le header
        for row in reader:
            if not row:  # ligne vide
                continue
            first_col = row[0].strip()
            if first_col.isdigit():  # ignorer le header ou les valeurs non numériques
                ids.append(int(first_col))

    return max(ids, default=30) + 1

def add_movie():
    try:
        titre = input("Titre: ").strip()
        if not titre:
            raise InvalidTitleException("Titre vide")

        annee_input = input("Année: ").strip()
        if not annee_input.isdigit():
            raise InvalidYearException("Année invalide")
        annee = int(annee_input)

        genre = input("Genre: ").strip()
        if not genre:
            raise InvalidGenreException("Genre vide")

        age_input = input("Age limite: ").strip()
        if not age_input.isdigit():
            raise InvalidAgeLimitException("Age limite invalide")
        age = int(age_input)

        movie = Movies(titre, annee, genre, age)
        movie.id = get_next_id()

        write_header = not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0

        with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(["id", "titre", "annee_production", "genre", "age_limite"])
            writer.writerow([movie.id, movie.titre, movie.annee_production, movie.genre, movie.age_limite])

        print("Film ajouté:", movie)

    except Exception as e:
        print("Erreur:", e)

def modify_movie():
    try:
        movie_id_input = input("ID du film à modifier: ").strip()
        if not movie_id_input.isdigit():
            print("ID invalide.")
            return
        movie_id = int(movie_id_input)

        movies = []
        header = None
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # sauter le header
            for row in reader:
                if not row or not row[0].strip().isdigit():
                    continue
                movies.append(row)

        found = False
        for i, row in enumerate(movies):
            if int(row[0].strip()) == movie_id:
                found = True
                print(f"Film trouvé: {row}")

                titre = input("Nouveau titre: ").strip()
                if not titre:
                    raise InvalidTitleException("Titre vide")

                annee_input = input("Nouvelle année: ").strip()
                if not annee_input.isdigit():
                    raise InvalidYearException("Année invalide")
                annee = int(annee_input)

                genre = input("Nouveau genre: ").strip()
                if not genre:
                    raise InvalidGenreException("Genre vide")

                age_input = input("Nouvelle limite d'âge: ").strip()
                if not age_input.isdigit():
                    raise InvalidAgeLimitException("Age limite invalide")
                age = int(age_input)

                movies[i] = [str(movie_id), titre, str(annee), genre, str(age)]
                break

        if not found:
            print("Film non trouvé.")
            return

        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(header)
            writer.writerows(movies)

        print("Film modifié avec succès.")

    except Exception as e:
        print("Erreur:", e)

def delete_movie():
    try:
        movie_id_input = input("ID du film à supprimer: ").strip()
        if not movie_id_input.isdigit():
            print("ID invalide.")
            return
        movie_id = int(movie_id_input)

        movies = []
        header = None
        with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # sauter le header
            for row in reader:
                if not row or not row[0].strip().isdigit():
                    continue
                movies.append(row)

        new_movies = [row for row in movies if int(row[0].strip()) != movie_id]

        if len(new_movies) == len(movies):
            print("Film non trouvé.")
            return

        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if header:
                writer.writerow(header)
            writer.writerows(new_movies)

        print("Film supprimé avec succès.")

    except Exception as e:
        print("Erreur:", e)

def menu():
    while True:
        print("\n===== Gestion des Films =====")
        print("1. Ajouter un film")
        print("2. Modifier un film")
        print("3. Supprimer un film")
        print("4. Quitter")
        
        choice = input("Choisissez une option (1-4): ").strip()
        
        if choice == "1":
            add_movie()
        elif choice == "2":
            modify_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    menu()
