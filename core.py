import threading

from Functions.gobuster import Gobuster
from Functions.httrack import Mirror
from Functions.nikto import Nikto
from Functions.nmap import Nmap
from Functions.Dorks import Dorks

from menu.allmenu import show_main_menu


# Main Menu
# Menu Principal

def get_user_input():
    while True:
        try:
            print(f"Choose your warrior (1-5)")
            value = int(input("Toolbox >>> "))
            if value >= 0:
                return value
            else:
                print(f"\n Please enter a valid option number")
        except KeyboardInterrupt:
            return


def main_menu():
    show_main_menu()
    user_input = get_user_input()

    if user_input == 1:
        gobuster = Gobuster()
        gobuster.execute()

    if user_input == 2:
        mirror = Mirror()
        mirror.execute()

    if user_input == 3:
        nikto = Nikto()
        nikto.execute()

    if user_input == 4:
        nmap = Nmap()
        nmap.execute()

    if user_input == 5:
        dorks = Dorks()
        dorks.execute()
