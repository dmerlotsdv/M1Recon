import subprocess

class Mirror:
    def execute(self):
        url = input("Enter a URL: ")
        command = f"httrack {url} -o /parrot/home/reports/httrack/"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    mirror = Mirror()
    mirror.execute()

#Ce script apelle un shell pour lancer l'outil httrack et défini ou seront stocké les données.
#This script calls a shell to lauch httrack and specify where the data is stored after the execution.