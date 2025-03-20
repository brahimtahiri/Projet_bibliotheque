from flask import Flask, render_template, redirect, url_for, request
import sqlite3, bcrypt, datetime

app = Flask(__name__)

app.secret_key = b'5&y9L$zYq2WkT9*8aFhB^8zM#t3S@e9q'

connexion = sqlite3.connect("database.db", check_same_thread = False)
cursor = connexion.cursor()

@app.route('/', methods = ['GET'])
def index():
    return render_template("/index.html")

@app.route('/login', methods = ['POST'])
def login():
    return redirect(url_for('books'))

@app.route('/users', methods = ['GET'])
def users():
    cursor.execute("SELECT id_utilisateur, nom, prenom, username, type_utilisateur FROM Utilisateurs;")
    users = cursor.fetchall()

    return render_template("/users/users.html", utilisateurs=users)

@app.route('/register_user', methods = ['GET', 'POST'])
def register_user():
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        username = request.form['username']
        password =  bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        type_utilisateur = request.form['type_utilisateur']

        cursor.execute('''INSERT INTO Utilisateurs (nom, prenom, username, password, type_utilisateur)
                      VALUES (?, ?, ?, ?, ?)''', (nom, prenom, username, password, type_utilisateur))
        connexion.commit()

        return redirect(url_for('users'))

    return render_template('/users/user_form.html')


@app.route('/delete_user/<int:id>', methods = ['GET'])
def delete_user(id):
    cursor.execute("DELETE FROM Utilisateurs WHERE id_utilisateur = ?", (id,))
    connexion.commit()

    print("L'utilisateur %d a été supprimé !" %id)

    return redirect(url_for('users'))

@app.route('/books', methods = ['GET'])
def books():
    cursor.execute("SELECT id_livre, titre, auteur, annee_publication, genre, disponible, quantite_stock FROM Livres;")
    books = cursor.fetchall()

    return render_template("/books/books.html", livres=books)

@app.route('/register_book', methods = ['GET', 'POST'])
def register_book():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee_publication = request.form['annee_publication']
        genre = request.form['genre']
        disponible = True
        quantite_stock = request.form['quantite_stock']

        cursor.execute('''INSERT INTO Livres (titre, auteur, annee_publication, genre, disponible, quantite_stock)
                   VALUES (?, ?, ?, ?, ?, ?)''', (titre, auteur, annee_publication, genre, disponible, quantite_stock))
        connexion.commit()

        return redirect(url_for('books'))

    return render_template('/books/book_form.html', current_year = datetime.datetime.now().year)

@app.route('/search_book')

@app.route('/delete_book/<int:id>', methods = ['GET'])
def delete_book(id):
    cursor.execute("DELETE FROM Livres WHERE id_livre = ?", (id,))
    connexion.commit()

    print("Le livre %d a été supprimé !" %id)

    return redirect(url_for('books'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html'), 404 

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 80 , debug = True)
