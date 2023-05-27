import re
from googlesearch import search

class Dorks:
    def __init__(self):
        self.target = None
        self.dork_type = None

    def execute(self):
        self.target = input("Please enter your target domain:\n")
        # Regex à changer
        if not re.match("^(?:https?:\/\/)?(?:[\w-]+\.)+[a-zA-Z]{2,}(?:\/[^\s]*)?$", self.target):
            print("Invalid domain")
            return

        print("\n1. admin page\n2. pdf\n3. config wp\n4. log passwd\n")

        self.dork_type = int(input("Please choose a dork type:\n"))
        if self.dork_type < 1 or self.dork_type > 4:
            print("Invalid input")
            return

        if self.dork_type == 1:
            query = f"site:{self.target} inurl:admin"
        elif self.dork_type == 2:
            query = f"site:{self.target} filetype:pdf"
        elif self.dork_type == 3:
            query = f"site:{self.target} inurl:wp-config.php"
        elif self.dork_type == 4:
            query = f"site:{self.target} intext:'password' filetype:log"

        for url in search(query, tld="com", lang="en", num=10, start=0, stop=None, pause=2):
            print(url)

if __name__ == '__main__':
    dorks = Dorks()
    dorks.execute()