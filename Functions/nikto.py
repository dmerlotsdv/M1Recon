import subprocess

class Nikto:
    def execute(self):
        url = input("Enter a URL: ")
        command = f"nikto -h {url} -o /home/parrot/reports/nikto.txt -Format txt"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    nikto = Nikto()
    nikto.execute()
