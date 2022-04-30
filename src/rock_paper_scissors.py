'''
NAME
    rock_paper_scissors

VERSION
    4.0

AUTHOR
    Gabriel Ramirez Vilchis

GITHUB
    https://github.com/gabrielramirezv/Programacion_en_Python/blob/master/src/rock_paper_scissors.py

DESCRIPTION
    Juego "piedra, papel o tijeras" entre computadora y usuario
    Se pide eleccion al usuario y computadora elige aleatoriamente

CATEGORY
    Game

USAGE
    py src/rock_paper_scissors.py

ARGUMENTS
    None

INPUT
    Eleccion del usuario entre "rock", "paper" o "scissors"

OUTPUT
    Opciones elegidas y notificacion sobre ganador del juego

SEE ALSO
    None

'''

import random

# Definir errores para inputs no validos
class InvalidChoiceError(Exception):
    pass

class PlayAgainError(Exception):
    pass

# Solicitar su nombre al usuario
user_name = input("\nPlease, enter your name: ")

# Definir opciones validas
possible_choices = ["rock", "paper", "scissors"]

# Permitir que el usuario juegue mientras diga que desea seguir jugando
play_again = "yes"
while play_again == "yes":

    # Leer eleccion de usuario desde teclado y estandarizar a minusculas
    user_choice = input("\n\nEnter a choice (rock, paper, scissors): ")
    user_choice = user_choice.lower()

    # Intentar evaluar resultado del juego
    try:
        # Si la eleccion no es valida, generar InvalidChoiceError()
        if user_choice not in possible_choices:
            raise InvalidChoiceError("The choice is not valid.")

        # Calcular eleccion de la computadora
        computer_choice = random.choice(possible_choices)

        # Imprimir eleccion de usuario y de computadora
        print(f"\n{user_name} chose {user_choice}\
            \nComputer chose {computer_choice}\n")

        # Comparar elecciones de usuario y computadora
        # Si son iguales, imprimir empate
        if user_choice == computer_choice:
            print("Tie!\n")

        # Si la eleccion del usuario es "rock"...
        elif user_choice == "rock":
            # Si eleccion de computadora es "paper", computadora gana
            if computer_choice == "paper":
                print("Computer wins!\n")
            # Si eleccion de computadora es "scissors", usuario gana
            else:
                print(f"{user_name} wins!\n")

        # Si la eleccion del usuario es "paper"...
        elif user_choice == "paper":
            # Si eleccion de computadora es "rock", usuario gana
            if computer_choice == "rock":
                print(f"{user_name} wins!\n")
            # Si eleccion de computadora es "scissors", computadora gana
            else:
                print("Computer wins!\n")

        # Si eleccion del usuario es "scissors"...
        else:
            # Si eleccion de computadora es "rock", computadora gana
            if computer_choice == "rock":
                print("Computer wins!\n")
            # Si eleccion de computadora es "paper", usuario gana
            else:
                print(f"{user_name} wins!\n")

        # Preguntar al usuario si desea jugar de nuevo
        play_again = input("\nPlay again? (yes/no): ").lower()
        
        # Si la respuesta no es valida, generar PlayAgainError()
        if (play_again != "yes") and (play_again != "no"):
            raise PlayAgainError("The choice is not valid.")

    # Si la eleccion del usuario no es valida, notificarlo
    except InvalidChoiceError as invalid_choice_error:
        print(invalid_choice_error.args[0] + " Try again!\n")

    # Si la respuesta a jugar de nuevo es ambigua, preguntar de nuevo
    except PlayAgainError as play_again_error:
        while play_again != "yes" and play_again != "no":
            print(play_again_error.args[0] 
                  + " Please, tell us if you want to play again.\n")
            play_again = input("Play again? (yes/no): ").lower()

# Agradecer al usuario por jugar
print(f"\n\nThanks for playing, {user_name}! :) \n\n")