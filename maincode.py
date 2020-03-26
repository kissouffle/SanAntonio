import random

# Liste de citations
quotes = ["Salut tout le monde", "Comment ça va aujourd'hui?", "Qu'as tu mangé ce midi?", "Ca te dirait de sortir ce soir?"]
# Liste de personnages
characters = ["Pierre", "Marine", "Paul","Jacques"]


# Continuer ou non le programme
user_answer = input("Appuyez sur A pour continuer ou B pour quitter : ")

# Fonction permettant de générer aléatoirement des items de chaque liste
def show_random_quote(char_list, quote_list):
    
    random_char_num = random.randint(0 , len(char_list) - 1)
    m_char = char_list[random_char_num]
    m_char = m_char.upper() 
    
    random_quote_num = random.randint(0 , len(quote_list) - 1)
    quote = quote_list[random_quote_num]

    print(m_char, " : ", quote)

# Boucle permettant de poursuivre le programme tant que"B" n'est pas utilisé
while user_answer != "B":
    show_random_quote(characters, quotes)
    user_answer = input("Appuyez sur A pour continuer ou B pour quitter : ")
else:
    print("FIN DU PROGRAMME")
    pass

