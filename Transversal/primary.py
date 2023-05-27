import sys

# Fonction d'arret du programme

def end_program():
    if KeyboardInterrupt:
        print(f"\n Mischief Managed ! ")
        sys.exit()
