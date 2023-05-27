import subprocess

class Nikto:
    def execute(self):
        url = input("Enter a URL: ")
        command = f"nikto -h {url} -o /home/parrot/reports/nikto.txt -Format txt"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    nikto = Nikto()
    nikto.execute()

#This script calls a shell to execute Nikto tool. More options to come in the futur.
#Ce script apelle une invite de commande pour lancer l'outil nikto. Améliorations a venir.
