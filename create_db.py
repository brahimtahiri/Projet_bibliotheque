import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

with open('schema.sql') as file:
    connection.executescript(file.read())

books = [
    (1, 'Le Seigneur des Anneaux', 'J.R.R. Tolkien', 1954, 'Fantasy', True, 10),
    (2, '1984', 'George Orwell', 1949, 'Dystopie', True, 8),
    (3, 'Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 'Fantasy', True, 15),
    (4, 'L\'Alchimiste', 'Paulo Coelho', 1988, 'Roman initiatique', True, 12),
    (5, 'Les Misérables', 'Victor Hugo', 1862, 'Classique', True, 5),
    (6, 'L\'Art de la guerre', 'Sun Tzu', -500, 'Philosophie', True, 7),
    (7, 'Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 'Conte', True, 20),
    (8, 'Don Quichotte', 'Miguel de Cervantes', 1605, 'Classique', True, 6),
    (9, 'La Peste', 'Albert Camus', 1947, 'Roman existentialiste', True, 9),
    (10, 'Fahrenheit 451', 'Ray Bradbury', 1953, 'Science-fiction', True, 11)
]

cursor.executemany('''INSERT INTO Livres (id_livre, titre, auteur, annee_publication, genre, disponible, quantite_stock)
           VALUES (?, ?, ?, ?, ?, ?, ?)''', books)

users = [
    (0, "Administrateur", "", "administrateur", "administrateur", "administrator"),
    (1, 'Martin', 'Claire', 'cmartin', "cmartin", 'librarian'),
    (2, 'Dupont', 'Jean', 'jdupont', "jdupont", 'member'),
]

cursor.executemany('''INSERT INTO Utilisateurs (id_utilisateur, nom, prenom, username, password, type_utilisateur)
                      VALUES (?, ?, ?, ?, ?, ?)''', users)


connection.commit()
connection.close()
