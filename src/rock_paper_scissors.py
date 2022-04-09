'''
NAME
    rock_paper_scissors

VERSION
    1.0

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

# 1. Inicio
import random

# 2. Definir opciones validas
possible_choices = ["rock", "paper", "scissors"]

# 3. Leer eleccion del usuario desde teclado
user_choice = input("\nEnter a choice (rock, paper, scissors): ")

# 4. Estandarizar formato del texto de la eleccion del usuario
user_choice = user_choice.lower()

# 5. Si la eleccion del usuario no es valida, entonces
if user_choice not in possible_choices:
    # Imprimir mensaje de error y terminar el programa
    print("\nError: The choice is not valid.\n")
    exit()

# 6. Calcular eleccion de la computadora
computer_choice = random.choice(possible_choices)

# 7. Imprimir eleccion de usuario y de computadora
print(f"\nUser chose {user_choice}, computer chose {computer_choice}.\n")

# 8. Comparar eleccion del usuario con eleccion de la computadora

# 8.1. Si la eleccion del usuario y de la computadora son iguales
if user_choice == computer_choice:
    # Imprimir "Tie"
    print("Tie!\n")

# 8.2. Si la eleccion del usuario es "rock", entonces
elif user_choice == "rock":
    # 8.2.1. Si la eleccion de la computadora es "paper", entonces
    if computer_choice == "paper":
        # Imprimir "Computer wins!"
        print("Computer wins!\n")
    # 8.2.2. Si la eleccion de la computadora es "scissors", entonces
    else:
        # Imprimir "User wins!"
        print("User wins!\n")

# 8.3. Si la eleccion del usuario es "paper", entonces
elif user_choice == "paper":
    # 8.3.1. Si la eleccion de la computadora es "rock", entonces
    if computer_choice == "rock":
        # Imprimir "User wins!"
        print("User wins!\n")
    # 8.3.2. Si la eleccion de la computadora es "scissors", entonces
    else:
        # Imprimir "Computer wins!"
        print("Computer wins!\n")

# 8.4. Si la eleccion del usuario es "scissors", entonces
else:
    # 8.4.1. Si la eleccion de la computadora es "rock", entonces
    if computer_choice == "rock":
        # Imprimir "Computer wins!"
        print("Computer wins!\n")
    # 8.4.2. Si la eleccion de la computadora es "paper", entonces
    else:
        # Imprimir "User wins!"
        print("User wins!\n")

# 9. Fin
