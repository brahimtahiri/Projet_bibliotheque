-- Table Livres
CREATE TABLE IF NOT EXISTS Livres (
    id_livre INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER NOT NULL,
    genre TEXT,
    disponible BOOLEAN DEFAULT 1,  -- 1 pour TRUE, 0 pour FALSE
    quantite_stock INTEGER NOT NULL
);

-- Table Utilisateurs
CREATE TABLE IF NOT EXISTS Utilisateurs (
    id_utilisateur INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    type_utilisateur TEXT CHECK(type_utilisateur IN ('administrator', 'librarian', 'member')) NOT NULL
);

-- Table Emprunts
CREATE TABLE IF NOT EXISTS Emprunts (
    id_emprunt INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utilisateur INTEGER,
    id_livre INTEGER,
    date_emprunt DATE NOT NULL,
    date_retour_prevu DATE NOT NULL,
    date_retour_effectif DATE,
    etat_emprunt TEXT CHECK(etat_emprunt IN ('ongoing', 'returned', 'overdue')) DEFAULT 'ongoing',
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES Livres(id_livre) ON DELETE CASCADE
);

-- Table Stocks
CREATE TABLE IF NOT EXISTS Stocks (
    id_stock INTEGER PRIMARY KEY AUTOINCREMENT,
    id_livre INTEGER,
    quantite_disponible INTEGER NOT NULL,
    FOREIGN KEY (id_livre) REFERENCES Livres(id_livre) ON DELETE CASCADE
);

-- Table Historique_Emprunts
CREATE TABLE IF NOT EXISTS Historique_Emprunts (
    id_historique INTEGER PRIMARY KEY AUTOINCREMENT,
    id_utilisateur INTEGER,
    id_livre INTEGER,
    date_emprunt DATE NOT NULL,
    date_retour DATE NOT NULL,
    statut TEXT CHECK(statut IN ('emprunté', 'retourné')) NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES Utilisateurs(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_livre) REFERENCES Livres(id_livre) ON DELETE CASCADE
);
