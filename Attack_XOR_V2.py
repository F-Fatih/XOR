import os
from XOR import XOR
import string
import itertools
import time

xor = XOR()
liste_mots_FR = ["je", "tu", "il", "elle", "nous", "vous", "ils", "elles", "être", "avoir", "faire", "code", "dire", "pouvoir", "vouloir", "voir", "savoir", "venir", "aller", "prendre", "donner", "mettre", "aimer", "devoir", "parler", "demander", "trouver", "regarder", "croire", "falloir", "aider", "jouer", "travailler", "manger", "écouter", "lire", "écrire", "vivre", "sentir", "penser", "choisir", "commencer", "finir", "chercher", "réussir", "oublier", "rester", "marcher", "répondre", "expliquer", "cacher", "montrer", "utiliser", "mon", "attendre", "réaliser", "réparer", "visiter", "répéter", "baisser", "augmenter", "temps", "année", "jour", "moment", "chose", "homme", "femme", "enfant", "maison", "voiture", "argent", "travail", "espace", "question", "réponse", "chambre", "porte", "fenêtre", "ville", "pays", "rue", "salle", "table", "chaise", "lumière", "ombre", "ciel", "terre", "mer", "montagne", "fleur", "arbre", "animal", "chat", "chien", "oiseau", "poisson", "nourriture", "boisson", "amis", "famille", "école", "professeur", "élève", "livre", "ordinateur", "téléphone", "musique", "film", "sport", "jeux", "saison", "été", "hiver", "printemps", "automne", "chaussure", "vêtement", "parapluie", "écharpe", "montre", "sac", "clé", "bouteille", "assiette", "fourchette", "couteau", "cuillère", "couvert", "plat", "menu", "restaurant", "marché", "supermarché", "boulangerie", "pharmacie", "hôpital", "banque", "poste", "gare", "aéroport", "centre-ville", "triste", "heureux", "beau", "laid", "grand", "petit", "jeune", "vieux", "nouveau", "ancien", "fort", "faible", "rapide", "lent", "facile", "difficile", "long", "court", "chaud", "froid", "mouillé", "sec", "propre", "sale", "ouvert", "fermé", "lourd", "léger", "tôt", "tard", "bientôt", "loin", "près", "bruyant", "silencieux","Bonjour", "doux", "amer", "salé", "sucré", "cher", "bon marché", "moderne", "plein", "vide", "serré", "large", "connu", "inconnu", "bien", "mal", "très", "trop", "vite", "lentement", "venez", "souvent", "rarement", "toujours", "jamais", "parfois", "ici", "là", "ailleurs", "hier", "aujourd'hui", "demain", "ensemble", "seul", "près de", "loin de", "vers", "par", "pour", "contre", "en", "de", "à", "dans", "sur", "sous", "entre", "devant", "derrière", "à travers", "auprès de", "envers", "au-delà de", "en face de", "malgré", "avant", "après", "pendant", "selon", "essayer", "jusqu'à", "au milieu de"]

def trouver_clef(message_code, caractere_min, caractere_max):

    # Teste toutes les combinaisons de clefs possibles
    for longueur in range(caractere_min, caractere_max + 1):
        for clef in itertools.product(string.ascii_lowercase, repeat=longueur):
            clef_string = str().join(clef)
            print(f"Test de la clef : {clef_string}")
            
            try:
                # Déchiffre le message
                dechiffrer_message = xor.Dechiffrer_XOR(message_code, clef_string)
                
                # Divise le message en mots
                mots = dechiffrer_message.split()
                
                # Compte le nombre de mots français
                compteur_mots_FR = 0
                for mot in mots:
                    if mot.lower() in liste_mots_FR:
                        compteur_mots_FR += 1
                
                # Si 3 mots français ou plus sont trouvés, retourne le résultat
                if compteur_mots_FR >= 3:
                    return f"Clef : {clef_string}\nMessage : {dechiffrer_message}\nNombre de mots français : {compteur_mots_FR}"
                
            except Exception as e:
                print(f"Échec du décodage avec la clef {clef_string}: {e}")

    return "Clef non trouvée"

message = "JBoABBYYE0JGAwEbCk0XCwgQFE4dSgQdFRQXCwtNDAEIVQ0BHQhBTw=="
print(trouver_clef(message, 2, 8))