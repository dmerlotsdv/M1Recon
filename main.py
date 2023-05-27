#Import de core.py qui est mon moteur du programme et import des fonctions transverale du programme
#Import of core.py which is the program engine and import of constant functions

import core
from Transversal.primary import end_program

# Main Loop
#Boucle principale du programme

while True:
    try:
        core.main_menu()
    except KeyboardInterrupt:
        end_program()
