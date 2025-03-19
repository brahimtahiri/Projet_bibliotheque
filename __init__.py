from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

app.secret_key = b'5&y9L$zYq2WkT9*8aFhB^8zM#t3S@e9q'

connexion = sqlite3.connect("database.db", check_same_thread=False)
cursor = connexion.cursor()

@app.route('/', methods=['GET'])
def index():
    return render_template("/index.html")

@app.route('/login')
def login():
    return render_template("/index.html")

@app.route('/livres', methods=['GET'])
def livres():
    id = request.args.get('id_livre')
    
    cursor.execute("SELECT id_livre, titre, auteur, annee_publication, genre, disponible, quantite_stock FROM Livres;")
    livres = cursor.fetchall()

    print(livres)

    return render_template("/livres.html", livres=livres)

@app.route('/register_livre',methods=['GET', 'POST'])
def register_livre():
    if request.method == 'POST':
        titre = request.form['titre']
        auteur = request.form['auteur']
        annee_publication = request.form['annee_publication']
        genre = request.form['genre']
        disponible = True
        quantite_stock = request.form['quantite_stock']

        query = '''INSERT INTO Livres (titre, auteur, annee_publication, genre, disponible, quantite_stock)
                   VALUES (?, ?, ?, ?, ?, ?)'''
        cursor.execute(query, (titre, auteur, annee_publication, genre, disponible, quantite_stock))
        connexion.commit()

        return redirect(url_for('livres'))

    return render_template('form_livre.html')

@app.route('/delete_livre/<int:id>', methods=['GET'])
def delete_livre(id):
    cursor.execute("DELETE FROM Livres WHERE id_livre = ?", (id,))
    connexion.commit()

    print("Le livre %d a été supprimé !" %id)

    return redirect(url_for('livres'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

if __name__ == '__main__':
    app.run(debug = True)
