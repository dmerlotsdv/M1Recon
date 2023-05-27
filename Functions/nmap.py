import nmap


#Récupération de l'input utilisateur et affichage des différente option sous forme de menu avec message d'erreur si inccorect
#Ask for user input and display option in menu, also print a error message if data is incorret.

class Nmap:
    def setup(self):
        target = input("IP target: ")
        type_scan = int(input("Which type of scan do you want to run? (1-5): \n1. Scan rapide\n2. Scan hôtes actifs\n3. Scan port\n4. Scan script\n5. Scan complet\n"))
        if type_scan < 1 or type_scan > 5:
            print("Invalid input")
            return None, None
        return target, type_scan

#Fonction pour lancer le scan
#Function to run scan


    def run_scan(self, target, arguments):
        nm = nmap.PortScanner()
        nm.scan(hosts=target, arguments=arguments)

        scan_results = nm.csv()

#chemin de sortie de la data du scan.
#This is where the data is saved.


        output_file = "/home/parrot/reports/nmap.txt"  # Chemin fixe pour le fichier de sortie avec l'extension .txt
        with open(output_file, "w") as f:
            f.write(scan_results)

        print("Scan completed. Results saved.", output_file)

#Fonction pour changer le type de scan en fonction de l'input utilisateur
#Function to adapt the type of scan
    def execute(self):
        target, type_scan = self.setup()
        if target is None or type_scan is None:
            return

        if type_scan == 1:
            arguments = "-F"
        elif type_scan == 2:
            arguments = "-sn"
        elif type_scan == 3:
            ports = input("Enter port(s) to scan (separated by commas): ")
            arguments = "-p" + ports
        elif type_scan == 4:
            arguments = "-sC"
        elif type_scan == 5:
            arguments = "-sN -p- -sV -sC"
        else:
            print("Invalid input")
            return

        self.run_scan(target, arguments)

if __name__ == '__main__':
    nmap = Nmap()
    nmap.execute()
