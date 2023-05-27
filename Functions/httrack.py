import subprocess

class Mirror:
    def execute(self):
        url = input("Enter a URL: ")
        command = f"httrack {url} -o /parrot/home/reports/httrack/"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    mirror = Mirror()
    mirror.execute()

