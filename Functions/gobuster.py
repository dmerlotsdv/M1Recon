import subprocess
import os
import re


#Fonction pour récupérer l'input user avec verification de la données entrée via une regex pour les IP et URL, affichage du menu et des wordlist disponible ainsi que définition d'une worlist par defaut.
#Function to get user input and check input wia a RegEx for URL/IP , display a menu, worlist and set a default wordlist.
class Gobuster:
    def get_user_input(self):
        while True:
            url = input("Enter a URL or an IP address: ")
            if not re.match("^(?:(?:https?|ftp):\/\/)?(?:www\.)?(?:[\w-]+\.)+[a-zA-Z]{2,}(?::\d{1,5})?(?:\/\S*)?|(?:\d{1,3}\.){3}\d{1,3}|(?:https?|ftp):\/\/(?:\d{1,3}\.){3}\d{1,3}(?::\d{1,5})?(?:\/\S*)?$", url):
                print(f"Invalid input.")
            else:
                choice = input("choose the enumeration type: \n1. Dir\n2. Dns\n3. Vhost\n4. Fuzz\n5. s3\n")
                wordlists = self.get_wordlists()
                print("Wordlist available:")
                for i, wordlist in enumerate(wordlists):
                    print(f"{i+1}. {wordlist}")
                wordlist_choice = input("Choose the wordlist (enter the corresponding number): ")
                if not wordlist_choice.isdigit() or int(wordlist_choice) not in range(1, len(wordlists) + 1):
                    print(f"Invalid input. Using default wordlist")
                    wordlist_path = "/usr/share/seclists/Discovery/Web-Content/dirsearch.txt"
                else:
                    wordlist_path = wordlists[int(wordlist_choice) - 1]
                return url, choice, wordlist_path


#This function takes the available wordlist in path and create a list to display
#Cette fonction recupère les wordlist dans le dossier et crée une liste qui sera affichée plus tard.
    def get_wordlists(self):
        wordlist_dir = "/usr/share/seclists/Discovery/Web-Content"
        wordlists = []
        if os.path.exists(wordlist_dir):
            for root, dirs, files in os.walk(wordlist_dir):
                for file in files:
                    wordlists.append(os.path.join(root, file))
        else:
            print(f"Wordlist directory {wordlist_dir} does not exist.")
        return wordlists

#Fonction pour lancer l'outil avec un fichier de sortie prédefinie pour la données.
#Function to launch the tool and specify where data is stored post execution.

    def run_gobuster(self, mode, url, wordlists):
        subprocess.Popen(["mate-terminal", "--", "gobuster", mode, "-u", url, "-w", wordlists, "-o", "/home/parrot/reports/gobuster.txt"])

#Function to allow user to adapt the type of enumeration wanted.
#Fonction pour adapter le type d'enumeration voulue par l'utilisateur.

    def execute(self):
        url, choice, wordlist = self.get_user_input()
        if choice == "1":
            self.run_gobuster("dir", url, wordlist)
        elif choice == "2":
            self.run_gobuster("dns", url, wordlist)
        elif choice == "3":
            self.run_gobuster("vhost", url, wordlist)
        elif choice == "4":
            self.run_gobuster("fuzz", url, wordlist)
        elif choice == "5":
            self.run_gobuster("fuzz", url, wordlist)
        else:
            print("Invalid input. Please enter a valid choice (1 to 5)")

if __name__ == '__main__':
    gobuster = Gobuster()
    gobuster.execute()
