'''
NAME
    rock_paper_scissors

VERSION
    3.0

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

# Solicitar su nombre al usuario
user_name = input("\nPlease, enter your name: ")

# Definir opciones validas
possible_choices = ["rock", "paper", "scissors"]

# Permitir que el usuario juegue mientras diga que desea seguir jugando
play_again = "yes"
while play_again.lower() == "yes":

    # Leer eleccion de usuario desde teclado y estandarizar a minusculas
    user_choice = input("\n\nEnter a choice (rock, paper, scissors): ")
    user_choice = user_choice.lower()

    # Si la eleccion del usuario no es valida, indicar error y terminar
    if user_choice not in possible_choices:
        print("\nError: The choice is not valid.\n")
        exit()

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
        # Si la eleccion de la computadora es "paper", computadora gana
        if computer_choice == "paper":
            print("Computer wins!\n")
        # Si la eleccion de la computadora es "scissors", usuario gana
        else:
            print(f"{user_name} wins!\n")

    # Si la eleccion del usuario es "paper"...
    elif user_choice == "paper":
        # Si la eleccion de la computadora es "rock", usuario gana
        if computer_choice == "rock":
            print(f"{user_name} wins!\n")
        # Si eleccion de la computadora es "scissors", computadora gana
        else:
            print("Computer wins!\n")

    # Si eleccion del usuario es "scissors"...
    else:
        # Si la eleccion de la computadora es "rock", computadora gana
        if computer_choice == "rock":
            print("Computer wins!\n")
        # Si la eleccion de la computadora es "paper", usuario gana
        else:
            print(f"{user_name} wins!\n")
    
    # Preguntar al usuario si desea jugar de nuevo
    play_again = input("Play again? (yes/no): ")

# Agradecer al usuario por jugar
print("\nThanks for playing!\n\n")