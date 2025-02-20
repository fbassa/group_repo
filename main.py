#start the game, yes

import random

def get_computer_choice():
    return random.choice(['sasso', 'carta', 'forbice'])

def get_user_choice():
    scelta = input("Scegli tra sasso, carta o forbice: ").lower()
    while scelta not in ['sasso', 'carta', 'forbice']:
        print("Scelta non valida. Riprova.")
        scelta = input("Scegli tra sasso, carta o forbice: ").lower()
    return scelta

def determina_vincitore(utente, computer):
    if utente == computer:
        return "Pareggio!"
    elif (utente == 'sasso' and computer == 'forbice') or \
         (utente == 'carta' and computer == 'sasso') or \
         (utente == 'forbice' and computer == 'carta'):
        return "Hai vinto!"
    else:
        return "Hai perso!"
    
def main():
    print("Benvenuto a Sasso, Carta, Forbice!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"Hai scelto: {user_choice}")
    print(f"Il computer ha scelto: {computer_choice}")
    
    risultato = determina_vincitore(user_choice, computer_choice)
    print(risultato)

if __name__ == "__main__":
    main()