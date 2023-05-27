import subprocess
import os
import re


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

    def run_gobuster(self, mode, url, wordlists):
        subprocess.Popen(["mate-terminal", "--", "gobuster", mode, "-u", url, "-w", wordlists, "-o", "/home/parrot/result.txt"])

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
